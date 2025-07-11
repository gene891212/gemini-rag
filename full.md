# A 10 x 10 Multi-Band MIMO Antenna System for LTE, 5G, Wi-Fi 7, and X-Band Communication Applications

MING- AN CHUNG, (Senior Member, IEEE), KAI- XIANG CHEN, CHIA- CHUN HSU, AND CHIA- WEI LIN

Department of Electronic Engineering, National Taipei University of Technology, Taipei City 10608, Taiwan

Corresponding author: Ming- An Chung (mingannchung@ntut.edu.tw)

This work was supported by the National Science and Technology Council, Taiwan, under Grant NSTC 113- 2221- E- 027- 068.

ABSTRACT To attend with the needs of modern wireless communication equipment, this paper proposes a multi- band planar antenna MIMO system. The antenna system operates in the frequency range of 0.8- 1.04 GHz, 1.6- 2.71 GHz, and 4.69- 11.5 GHz, supporting LTE, 5G NR, Wi- Fi 7, and X bands. The antenna proposed in this paper is  $60\mathrm{mm}\times 10\mathrm{mm}$ . A feed- through coupling structure reduces its size and achieves broadband coverage to adapt to increasingly compact electronic communication. The design uses multi- branch microstrip lines and long slot structures to ensure high gain and high efficiency over a wide spectrum and achieve omnidirectional radiation of the antenna. In the proposed MIMO antenna system, the envelope correlation coefficient (ECC) remains below 0.5 and even approaches zero at high frequencies. Additionally, the system maintains overall isolation below - 10 dB, demonstrating excellent signal isolation and anti- interference capabilities. In order to confirm the impact of antenna radiation on the human body, the analysis results of the specific absorption rate (SAR) and power density (PD) confirmed that the radiation impact of the antenna system on the human body is lower than the international standard value. The MIMO antenna system proposed in this paper is simple in design and doesn't require additional passive components in the circuit, which greatly reduces the manufacturing cost. When integrated into laptops, routers, and smartphones, it exhibits stable antenna performance, making it efficient and flexible for application in a variety of wireless communication environments.

INDEX TERMS 5G NR, LTE, X- band, Wi- Fi 7, specific absorption rate (SAR), MIMO, planar antenna, multi- band antenna.

# I. INTRODUCTION

With the development of high- speed wireless communications, multiple- input multiple- output (MIMO) technology has become one of the key technologies to improve system capacity, spectrum efficiency and data transmission rate in modern communications. MIMO technology uses multiple antennas to transmit and receive data simultaneously, which can't only effectively enhance channel capacity but also achieve higher data rates without increasing bandwidth [1], [2]. In addition, accurate direction- of- arrival estimation (DoA) plays an important role in smart antenna design in MIMO systems. It has a critical impact on realizing spatial signal processing, beamforming, and improving link reliability [3]. By increasing the number of antennas, the system can not only improve channel stability [4], but also use multiple independent signals to achieve multiplexing, thereby increasing the total signal transmission volume [5]. Currently, MIMO antennas are widely applied in various portable and industrial devices such as smartphones [6], laptops [7], autonomous aerial vehicles (AAVs) [8], and routers [9], [10] to improve communication stability and signal reliability. However, due to the limited space of the device, how to achieve multi- band response in

a compact structure while achieving high isolation and low mutual coupling has become a major challenge in antenna design [11], [12]. As the number of antennas increases, it becomes essential to address the mutual influence between antennas. For instance, coupling effects can lead to reduced transmission efficiency and signal interference [13]. Numerous studies have proposed various solutions to enhance antenna isolation, including self- decoupling designs [14], employing shorting stubs to eliminate excess currents [15], and using LC circuits [16] and slot structures to minimize coupling [17].

With the growing demand for multi- band communication, the frequency range of LTE (Long- Term Evolution) spans from  $450\mathrm{MHz}$  to  $3.8\mathrm{GHz}$ . 5G NR is divided into two frequency ranges: Frequency Range 1 (FR1), covering  $410\mathrm{MHz}$  to  $7.125\mathrm{GHz}$ , and Frequency Range 2 (FR2), covering  $24.25\mathrm{GHz}$  to  $52.6\mathrm{GHz}$  [18], [19]. Wi- Fi 7 supports frequency ranges including  $2.4\mathrm{GHz}$  (2.4- 2.4835 GHz),  $5\mathrm{GHz}$  (5.15- 5.85 GHz), and  $6\mathrm{GHz}$  (5.925- 7.125 GHz) [20]. Therefore, designing compact and high- isolation multiband antennas is particularly challenging [21], [22], [23], especially in mobile devices where the limited size further increases the complexity of the design. To address these challenges, structures such as planar inverted- F antennas (PIFA) [24] and feed- coupled antennas [25], [26], as well as materials for transparent flexible antennas [27], have been widely adopted. The X- band belongs to the microwave frequency range of  $8 - 12\mathrm{GHz}$  [12]. In satellite communications, the uplink frequency range for the X- band is  $7.9 - 8.4\mathrm{GHz}$ , while the downlink frequency range is  $7.25 - 7.75\mathrm{GHz}$ . For space communication applications, such as those space stations operated by NASA or ESA, the uplink frequency range is  $7.145 - 7.235\mathrm{GHz}$ , and the downlink frequency range is  $8.4 - 8.5\mathrm{GHz}$ . Typically, reconfigurable antennas [28] or parabolic reflector antennas are employed to enhance gain and reduce mutual coupling [29]. Thus, designing multi- band antennas requires the integration of various technologies and innovations to accommodate different device deployments and achieve optimal performance. Due to their unique feed design, coupled- feed antennas can achieve multi- band coverage without increasing the antenna size, making them especially suitable for compact electronic devices. Their structural design significantly reduces antenna dimensions and eliminates the need for additional passive components [26], making them a preferred technology for multi- band antenna design.

