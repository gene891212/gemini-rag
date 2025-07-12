# Gemini RAG System

使用 Google Gemini API 和 ChromaDB 實現的檢索增強生成（RAG）系統。專案展示如何構建一個問答系統，能夠基於文件內容回答使用者問題。

> 專案基於 [BiliBili 教學影片](https://www.bilibili.com/video/BV168j7zCE6D) 修改而成。

## 📖 範例文檔

本專案使用的範例文檔 `full.md` 是多頻段 MIMO 天線系統的論文：

**"A 10 x 10 Multi-Band MIMO Antenna System for LTE, 5G, Wi-Fi 7, and X-Band Communication Applications"**

- **論文來源**: [IEEE Xplore](https://ieeexplore.ieee.org/document/10879367)
- **研究領域**: 無線通訊、天線設計、MIMO 技術
- **內容概要**: 介紹了一個支援 LTE、5G、Wi-Fi 7 和 X 波段通訊應用的 10×10 多頻段 MIMO 天線系統

## 🚀 快速開始

### 1. 下載專案

```bash
git clone https://github.com/gene891212/gemini-rag.git
cd gemini-rag
```

### 2. 安裝環境

```bash
# 使用 uv（推薦）
uv sync

# 或使用 pip
pip install .
```

### 3. 環境設置

創建 `.env` 文件並添加您的 Google AI API 密鑰：

```bash
echo "GOOGLE_API_KEY=your_api_key_here" > .env
```

> 📝 **獲取 API 密鑰**: 前往 [Google AI Studio](https://aistudio.google.com/app/apikey) 獲取免費的 API 密鑰

### 4. 準備文檔

將您要處理的 Markdown 文檔放入專案目錄，或使用提供的範例文檔 `full.md`。

### 5. 開始使用

#### 方法一：直接使用（推薦新手）

```bash
python gemini_rag.py
```

程式會自動檢查是否需要建立資料庫，並進入互動式問答模式。

#### 方法二：手動建立資料庫

```bash
# 建立向量資料庫
python gemini_rag.py --create-db

# 進入互動演示
python gemini_rag.py --demo
```

## 💡 使用範例

### 互動式問答

```
🤖 Gemini RAG System Demo
==================================================
📊 Database contains 145 document chunks

💬 Ask questions about the document (type 'quit' to exit):

📝 Example questions:
   1. What are the main applications of this antenna system?
   2. What frequency ranges does this antenna support?
   3. What are the advantages of this MIMO system?

❓ Your question: 
```

## ⚙️ 配置選項

可以在 `gemini_rag.py` 文件頂部修改以下配置：

```python
CHUNK_SIZE = 1200                    # 文本塊大小
CHUNK_OVERLAP = 150                  # 文本塊重疊
QUERY_RESULTS_LIMIT = 5              # 檢索結果數量
API_RATE_LIMIT_DELAY = 20            # API 調用間隔（秒）
```

## 🔧 命令行選項

```bash
python gemini_rag.py              # 互動式（推薦）
python gemini_rag.py --create-db  # 僅建立向量資料庫
python gemini_rag.py --demo       # 進入互動演示
python gemini_rag.py --help       # 顯示幫助信息
```

## 🚨 注意事項

1. **API 費用**: Google Gemini API 有使用配額，請注意使用量
2. **建立資料庫時間**: 若是使用免費API，首次建立資料庫可能需要幾分鐘，注意不要將`API_RATE_LIMIT_DELAY`時間設置太短
3. **資料庫**: ChromaDB 資料庫會保存在本地，無需重複建立
