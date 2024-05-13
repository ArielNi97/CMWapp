# Example 4: Out of Plane confined Masonry Wall Capacity

## Description

Calculate the out of plane capacity and demand stresses of a Second-story confined Masonry wall of a two-story residency which has all the borders restrained. This wall is located in Managua (a = 0.367g), and a Soil Amplification factor of 1.7 (Assuming type of soil D), per Managua City Seismic Resistant Code (NSM, 2021). The wall has a thickness of 15 cm, the wall total length (including vertical confined elements) is 3 m, its height 3 m, the columns and beams, width and height, is 15 cm both, the intermediate beam is located at the half of the wall's height. After a Seismic and Gravity Analysis of the building, the wall results in having an axial load of 3500 kg (Assume an eccentricity of 10% of the thickness of the wall) and the shear load is 1000kg. Consider f'm = 55 kg/cm2 based on net area and that the total base shear and gravity reaction of the building is ten times the loads of this wall. Use the Guidelines on chapter 19 (E070,2019) to do the stress check.


\[
\begin{aligned}
& \textrm{ \huge Solution:}\\[10pt]
& \textrm{ \LARGE Data:}\\[10pt]
& \textrm{ \textbf{1. Seismic Hazard}}\\[10pt]
& \textrm{ 1.1. PGA}\\[10pt]
\mathrm{ac} &= 0.367 \; \;\textrm{(g)}
\\[10pt]
& \textrm{ 1.2. Soil Amplification Factor}\\[10pt]
\mathrm{Fs} &= 1.700 \; 
\\[10pt]
& \textrm{ 1.3. Importance Factor}\\[10pt]
I &= 1 \; 
\\[10pt]
& \textrm{ \textbf{2. Geometry Properties}}\\[10pt]
& \textrm{ 2.1. Wall Length}\\[10pt]
L &= 3.000 \; \;\textrm{(m)}
\\[10pt]
& \textrm{ 2.2. Wall thickness}\\[10pt]
t &= 0.150 \; \;\textrm{(m)}
\\[10pt]
& \textrm{ 2.3. Wall Height}\\[10pt]
H &= 3.000 \; \;\textrm{(m)}
\\[10pt]
& \textrm{ 2.4. Confined Wall Elements width and height}\\[10pt]
\mathrm{wc} &= 0.150 \; \;\textrm{(m)}
\\[10pt]
& \textrm{ 2.5. Panel length}\\[10pt]
\mathrm{Lw} &= L - \mathrm{wc} \cdot 2  = 3.000 - 0.150 \cdot 2 &= 2.700 \; \;\textrm{(m)}
\\[10pt]
& \textrm{ 2.6. Panel height}\\[10pt]
\mathrm{Hw} &= \frac{ H - \mathrm{wc} - \mathrm{wc} }{ 2 }  = \frac{ 3.000 - 0.150 - 0.150 }{ 2 } &= 1.350 \; \;\textrm{(m)}
\\[10pt]
& \textrm{ \textbf{3. Material Properties}}\\[10pt]
& \textrm{ 3.1. Masonry compressive strength based on Net area}\\[10pt]
f_{mn} &= 55 \; \;\textrm{($kg/cm^2$)}
\\[10pt]
& \textrm{ 3.2. Relationship ratio between Gross Area and Net Area.}\\[10pt]
\mathrm{factor} &= \frac{ 48.75 }{ 93 } &= 0.524 \; \;\textrm{(-)}
\\[10pt]
& \textrm{ \textbf{4. Loads}}\\[10pt]
& \textrm{ 4.1. Wall Panel weight}\\[10pt]
\mathrm{Pe} &= 1800 \cdot t \cdot \mathrm{factor}  = 1800 \cdot 0.150 \cdot 0.524 &= 141.532 \; \;\textrm{($kg/m^2$)}
\\[10pt]
& \textrm{ 4.2. Axial Load on Walls}\\[10pt]
P &= 3500 \; \;\textrm{(kg)}
\\[10pt]
& \textrm{ 4.3. Shear Load on Walls}\\[10pt]
V &= 1000 \; \;\textrm{(kg)}
\\[10pt]
& \textrm{ 4.4. Sum of Axial loads per story}\\[10pt]
\mathrm{Sum}_{P} &= P \cdot 10  = 3500 \cdot 10 &= 35000 \; \;\textrm{(kg)}
\\[10pt]
& \textrm{ 4.5. Sum of Shear loads per story}\\[10pt]
\mathrm{Sum}_{V} &= V \cdot 10  = 1000 \cdot 10 &= 10000 \; \;\textrm{(kg)}
\\[10pt]
& \textrm{ \textbf{5. Boundary Conditions}}\\[10pt]
& \textrm{  5.1. Wall with all borders restrained}\\[10pt]
& \textrm{ \small \textit{Reference: Peruvian code, chapter 19, table 13 (E070, 2019)}}\\[10pt]
\mathrm{Case} &= 1 \; \;\textrm{(-)}
\\[10pt]
& \textrm{ \LARGE Calculations}\\[10pt]
& \textrm{ \textbf{1. Geometric parameters and adimensional moment coefficient}}\\[10pt]
& \textrm{ \small \textit{Reference: Peruvian code, chapter 19, table 13 (E070, 2019)}}\\[10pt]
a &= \mathrm{np.minimum} { \left( \mathrm{Lw} ,\  \mathrm{Hw} \right) }  = np.minimum { \left( 2.700 ,\  1.350 \right) } &= 1.350 \; \;\textrm{(m)}
\\[10pt]
b &= \mathrm{np.maximum} { \left( \mathrm{Lw} ,\  \mathrm{Hw} \right) }  = np.maximum { \left( 2.700 ,\  1.350 \right) } &= 2.700 \; \;\textrm{(m)}
\\[10pt]
m &= 0.102 \; \;\textrm{(-)}
\\[10pt]
& \textrm{ 1.1. Axial Load Eccentricity (Assuming 10 \% of thickness)}\\[10pt]
e &= 0.10 \cdot t  = 0.10 \cdot 0.150 &= 0.015 \; \;\textrm{(m)}
\\[10pt]
& \textrm{ \textbf{2. Hazard transformation from Nicaraguan Hazard to Peruvian Hazard}}\\[10pt]
Z &= 0.367 \; \;\textrm{(g)}
\\[10pt]
U &= 1 \; \;\textrm{(-)}
\\[10pt]
S &= 1.700 \; \;\textrm{(-)}
\\[10pt]
& \textrm{ \textbf{3. Demands}}\\[10pt]
& \textrm{ 3.1. Out of plane stress}\\[10pt]
& \textrm{ \small \textit{Reference: Peruvian code, chapter 19, article 68 (E070, 2019)}}\\[10pt]
\mathrm{C1} &= 2 \; 
\\[10pt]
w &= 0.3 \cdot \frac{ \mathrm{Sum}_{V} }{ \mathrm{Sum}_{P} } \cdot \mathrm{C1} \cdot \mathrm{Pe}  = 0.3 \cdot \frac{ 10000 }{ 35000 } \cdot 2 \cdot 141.532 &= 24.263 \; \;\textrm{($kg/m^2$)}
\\[10pt]
& \textrm{ 3.2. Out of plane moment}\\[10pt]
& \textrm{ \small \textit{Reference: Peruvian code, chapter 19, article 68 (E070, 2019)}}\\[10pt]
\mathrm{Ms} &= m \cdot w \cdot \left( a \right) ^{ 2 }  = 0.102 \cdot 24.263 \cdot \left( 1.350 \right) ^{ 2 } &= 4.497 \; \;\textrm{($kg-m/m$)}
\\[10pt]
& \textrm{ 3.3. Moment due to gravity load eccentricity}\\[10pt]
& \textrm{ \small \textit{Reference: Peruvian code, chapter 19, article 69.1 (E070, 2019)}}\\[10pt]
\mathrm{Mg} &= P \cdot e  = 3500 \cdot 0.015 &= 52.500 \; \;\textrm{($kg-m/m$)}
\\[10pt]
& \textrm{ 3.4. Total Design Moment}\\[10pt]
& \textrm{ \small \textit{Reference: Peruvian code, chapter 19, article 69.1 (E070, 2019)}}\\[10pt]
\mathrm{Mt} &= \mathrm{Ms} + \mathrm{Mg}  = 4.497 + 52.500 &= 56.997 \; \;\textrm{($kg-m/m$)}
\\[10pt]
& \textrm{ 3.5. Maximum stress}\\[10pt]
& \textrm{ 3.5.1. Gravity load per unit length}\\[10pt]
& \textrm{ \small \textit{Reference: Peruvian code, chapter 19, article 69.2 (E070, 2019)}}\\[10pt]
\mathrm{fa} &= \frac{ P }{ t }  = \frac{ 3500 }{ 0.150 } &= 23333.333 \; \;\textrm{($kg/m^2$)}
\\[10pt]
& \textrm{ 3.5.2. Stress due to Mt}\\[10pt]
& \textrm{ \small \textit{Reference: Peruvian code, chapter 19, article 69.2 (E070, 2019)}}\\[10pt]
\mathrm{fm} &= 6 \cdot \frac{ \mathrm{Mt} }{ \left( t \right) ^{ 2 } }  = 6 \cdot \frac{ 56.997 }{ \left( 0.150 \right) ^{ 2 } } &= 15199.212 \; \;\textrm{($kg/m^2$)}
\\[10pt]
& \textrm{ 3.5.3. Stress capacities}\\[10pt]
& \textrm{ \small \textit{Reference: Peruvian code, chapter 19, article 69.3 (E070, 2019)}}\\[10pt]
f_{mg} &= \mathrm{factor} \cdot f_{mn} \cdot 10000  = 0.524 \cdot 55 \cdot 10000 &= 288306.452 \; \;\textrm{($kg/m^2$)}
\\[10pt]
\mathrm{Fa} &= 0.20 \cdot f_{mg} \cdot \left( 1 - \left( \frac{ H }{ 35 \cdot t } \right) ^{ 2 } \right)  = 0.20 \cdot 288306.452 \cdot \left( 1 - \left( \frac{ 3.000 }{ 35 \cdot 0.150 } \right) ^{ 2 } \right) &= 38833.114 \; \;\textrm{($kg/m^2$)}
\\[10pt]
\mathrm{Fm} &= 0.4 \cdot f_{mg}  = 0.4 \cdot 288306.452 &= 115322.581 \; \;\textrm{($kg/m^2$)}
\\[10pt]
& \textrm{ \small \textit{Reference: out of plane stress limit Per table 5.1 (MP-001)}}\\[10pt]
f_{t} &= 0.8 \cdot 3 \cdot 10000 &= 24000.000 \; \;\textrm{($kg/m^2$)}
\end{aligned}
\]


\[
\begin{aligned}
& \textrm{ 4. Stress check}\\[10pt]
& \textrm{ \small \textit{Reference: Peruvian code, chapter 19, article 69.3 (E070, 2019)}}\end{aligned}
\]



\[
\begin{aligned}
&\text{Since, } \mathrm{fm} - \mathrm{fa} \lt f_{t} \rightarrow \left( 15199.212 - 23333.333 \lt 24000.000 \right) : \; \;\textrm{($kg/m^2$)} \\[10pt]
\mathrm{Check} &= \mathrm{Ok, -8134.12 < 24000.000000000004} \; 
\end{aligned}
\]


\[
\begin{aligned}
&\text{Since, } \frac{ \mathrm{fm} }{ \mathrm{Fm} } + \frac{ \mathrm{fa} }{ \mathrm{Fa} } \leq 1.33 \rightarrow \left( \frac{ 15199.212 }{ 115322.581 } + \frac{ 23333.333 }{ 38833.114 } \leq 1.33 \right) :   \\[10pt]
\mathrm{Check} &= \mathrm{Ok, 0.73 < 1.33 } \; 
\end{aligned}
\]