In recent years, the increasing demand for miniaturized multi- band antennas in handheld devices and wearable gadgets has posed significant challenges for the design of compact MIMO antennas [30], [31]. The PIFA structure proposed in [30] achieves high gain and efficiency within a limited space but exhibits suboptimal performance in terms of gain and efficiency at lower frequency bands. In [31], inductors and capacitors were incorporated for impedance matching to achieve multi- band antenna functionality.

![](images/00f238013f1112974f7bd346ad3566ad66dd57ae44f4997bd381a7320ad7b6cb.jpg)  
FIGURE 1. Dimensions of the multi-band planar antenna structure.

![](images/9517d43dde68ac08eb0e72832deaf1ef8407b14c4271100f5d47bdb5b8027338.jpg)  
FIGURE 2. Equivalent circuit diagram of the multi-band planar antenna.

However, such designs often increase manufacturing complexity and costs. The practicality of flexible transparent materials is limited, making them suitable only for wearable devices due to their poor conductivity, high manufacturing costs, and complexity. These characteristics make them unsuitable for mobile phone antenna applications [32]. In [33], it is mentioned that although dipole antenna elements can improve the isolation of the antenna system, they fail to reduce the system size. Furthermore, since communication devices are often used close to the human body, Specific Absorption Rate (SAR) becomes a critical consideration in antenna design. Recent studies have focused on reducing the impact of antenna radiation on the human body. In [34], low- SAR antenna elements using TCM were employed to reduce SAR. In [31], SAR was minimized by generating adjacent countercurrents to cancel each other out. These studies indicate that future MIMO antenna designs should feature simple structures, low cost, multi- band support, and low SAR characteristics.

This paper presents a multi- branch planar antenna MIMO system based on a feed- coupled structure and long- slot design, optimized to dimensions of  $60\mathrm{mm}\times 10\mathrm{mm}$ . The proposed antenna successfully covers LTE, 5G NR, Wi- Fi 7, and X- band, achieving multi- band coverage while being compactly designed for mobile devices such as laptops, routers, and smartphones. In terms of radiation performance, the antenna adopts an omnidirectional design, effectively reducing radiation nulls and further enhancing flexibility and reliability in practical use. The substrate material selected is FR4, offering high reliability and low cost, making it suitable for mass production of current mobile products. Through

![](images/6342790ff47c3a24d8b747cf4160f4965ee5b59185075abd6b9e1ba3f69e4371.jpg)  
FIGURE 3. Evolution of multi-band planar antennas.

detailed analysis of antenna data, the proposed multi- band antenna demonstrates stable coverage, gain, and efficiency across devices of varying sizes. The envelope correlation coefficient (ECC) consistently remains below 0.5, meeting the signal independence requirements of MIMO systems. Additionally, SAR simulations were conducted to ensure compliance with human safety standards. The above discussion highlights that the proposed multi- band planar antenna MIMO system demonstrates excellent adaptability, stability, and performance. Its compact design and wideband coverage provide significant advantages in various wireless communication environments, showcasing broad application potential.

![](images/cea69ae573da34ed4707307cb7f67ff42f78efc7a09485c9643f8f3e45abe43e.jpg)  
FIGURE 4. Geometric analysis of branches in the multi-band planar antenna.

# II. ANTENNA DESIGN

# A. MINIATURIZED MULTI-BAND PLANAR ANTENNA DESIGN

Fig. 1 shows a multi- band planar antenna fabricated on an FR4 substrate. The substrate has a dielectric constant of 4.4, offering excellent dielectric properties at a low cost. The antenna dimensions are  $60~\mathrm{mm} \times 10~\mathrm{mm}$  with a thickness of  $0.8~\mathrm{mm}$ , making it suitable for the increasingly compact sizes of electronic devices. The copper conductor parts of the antenna are marked in yellow and blue, while the

substrate is depicted in green. This antenna design includes a feeding point and a grounding point, represented by red and brown dots, respectively. The coupled- feed structure used in this design enables the generation of multiple frequency bands simultaneously. This structure achieves good impedance matching through radiation between the feeding point and the grounding point. This paper designs a feedcoupled structure based on a microstrip antenna, effectively supporting multi- band operation. By optimizing the coupling mechanism between the feed point and the ground point, the structure achieves excellent impedance matching, thereby enhancing the antenna's performance and bandwidth coverage.

