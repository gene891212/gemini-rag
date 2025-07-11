"""
Gemini RAG (Retrieval-Augmented Generation) System

This module provides functionality for:
- Text chunking and processing
- Document embedding using Google Gemini
- Vector storage with ChromaDB
- Question answering with context retrieval
"""

import time
from typing import List

import chromadb
import dotenv
from google import genai
from google.genai import types
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load environment variables
dotenv.load_dotenv()

# Configuration constants
GEMINI_EMBEDDING_MODEL = "gemini-embedding-exp-03-07"
GEMINI_LLM_MODEL = "gemini-2.5-flash"
CHROMA_DB_PATH = "./chroma.db"
COLLECTION_NAME = "genehsieh"
CHUNK_SIZE = 1200
CHUNK_OVERLAP = 150
QUERY_RESULTS_LIMIT = 5
API_RATE_LIMIT_DELAY = 20  # seconds

# Initialize clients
gemini_client = genai.Client()
vector_db_client = chromadb.PersistentClient(CHROMA_DB_PATH)
document_collection = vector_db_client.get_or_create_collection(COLLECTION_NAME)

# Initialize text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
    length_function=len,
)


def split_text_into_chunks(text: str) -> List[str]:
    """
    Split text into manageable chunks for processing.

    Args:
        text: Input text to be split

    Returns:
        List of text chunks
    """
    chunks = text_splitter.split_text(text)
    return chunks


def generate_text_embedding(text: str, is_document: bool = True) -> List[float]:
    """
    Generate embedding for text using Google Gemini embedding model.

    Args:
        text: Text to embed
        is_document: True if embedding a document for storage,
                    False if embedding a query

    Returns:
        List of embedding values
    """
    task_type = "RETRIEVAL_DOCUMENT" if is_document else "RETRIEVAL_QUERY"

    response = gemini_client.models.embed_content(
        model=GEMINI_EMBEDDING_MODEL,
        contents=text,
        config=types.EmbedContentConfig(task_type=task_type),
    )

    assert response.embeddings, "No embeddings returned from API"
    assert response.embeddings[0].values, "No embedding values returned"

    return response.embeddings[0].values


def create_vector_database(markdown_file_path: str = "full.md") -> None:
    """
    Create vector database from markdown file.

    Args:
        markdown_file_path: Path to the markdown file to process
    """
    print(f"Loading text from {markdown_file_path}...")

    with open(markdown_file_path, "r", encoding="utf-8") as file:
        document_text = file.read()

    text_chunks = split_text_into_chunks(document_text)
    total_chunks = len(text_chunks)

    print(f"Processing {total_chunks} chunks...")

    for chunk_index, chunk_text in enumerate(text_chunks):
        chunk_number = chunk_index + 1
        print(f"Processing chunk {chunk_number}/{total_chunks}")

        # Skip already processed chunks (for resuming interrupted runs)
        if chunk_number <= 11:
            continue

        try:
            chunk_embedding = generate_text_embedding(chunk_text, is_document=True)

            document_collection.upsert(
                ids=str(chunk_index), documents=chunk_text, embeddings=chunk_embedding
            )

            print(f"✓ Chunk {chunk_number} successfully stored")

            # Rate limiting to avoid API limits
            if chunk_number < total_chunks:
                time.sleep(API_RATE_LIMIT_DELAY)

        except Exception as e:
            print(f"✗ Error processing chunk {chunk_number}: {e}")
            continue


def query_similar_documents(question: str) -> List[str]:
    """
    Query the vector database for documents similar to the question.

    Args:
        question: User's question

    Returns:
        List of relevant document chunks
    """
    question_embedding = generate_text_embedding(question, is_document=False)

    search_results = document_collection.query(
        query_embeddings=question_embedding, n_results=QUERY_RESULTS_LIMIT
    )

    assert search_results["documents"], "No documents returned from query"
    return search_results["documents"][0]


def generate_answer_with_context(question: str) -> str:
    """
    Generate an answer to the question using retrieved context.

    Args:
        question: User's question

    Returns:
        Generated answer
    """
    print("🔍 Searching for relevant context...")
    relevant_documents = query_similar_documents(question)

    print("🤖 Generating answer...")

    # Construct prompt with context
    context_separator = "\n" + "-" * 50 + "\n"
    context_text = context_separator.join(relevant_documents)

    prompt = f"""Please answer the user's question based on the provided context.

Question: {question}

Context:
{context_text}

Please provide an accurate, concise and powerful answer based on the above."""

    response = gemini_client.models.generate_content(
        model=GEMINI_LLM_MODEL, contents=prompt
    )

    return response._get_text()


def check_database_exists() -> bool:
    """Check if the vector database exists and has documents."""
    try:
        result = document_collection.count()
        return result > 0
    except Exception:
        return False


def interactive_demo():
    """Interactive demonstration of the RAG system."""
    print("🤖 Gemini RAG System Demo")
    print("=" * 50)

    # Check if database exists
    if not check_database_exists():
        print("⚠️  Vector database not found or empty!")
        print("\nOptions:")
        print("1. Create database from full.md")
        print("2. Exit and manually create database")

        choice = input("\nEnter your choice (1/2): ").strip()

        if choice == "1":
            print("\n🔧 Creating vector database...")
            try:
                create_vector_database()
                print("✅ Database created successfully!")
            except Exception as e:
                print(f"❌ Error creating database: {e}")
                return
        else:
            print("\nPlease run: python gemini_rag.py --create-db")
            return

    print(f"\n📊 Database contains {document_collection.count()} document chunks")

    # Interactive Q&A loop
    print("\n💬 Ask questions about the document (type 'quit' to exit):")

    example_questions = [
        "What are the main applications of this antenna system?",
        "What frequency ranges does this antenna support?",
        "What are the advantages of this MIMO system?",
    ]

    print("\n📝 Example questions:")
    for i, q in enumerate(example_questions, 1):
        print(f"   {i}. {q}")
    print()

    while True:
        try:
            question = input("❓ Your question: ").strip()

            if question.lower() in ["quit", "exit", "q"]:
                print("👋 Goodbye!")
                break

            if not question:
                continue

            print("\n" + "=" * 60)
            print(f"Question: {question}")
            print("=" * 60)

            answer = generate_answer_with_context(question)
            print(answer)
            print("\n" + "-" * 60 + "\n")

        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}\n")


def main():
    """Main function with command line interface."""
    import sys

    if len(sys.argv) > 1:
        if sys.argv[1] == "--create-db":
            print("🔧 Creating vector database...")
            try:
                create_vector_database()
                print("✅ Database created successfully!")
            except Exception as e:
                print(f"❌ Error creating database: {e}")
        elif sys.argv[1] == "--demo":
            interactive_demo()
        elif sys.argv[1] == "--help":
            print("Gemini RAG System")
            print("\nUsage:")
            print("  python gemini_rag.py              # Interactive demo")
            print("  python gemini_rag.py --create-db  # Create vector database")
            print("  python gemini_rag.py --demo       # Interactive demo")
            print("  python gemini_rag.py --help       # Show this help")
        else:
            print(f"Unknown option: {sys.argv[1]}")
            print("Use --help for available options")
    else:
        interactive_demo()


if __name__ == "__main__":
    main()