The design of the microstrip antenna is based on the coupling relationship between the substrate's dielectric properties and the feedline structure. To ensure the antenna exhibits desirable radiation characteristics and impedancematching performance, the design follows the formulas outlined below [35]. The microstrip feedline width  $W_{f}$  is calculated using the substrate dielectric constant  $\epsilon_{r}$  ,substrate thickness  $h$  and the target operating frequency  $f_{d}$  as shown in Equation (1). To account for the substrate edge effects,  $W_{f}$  is substituted into the calculation of the effective dielectric constant  $\epsilon_{\mathrm{eff}}$  as per Equation (2). Finally, based on the quarter- wavelength resonance principle, the microstrip line length  $L_{f}$  is determined using  $\epsilon_{\mathrm{eff}}$  , as described in Equation (3), where  $c$  represents the speed of light. The relevant equations are as follows:

$$
\begin{array}{l}{W_f = \frac{2h}{\pi} [B - 1 - ln(2B - 1)]}\\ {\quad +\frac{\epsilon_r - 1}{2\epsilon_r}\left[ln(B - 1) + 0.39 - \frac{0.61}{\epsilon_r}\right],\quad B = \frac{377\pi}{100\sqrt{\epsilon_r}}} \end{array}
$$

$$
\begin{array}{l}\epsilon_{eff} = \frac{\epsilon_r + 1}{2} +\frac{\epsilon_r - 1}{2}\left(1 + \frac{12h}{W_f}\right)^{-0.5}\\ L_f = \frac{c}{4f_d\sqrt{\epsilon_{eff}}} \end{array} \tag{3}
$$

Fig. 2 illustrates the equivalent circuit model of the antenna. A gap exists between the feed point and the ground, creating a capacitive effect that can be divided into two components:  $C_r$  and  $C_s$  .These capacitors, together with the inductance  $L$  , form a series resonant circuit, while the resistances  $C_r + C_s$  represent the energy loss characteristics of the circuit [36].

In this study, the antenna is designed for multi- band coverage, requiring the calculation of the resonant frequency  $f_{r}$  of the equivalent circuit, which is expressed in Equation 4:

$$
f_{r} = \frac{1}{2\pi\sqrt{L(C_{r} + C_{s})}} \tag{4}
$$

To further analyze the antenna's energy loss and bandwidth performance, the quality factor  $Q_{u}$  needs to be calculated. Its expression is given in Equation 5:

![](images/2045dc697b428f0878741c1a1da970e0c8c2741b3b09d9bdf24a604445db84ea.jpg)  
FIGURE 5. MIMO antenna system applied to different devices, (a) laptop, (b) router, and (c) smartphone.

$$
Q_{u} = 2\pi f_{r}\frac{C_{r} + C_{s}}{G_{r} + G_{s}} = \frac{\frac{C_{r}}{C_{s}} + 1}{\tan\delta_{s}\left(\frac{G_{r}}{G_{s}} + 1\right)} \tag{5}
$$

The formula indicates that the quality factor  $Q_{u}$  depends not only on the capacitances  $C_r,C_s$  and the resonant frequency  $f_{r}$  , but also on the loss admittance ratio  $G_{r} / G_{s}$  and the dielectric loss tan  $\delta_{s}$  . In multi- band design, by adjusting the inductance and capacitance parameters, loss optimization and bandwidth control for different frequency bands can be achieved.

# B. EVOLUTION OF MULTI-BAND PLANAR ANTENNAS

Fig. 3 illustrates the evolution process of the multi- band planar antenna. In Fig. 3(a) (Step 1), an L- shaped branch  $\mathrm{L}_1$  with dimensions of  $25\mathrm{mm}\times 5.5\mathrm{mm}$  extends from the feeding point, and a T- shaped antenna  $\mathbf{L}_2$  extends from the grounding point. Additionally, a curved branch with a length of  $20~\mathrm{mm}$  is added to the right side of  $\mathbf{L}_2$  . This structure generates multiple resonances below - 6 dB within the  $4\mathrm{- }10\mathrm{GHz}$  range. In Step 2, an additional branch  $\mathbf{L}_3$  is introduced, enabling the antenna to support  $900\mathrm{MHz}$  and  $2.4\mathrm{GHz}$  frequency bands while retaining the high- frequency range of  $4\mathrm{- }10\mathrm{GHz}$

In Fig. 3(b) (Steps 3- 4), the addition of branch L4 increases the antenna's low- frequency bandwidth. Simultaneously, branch L5 optimizes the antenna's bandwidth

![](images/839a829c51f4e2a9620aa6c81f7b3a6dcb858682d7aa59b4bea27cdd0ef83866.jpg)  
FIGURE 6. Simulation analysis of return loss and isolation for different antenna spacing in a laptop MIMO antenna system. (a) Antenna configurations with varying spacing. (b) Return loss of Ant. 1, Ant. 2, and Ant. 7. (c) Isolation of Ant. 1, Ant. 2, and Ant. 7.

at  $2.4\mathrm{GHz}$  enabling it to cover the  $1.6 - 2.6\mathrm{GHz}$  range. In Step 5, branches L6 and L7 are added to the feed antenna, as shown in Fig. 3(c). L6 ensures that the reflection coefficients for the high- frequency bands remain below - 6 dB, while  $\mathbf{L}_7$  enhances the antenna's ultra- wideband performance in the high- frequency range, covering 4.7- 11.4 GHz. Through these evolutionary steps, a single antenna can simultaneously cover both low frequencies  $(< 1\mathrm{GHz})$  and high frequencies  $(>1\mathrm{GHz})$

This study conducts a detailed analysis of the branch resonance characteristics in the antenna design. According to the results in Fig. 4(a), adjusting the length of W2 reveals that when W2 is set to  $21\mathrm{mm}$  the reflection coefficient demonstrates a relatively broader bandwidth. From the simulation data in Fig. 4(b), it is observed that setting the length of W5 to  $2\mathrm{mm}$  effectively enhances the reflection performance in the high- frequency band, while maintaining stable impedance matching in other frequency bands. In Fig. 4(c), when the length of W6 is  $4\mathrm{mm}$  the high- frequency range spans from 4.69 to  $11.5\mathrm{GHz}$  significantly improving the high- frequency response. Through these parameter adjustments, the optimal geometric dimensions of the antenna structure were determined, successfully achieving wideband coverage.

# C. CONFIGURATION OF THE MULTI-BAND PLANAR ANTENNA SYSTEM

The design MIMO antenna system can be applied to various electronic devices, such as laptops, routers, and smartphones.

For laptops, the MIMO antenna system has a ground plane size of  $330\mathrm{mm}\times 220\mathrm{mm}$  and incorporates ten identical multi- band planar antennas arranged around the perimeter. These antennas provide excellent signal coverage with minimal interference between them. For smartphones, the ground plane size is  $120\mathrm{mm}\times 70\mathrm{mm}$  with one antenna placed at the top and another at the bottom, forming a  $2\times 2$  MIMO antenna system. In routers, the ground plane is designed as a hexagon with a maximum width of  $140\mathrm{mm}$  with six antennas positioned in the center of each side. This hexagonal layout enables the router to achieve 360- degree omnidirectional signal coverage, effectively enhancing the strength and stability of the wireless signal. As shown in Fig. 5, these configurations are optimized for their respective applications.

To ensure good isolation between antennas and the stability of the reflection coefficient, this study conducts a detailed simulation analysis of the antenna spacing, evaluating the overall performance of the antennas in the MIMO system. In Fig. 6, we analyzed the impact of antenna spacing on the reflection coefficient and isolation. From Figs. 6(b) and (c), it can be observed that the antenna isolation shows no significant variation with different spacings, consistently remaining below - 10 dB. This demonstrates good mutual non- interference between the antennas. Meanwhile, the reflection coefficient also shows no significant difference under varying spacings, proving that the designed antenna exhibits excellent stability. However, when the spacing between Ant.1 and Ant.2 is set to  $5\mathrm{mm}$ ,  $\mathrm{S}_{11}$

![](images/ab315ef6053825b5838e55aa3fa1ee801c8ac101fb2ed41a9e3f1532362f0d38.jpg)  
FIGURE 7. Surface current analysis for laptop Ant.1. (a) 0.85 GHz. (b) 1 GHz. (c) 1.85 GHz. (d) 2.4 GHz. (e) 5.15 GHz. (f) 6.25 GHz. (g) 6.8 GHz. (h) 7.7 GHz. (i) 8.25 GHz. (j) 10.1 GHz. (k) 10.65 GHz.

![](images/586ab5b8217313c249ac22469547fd4cf2efa2a0454968e72438a1d2440356ef.jpg)  
FIGURE 8. Surface current analysis for laptop Ant.2. (a) 0.85 GHz. (b) 1 GHz. (c) 1.85 GHz. (d) 2.4 GHz. (e) 5.15 GHz. (f) 6.25 GHz. (g) 6.8 GHz. (h) 7.7 GHz. (i) 8.25 GHz. (j) 10.1 GHz. (k) 0.65 GHz.

demonstrates superior characteristics in the low- frequency band, while  $\mathrm{S}_{77}$  exhibits better performance in the high- frequency band. Based on this observation, the distance between Ant. 1 and Ant. 2 in the MIMO antenna system for laptops is set to  $5\mathrm{mm}$  to achieve a balanced and optimized performance across both low and high- frequency bands.

# D. MULTI-BAND PLANAR ANTENNA SURFACE CURRENT ANALYSIS

Figs. 7- 9 show the surface current simulations of Ant. 1, Ant. 2, and Ant. 7 in a laptop. The use of the coupled- feed structure identifies the regions where the current is concentrated, facilitating faster identification of branch- specific frequency bands and accelerating the optimization process. Each antenna in the proposed MIMO antenna system exhibits mirror symmetry and similar trends, allowing Ant.1, Ant.2, and Ant.7 to represent all antennas in the laptop. Similarly, for the router in Fig. 10 and the smartphone in Fig. 11, Ant.1 alone is sufficient to represent all antennas. In Fig. 7(a), at a frequency of  $0.87\mathrm{GHz}$ , the current is primarily concentrated in the branch at the upper- left corner of the ground plane. In Fig. 7(b), the current flows toward the right side

![](images/6546d899420c897b25944811387e050b7aa3b86229b1c5c7fb527d27cabe7906.jpg)  
FIGURE 9. Surface current analysis for laptop Ant.7. (a) 0.85 GHz. (b) 1 GHz. (c) 1.85 GHz. (d) 2.4 GHz. (e) 5.15 GHz. (f) 6.25 GHz. (g) 6.8 GHz. (h) 7.7 GHz. (i) 8.25 GHz. (j) 10.1 GHz. (k) 5.15 GHz.

![](images/f1efc7defabf0cd09a88515d62f48810a1ebd7df646da26573432020b70e8a14.jpg)  
FIGURE 10. Surface current analysis for router Ant.1. (a) 0.84 GHz. (b) 1 GHz. (c) 1.88 GHz. (d) 2.46 GHz. (e) 5.11 GHz. (f) 6.2 GHz. (g) 6.63 GHz. (h) 7.75 GHz. (i) 8.26 GHz. (j) 10.2 GHz. (k) 10.7 GHz.

![](images/1938cf7d4832d79b4eff0b8c4a6119f5dfad121b539c9715e29f700d272c0271.jpg)  
FIGURE 11. Surface current analysis for smartphone Ant.1. (a) 0.87 GHz. (b) 1 GHz. (c) 1.9 GHz. (d) 2.43 GHz. (e) 5.17 GHz. (f) 6.22 GHz. (g) 6.75 GHz. (h) 7.79 GHz. (i) 8.26 GHz. (j) 10.05 GHz. (k) 10.7 GHz.

![](images/24cc839a9c0b1438bf4d5f4c50c08d0e1cdbbfd09b2188ce5a38b8c517b18684.jpg)  
FIGURE 12. Simulated and measured reflection coefficients for (a) laptop Ant. 1, (b) laptop Ant. 2, (c) laptop Ant. 7, (d) router Ant. 1, and (e) smartphone Ant. 1.

![](images/beb5f825481934e1d480dea1f8f43e55e79a434c4b5ad6e981419b8e20897b0c.jpg)  
FIGURE 13. Simulated and measured isolation for (a) laptop, (b) router, and (c) smartphone.

of branch  $\mathbf{L}_2$ , generating a frequency of  $1\mathrm{GHz}$ . When the frequency is  $1.9\mathrm{GHz}$ , the current is mostly concentrated on the feeding antenna, as shown in Fig. 7(c). In Fig. 7(d), the current is distributed near the grounding and feeding points and the upper- left branch of the ground plane, producing a frequency of  $2.4\mathrm{GHz}$ . In Figs. 7(e)- (g), most of the current is concentrated on the small lower- left branch of the ground plane, achieving frequencies of 5.15, 6.25, and

![](images/918a25f0926d488ea1f04f77979559049cc88708bde3641a0b6d70b96248c710.jpg)  
FIGURE 14. Simulated and measured gain for (a) laptop Ant.1, (b) laptop Ant.2, (c) laptop Ant.3, (d) router Ant.1, and (e) smartphone Ant.1.

![](images/7d138c2c3badb56bd15e50aadac09f86d8ade6810d973124e72052b13c971dc9.jpg)  
FIGURE 15. Simulated and measured efficiency for (a) laptop Ant.1, (b) laptop Ant.2, (c) laptop Ant.7, (d) router Ant.1, and (e) smartphone Ant.1.

6.8 GHz through shorter branches. At 7.7 GHz, the current appears on branch  $\mathrm{L}_4$ , as shown in Fig. 7(h). In Figs. 7(i) and (j), the current is distributed between the grounding and feeding antennas, generating frequencies of 8.25 and 10.1 GHz. Finally, in Fig. 7(k), at 10.65 GHz, a significant current concentration is observed on branch  $\mathrm{L}_6$ .

![](images/788be837d7942123cba7285775fc9ef02bf3a463770ddda35c23d539811811af.jpg)  
FIGURE 16. Setup of the MIMO antenna system in the chamber. (a) laptop. (b) router. (c) smartphone.

From the surface current analysis above, when the antenna is configured for routers and smartphones, the results are similar to those of the laptop. This confirms that the proposed antenna maintains consistent current radiation and excellent frequency performance when deployed in electronic devices of varying sizes.

# III. ANALYSIS OF THE MULTI-BAND PLANAR ANTENNA SYSTEM

# A. S-PARAMETER ANALYSIS

The laptop, router, and smartphone discussed in this paper were analyzed using electromagnetic simulation software for S- parameters, gain, efficiency, ECC, and radiation patterns. All simulation results were compared with measurements for validation. Due to the symmetrical and mirrored design of the proposed multi- band planar antennas across devices, the analysis focuses only on a subset of antennas.

Fig. 12 presents the simulated and measured reflection coefficients of the multi- band planar MIMO antenna system applied to different electronic devices. Fig. 12(a) shows that both simulation and measurement results for Ant. 1 cover the 0.8- 1.04 GHz, 1.6- 2.71 GHz, and 4.69- 11.5 GHz frequency bands. In Figs. 12(b)- (c), the reflection coefficients of Ant. 2 and Ant. 7 show consistent trends with Ant. 1. Figs. 12(d) and (e) depict the simulated and measured reflection coefficients when the antennas are configured in the router and smartphone, respectively. In the relevant literature, the application frequency bands for laptops and smartphones are typically defined by a reflection coefficient below - 6 dB [1], [2], [13], while for routers, a reflection coefficient below - 10 dB is commonly used as the standard [9], [10]. The proposed multi- band antenna, when applied to routers, can achieve the same response frequency bands as other application devices under a reflection coefficient of less than - 6 dB. When the reflection coefficient is below - 10 dB, the antenna effectively satisfies the response frequency requirements of Wi- Fi 7. In this study, the three devices are regarded as portable, and a reflection coefficient of - 6 dB is therefore adopted as the standard. Fig. 12 demonstrates that the proposed multi- band planar antenna maintains a good reflection coefficient across all frequency bands when applied to devices of different sizes, thereby meeting the requirements for multiband applications.

In MIMO antenna systems, isolation is used to evaluate the extent of mutual influence between antennas. This study analyzes the spacing and positioning of antennas in devices of different sizes to ensure good isolation between them. Fig. 13 presents the simulated and measured isolation results for MIMO antenna systems in various devices. The isolation results for each device show values below - 10 dB, confirming that the proposed antenna maintains excellent stability and transmission performance across devices of different sizes.

# B. GAIN AND EFFICIENCY ANALYSIS

Figs. 14- 15 presents the gain and efficiency results of the multi- band planar MIMO antenna system in different devices. For Ant. 1, Ant. 2, and Ant. 7 in Figs. 14(a)- (c), the highest

![](images/ddc6f69a0c2a77ae6aca4fc0ce46944dd1cf1501e639500efdb3dde79809f8ed.jpg)  
FIGURE 17. 2D radiation pattern analysis of the antenna in a laptop for (a) 0.85 GHz, (b) 1 GHz, (c) 1.85 GHz, (d) 2.4 GHz, (e) 5.15 GHz, (f) 6.25 GHz, (g) 6.8 GHz, (h) 7.7 GHz, (i) 8.25 GHz, (j) 10.1 GHz, and (k) 10.65 GHz.

simulated gain is 1.91 dBi at 0.8- 1.04 GHz, with an efficiency of  $44\%$ . At 1.6- 2.71 GHz, the highest gain reaches 4.24 dBi, with an efficiency of  $82\%$ . Finally, at 4.69- 11.5 GHz, the gain peaks at 6.49 dBi, with an efficiency of  $81\%$ . The laptop antenna system exhibits consistent trends between the simulated and measured results.

Routers, smartphones, and laptops all use multi- band planar antennas with the same structure for MIMO configuration. Therefore, (d) and (e) in Fig. 14 and Fig. 15 show that the gain and efficiency measurement results of routers and smartphones have similar trends to the measurement results of notebook computers. The above results confirm that the antenna will not affect the transmission performance due to changes in device size.

# C. FAR-FIELD RADIATION PATTERN ANALYSIS

Fig. 16 illustrates the setup and measurement configuration of the MIMO antenna systems for three different devices in a standard far- field anechoic chamber. The three- axis (X, Y, Z) coordinates in the electromagnetic simulation software are aligned with the chamber's configuration to ensure accuracy between the simulation and actual measurements.

![](images/a4825a8656a8c6497feafd1ae5a53eb026b2390b734eafcce79f100d6abd0faf.jpg)  
FIGURE 18. 2D radiation pattern analysis of the antenna in a router for (a) 0.84 GHz, (b) 1 GHz, (c) 1.88 GHz, (d) 2.46 GHz, (e) 5.11 GHz, (f) 6.2 GHz, (g) 6.63 GHz, (h) 7.75 GHz, (i) 8.26 GHz, (j) 10.2 GHz, and (k) 10.7 GHz.

Fig. 17 presents the simulated and measured radiation patterns of Ant.1 for the laptop in the X,Y, XZ, and YZ planes. The analysis includes 11 antenna frequencies: 0.85, 1, 1.85, 2.4, 5.15, 6.25, 6.8, 7.7, 8.25, 10.1, and 10.65 GHz. Both the simulation and measurement results exhibit omnidirectional radiation trends. In the MIMO antenna radiation patterns of Ant.1 in the router and Ant.1 in the smartphone, as shown in Fig. 18 and 19, a radiation trend similar to that of the laptop antenna is also observed. This confirms that the proposed antenna possesses stable omnidirectional radiation characteristics, effectively preventing potential signal dead zones in devices.

# D. ENVELOPE CORRELATION COEFFICIENT ANALYSIS

The Envelope Correlation Coefficient (ECC) is an important metric for evaluating the degree of correlation between the radiation patterns of two MIMO antennas. Ideally, completely independent antennas will have an ECC value of zero. The ECC of MIMO antennas can be calculated using their S- parameters or far- field radiation patterns, as expressed in Equation (6) [37].

$$
ECC = \frac{\left|\int_0^{4\pi}\vec{E_1}\cdot\vec{E_2^*}d\Omega\right|^2}{\left(\int_0^{4\pi}\left|\vec{E_1}\right|^2d\Omega\right)\cdot\left(\int_0^{4\pi}\left|\vec{E_2}\right|^2d\Omega\right)} \tag{6}
$$

![](images/9f77ec721be1a4c186f2f812b5a410f3e0e78a7c1da59f71290ec3c50e2085b5.jpg)  
FIGURE 19. 2D radiation pattern analysis of the antenna in a smartphone for (a) 0.87 GHz, (b) 1 GHz, (c) 1.9 GHz, (d) 2.43 GHz, (e) 5.17 GHz, (f) 6.22 GHz, (g) 6.75 GHz, (h) 7.79 GHz, (i) 8.26 GHz, (j) 10.05 GHz, and (k) 10.7 GHz.

The ECC value, as indicated in recent literature, should be below 0.5 [37], [38]. Fig. 20 shows that the ECC for each device is consistently below the standard threshold of 0.5, with ECC values approaching zero at higher frequencies. These results confirm that the proposed multi- band planar MIMO antenna system demonstrates excellent independence across different devices.

# IV. ANALYSIS OF SPECIFIC ABSORPTION RATE (SAR) IMPACT ON THE HUMAN BODY

International regulations set clear limits on SAR values to protect user health [39]. The European Union specifies that

SAR values must not exceed  $2\mathrm{W / kg}$  (averaged over 10 grams of tissue), while the U.S. Federal Communications Commission (FCC) sets the limit at  $1.6\mathrm{W / kg}$  (averaged over 1 gram of tissue) [40]. In this study, Sim4Life simulation software was used to analyze the radiation impact of the Specific Absorption Rate (SAR) on users. Fig. 21 illustrates the placement of the smartphone multi- band planar MIMO antenna system on a human hand.

To evaluate the impact of the proposed MIMO antenna system on the human body during operation, simulations were conducted for the smartphone multi- band planar MIMO antenna system. The smartphone model was placed on an

![](images/59cc278a4a4f0a1150d06a28e5b228d9eab440edd9900d016bf7b1d136027e2b.jpg)  
FIGURE 20. Simulated and measured ECC of the multi-band planar MIMO antenna system. (a) Laptop Ant. 1-2. (b) Laptop Ant. 1-7. (c) Laptop Ant. 7-8. (d) Router Ant. 1-2. (e) Router Ant. 1-3. (f) Router Ant. 1-4. (g) Smartphone Ant. 1-2.

arm model and rendered invisible for clarity, as shown in Fig. 22 SAR values were assessed at  $0.88\mathrm{GHz}$ ,  $2.43\mathrm{GHz}$ , and  $5.1\mathrm{GHz}$ . Table 1 presents the simulated  $1\mathrm{g}$  SAR and  $10\mathrm{g}$  SAR results for Ant.1 of the smartphone. Both SAR values were significantly below the regulatory standards.

Fig. 23 illustrates the power density (PD) of the system's operation in high- frequency bands and its impact on human tissue. The U.S. Federal Communications Commission (FCC) sets specific regulations for PD exposure to ensure safety. For frequencies above  $6\mathrm{GHz}$ , the Maximum Permissible Exposure (MPE) limit for the general public is  $10\mathrm{W / m^2}$ , averaged over a  $4\mathrm{cm}^2$  area. For localized exposure, the limit is  $40\mathrm{W / m^2}$ , averaged over a  $1\mathrm{cm}^2$  area [40], [41]. Figs. 23(a) and 23(b) show the simulated PD results for  $1\mathrm{cm}^2$  and  $4\mathrm{cm}^2$  averaging scenarios, respectively. The results demonstrate that the proposed antenna design complies with international safety standards. These findings verify that the system's high- frequency operation has an impact on the human body well within permissible limits, ensuring user safety.

# V. COMPARISON WITH OTHER ANTENNAS

Table 3 compares the proposed multi- band planar MIMO antenna system with antennas from other studies. Compared to [9], the proposed antenna is more compact, covers a broader frequency range, and achieves higher efficiency in similar frequency bands. The antenna in [12] focuses on high- frequency bands and does not cover the low- frequency bands supported by the proposed antenna; within similar

![](images/dd0aa194d99c81d09656d746648c16587eeecef4121bb48d2a03390c7191a980.jpg)  
FIGURE 21. Illustration of the smartphone multi-band planar MIMO antenna system positioned on a human hand.

![](images/5a3675efbc7230f067b6b91784603f2843d0227a26dbd36382de51cc1030b9e7.jpg)  
FIGURE 22. SAR simulation results of the smartphone multi-band planar MIMO antenna system. (a) 0.88 GHz. (b) 2.43 GHz. (c) 5.1 GHz.

frequency ranges, the proposed antenna demonstrates superior isolation and gain. Compared to [13], the proposed antenna offers broader frequency coverage and shows significant advantages in isolation, efficiency, and gain. Similarly, compared to [21], the proposed antenna is more compact, supports a broader frequency range, and outperforms in isolation, efficiency, and gain within similar frequency bands.

Although [25] and [26] support multiple frequency bands, their high- frequency coverage is inferior to that of the proposed antenna, which extends up to  $11.5\mathrm{GHz}$ . Moreover, the proposed antenna is more compact and exhibits better isolation, efficiency, and gain within similar frequency ranges. The high- frequency coverage of [31] also falls short compared to the proposed antenna, and in similar frequency bands, the proposed antenna performs better in isolation and efficiency. Compared to the proposed antenna, [31] supports only a single frequency band and lacks the multi- band characteristics of the antenna presented in this paper. Furthermore, within similar frequency bands, the proposed antenna exhibits superior isolation and efficiency compared to [31].

![](images/c57fb7c91236a471106d8c22e5020154c7980ab3869378280986ce73bee5d7ca.jpg)  
FIGURE 23. PD simulation results of the smartphone multi-band planar MIMO antenna system. (a) 6.2 GHz. (b) 8.2 GHz.

TABLE 1. SAR Analysis Results for Smartphone Ant.1.  

<table><tr><td>Frequency(GHz)</td><td>1g SAR(W/kg)</td><td>10g SAR(W/kg)</td></tr><tr><td>0.88</td><td>0.041</td><td>0.0304</td></tr><tr><td>2.43</td><td>0.182</td><td>0.138</td></tr><tr><td>5.1</td><td>1.19</td><td>0.262</td></tr></table>

TABLE 2. PD analysis results for Smartphone Ant.1.  

<table><tr><td>Frequency(GHz)</td><td>1cm²(W/m²)</td><td>4cm²(W/m²)</td></tr><tr><td>6.2</td><td>1.83</td><td>1.19</td></tr><tr><td>8.2</td><td>1.62</td><td>0.693</td></tr></table>

The proposed multi- band planar MIMO antenna system not only supports a wide range of communication bands but also features a compact design, high isolation, high efficiency, excellent gain, and ease of integration

TABLE 3. Antenna comparison table.  

<table><tr><td>Ref.</td><td>Size (mm3)</td><td>Apply to</td><td>Operating Band (GHz)</td><td>Isolation (dB)</td><td>Efficiency (%)</td><td>Gain (dBi)</td><td>ECC</td></tr><tr><td rowspan="2">[9]</td><td rowspan="2">5.9×5.9×15.7</td><td rowspan="2">Router</td><td>2.36-2.65</td><td>-30</td><td>76</td><td>&amp;gt;8.2</td><td rowspan="2">&amp;lt;0.05</td></tr><tr><td>4.8-5.84</td><td>-15</td><td>61.6</td><td>&amp;gt;12.1</td></tr><tr><td>[12]</td><td>20×20×0.05</td><td>UWB</td><td>3.82-15.9</td><td>-17</td><td>&amp;gt;93(im)</td><td>6.33</td><td>&amp;lt;0.005</td></tr><tr><td rowspan="2">[13]</td><td rowspan="2">15×3×0.4</td><td rowspan="2">Laptop</td><td>3.4-3.8</td><td rowspan="2">-10</td><td rowspan="2">42</td><td rowspan="2">&amp;lt;6</td><td rowspan="2">&amp;lt;0.27</td></tr><tr><td>4.8-5</td></tr><tr><td rowspan="2">[21]</td><td rowspan="2">25.8×30×2</td><td rowspan="2">mobile</td><td>5.14-9.05</td><td rowspan="2">-12</td><td rowspan="2">43.6-85.1</td><td rowspan="2">3.9-8.6</td><td rowspan="2">&amp;lt;0.04</td></tr><tr><td>0.74-0.99</td></tr><tr><td rowspan="3">[25]</td><td rowspan="3">12.5×70×0.8</td><td rowspan="3">Laptop, Smartphone</td><td>1.38-2.64</td><td rowspan="3">-10</td><td rowspan="3">&amp;gt;43</td><td>4</td><td rowspan="3">0.5</td></tr><tr><td>4.3-4.7</td><td>2.59</td></tr><tr><td>4.8-6.58</td><td>3.65</td></tr><tr><td rowspan="3">[26]</td><td rowspan="3">12.5×60×0.8</td><td rowspan="3">Laptop, Tablets</td><td>0.82-1.1</td><td>-17</td><td>62</td><td>2.5</td><td rowspan="3">0.5</td></tr><tr><td>1.44-2.67</td><td>-18</td><td>80</td><td>4.4</td></tr><tr><td>4.27-7.82</td><td>-18</td><td>71</td><td>4.1</td></tr><tr><td rowspan="3">[31]</td><td rowspan="3">6×19×0.8</td><td rowspan="3">Smartphone</td><td>0.698-0.96</td><td rowspan="3">-10</td><td>18</td><td rowspan="3">-</td><td rowspan="3">0.5</td></tr><tr><td>1.71-2.7</td><td>32</td></tr><tr><td>3.3-4.4</td><td>25</td></tr><tr><td>[42]</td><td>12.42×13.35×0.8</td><td>Smartphone</td><td>3.29-6.61</td><td>16.6</td><td>&amp;gt;70</td><td>&amp;lt;4.53</td><td>&amp;lt;0.236</td></tr><tr><td rowspan="3">Proposed antenna</td><td rowspan="3">10×60×0.8</td><td rowspan="3">Laptop, Router, Smartphone</td><td>0.8-1.04</td><td>-10</td><td>48</td><td>1.91</td><td>0.4</td></tr><tr><td>1.6-2.71</td><td>-20</td><td>82</td><td>4.24</td><td>0.1</td></tr><tr><td>4.69-11.5</td><td>-30</td><td>81</td><td>6.49</td><td>0.02</td></tr></table>

into various devices, demonstrating substantial application potential.

# VI. CONCLUSION

This paper proposes a multi- band planar MIMO antenna system configured with identical multi- band planar antennas.

The proposed multiband planar antenna can be simultaneously configured on different devices to achieve frequency band coverage for LTE, 5G NR, Wi- Fi 7, and X- band applications. When applied to different devices, the antenna system consistently achieves an ECC below 0.5 and isolation below  $- 10\textrm{dB}$  , demonstrating excellent isolation and independence. Both simulation and measurement results indicate that the antenna system's performance remains unaffected by device size or placement configuration, maintaining stable gain and operational frequency bands. Additionally, an evaluation of the antenna's radiation impact on the human body was conducted, showing that both SAR and PD levels are below international standards. The overall results demonstrate that the proposed multiband planar MIMO system antenna exhibits high stability and integration flexibility, making it highly suitable for future versatile wireless communication devices.
