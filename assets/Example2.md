# Example 2: Confined Masonry Wall Capacities Calculation

## Description

Calculate the Axial Capacity, Pure Bending, Axial-Bending interaction curve, In Plane Shear capacities and the BackBone curve (Borah, Kaushik & Singhal, 2022) of a first-story confined Masonry wall of a two-story residency. This wall is located in Managua (a = 0.367g), and a Soil Amplification factor of 1.7 (Assuming type of soil D), per Managua City Seismic Resistant Code (NSM, 2021). The wall has a thickness of 15 cm, the wall total length (including vertical confined elements) is 3.00 m, its height 3.0 m, the columns and beams, width and height, is 15 cm both, the intermediate beam is located at the half of the wall's height. Consider f'm = 55 kg/cm2 based on net area, fy = 4200 kg/cm^2, f'c = 210 kg/cm^2. The reinforcement bars are 4#6 per each column. Use the Guidelines on Chapter 7 on Nicaraguan Masonry code (MP-001, 2017).

\[
\begin{aligned}
& \textrm{ \huge Solution:}\\[10pt]
& \textrm{ \LARGE Data:}\\[10pt]
& \textrm{ \textbf{1. Geometry Properties}}\\[10pt]
& \textrm{ 1.1. Wall Length}\\[10pt]
L &= 300 \; \;\textrm{([cm])}
\\[10pt]
& \textrm{ 1.2. Wall thickness}\\[10pt]
t &= 15 \; \;\textrm{([cm])}
\\[10pt]
& \textrm{ 1.3. Wall Height}\\[10pt]
H &= 300 \; \;\textrm{([cm])}
\\[10pt]
& \textrm{ 1.4. Confined Wall Elements width and height}\\[10pt]
\mathrm{wc} &= 15 \; \;\textrm{([cm])}
\\[10pt]
& \textrm{ 1.5. Moment of Inertia}\\[10pt]
I &= \frac{ 1 }{ 12 } \cdot L \cdot \left( t \right) ^{ 3 }  = \frac{ 1 }{ 12 } \cdot 300 \cdot \left( 15 \right) ^{ 3 } &= 84375.000 \; \;\textrm{($cm^4$)}
\\[10pt]
& \textrm{ 1.6. Gross Area - Net Area ratio}\\[10pt]
\mathrm{Por} &= \frac{ 48.75 }{ 93 } &= 0.524 \; \;\textrm{(-)}
\\[10pt]
& \textrm{ 1.7. Net Area}\\[10pt]
\mathrm{An} &= L \cdot t \cdot \mathrm{Por}  = 300 \cdot 15 \cdot 0.524 &= 2358.871 \; \;\textrm{($cm**2$)}
\\[10pt]
& \textrm{ 1.8. Radius of Gyration}\\[10pt]
r &= \mathrm{np.sqrt} { \left( \frac{ I }{ \mathrm{An} } \right) }  = np.sqrt { \left( \frac{ 84375.000 }{ 2358.871 } \right) } &= 5.981 \; \;\textrm{(cm)}
\\[10pt]
& \textrm{ 1.9. Center to Center distance between confinement Columns}\\[10pt]
d' &= L + \mathrm{wc}  = 300 + 15 &= 315 \; \;\textrm{(cm)}
\\[10pt]
& \textrm{ 1.10. Effective depth}\\[10pt]
d &= L + \mathrm{wc} + \frac{ \mathrm{wc} }{ 2 }  = 300 + 15 + \frac{ 15 }{ 2 } &= 322.500 \; \;\textrm{(cm)}
\\[10pt]
& \textrm{ \textbf{2. Material Properties}}\\[10pt]
& \textrm{ 2.1. Masonry compressive strength based on Net area}\\[10pt]
\mathrm{fm} &= 55 \; \;\textrm{($kg/cm**2$)}
\\[10pt]
& \textrm{ 2.2. Rebars steel Area}\\[10pt]
\mathrm{As} &= 4 \cdot \left( \frac{ 6 }{ 8 } \cdot 2.54 \right) ^{ 2 } \cdot \frac{ \mathrm{np.pi} }{ 4 }  = 4 \cdot \left( \frac{ 6 }{ 8 } \cdot 2.54 \right) ^{ 2 } \cdot \frac{ np.pi }{ 4 } &= 11.401 \; \;\textrm{([cm**2])}
\\[10pt]
& \textrm{ 2.3. Yielding Steel Stress}\\[10pt]
\mathrm{fy} &= 4200 \; \;\textrm{($kg/cm^2$)}
\\[10pt]
& \textrm{ 2.4. Compressive Stress of concrete}\\[10pt]
\mathrm{fc} &= 210 \; \;\textrm{($kg/cm^2$)}
\\[10pt]
& \textrm{ 2.5. Shear Stress}\\[10pt]
& \textrm{ \small \textit{Reference: Nicaraguan code, section 5.1.1.2 (MP001, 2017)}}\\[10pt]
v &= \mathrm{np.minimum} { \left( 0.8 \cdot \mathrm{np.sqrt} { \mathrm{fm} } ,\  6 \right) }  = np.minimum { \left( 0.8 \cdot np.sqrt { 55 } ,\  6 \right) } &= 5.933  
\\[10pt]
& \textrm{ \LARGE Calculations}\\[10pt]
& \textrm{ \textbf{1. Axial Capacity}}\\[10pt]
& \textrm{ \small \textit{Reference: Nicaraguan code, section 8.2. (MP001, 2017)}}\\[10pt]
\mathrm{Pn} &= 0.80 \cdot \left( 0.80 \cdot \mathrm{fm} \cdot \mathrm{An} + 2 \cdot \mathrm{As} \cdot \mathrm{fy} \right) \cdot \left( 1 - \left( \frac{ H }{ 140 \cdot r } \right) ^{ 2 } \right) \\&= 0.80 \cdot \left( 0.80 \cdot 55 \cdot 2358.871 + 2 \cdot 11.401 \cdot 4200 \right) \cdot \left( 1 - \left( \frac{ 300 }{ 140 \cdot 5.981 } \right) ^{ 2 } \right) \\&= 139151.989 \; \;\textrm{(kg)}\\[10pt]
\\[10pt]
& \textrm{ \textbf{2. Pure Bending Capacity}}\\[10pt]
& \textrm{ \small \textit{Reference: Nicaraguan code, section 8.3. (MP001, 2017)}}\\[10pt]
\mathrm{Mn} &= 0.9 \cdot \mathrm{As} \cdot \mathrm{fy} \cdot \frac{ d' }{ 100 }  = 0.9 \cdot 11.401 \cdot 4200 \cdot \frac{ 315 }{ 100 } &= 135750.734 \; \;\textrm{(kg-m)}
\\[10pt]
& \textrm{ \textbf{3. Axial - Bending points of interaction curve}}\\[10pt]
& \textrm{ \small \textit{Reference: Nicaraguan code, section 8.3. (MP001, 2017)}}\\[10pt]
& \textrm{ Considering Pu as 35\% of the Axial Capacity}\\[10pt]
\mathrm{Pu} &= 0.35 \cdot \mathrm{Pn}  = 0.35 \cdot 139151.989 &= 20872.798 \; \;\textrm{(kg)}
\\[10pt]
\mathrm{M2} &= \left( 1.5 \cdot \mathrm{Mn} + 0.15 \cdot \mathrm{Pn} \cdot \frac{ d }{ 100 } \right) \cdot \left( 1 - \frac{ \mathrm{Pu} }{ \mathrm{Pn} } \right) \\&= \left( 1.5 \cdot 135750.734 + 0.15 \cdot 139151.989 \cdot \frac{ 322.500 }{ 100 } \right) \cdot \left( 1 - \frac{ 20872.798 }{ 139151.989 } \right) \\&= 176111.569 \; \;\textrm{(kg-m)}\\[10pt]
\\[10pt]
\mathrm{M3} &= 182871.076 \; \;\textrm{(kg-m)}
\\[10pt]
& \textrm{ \textbf{3. In Plane Shear Capacity}}\\[10pt]
& \textrm{ \small \textit{Reference: Nicaraguan code, section 8.6. (MP001, 2017)}}\\[10pt]
& \textrm{ Considering Pu as 15\% of the Axial Capacity conservatively}\\[10pt]
\mathrm{Pu} &= 0.15 \cdot \mathrm{Pn}  = 0.15 \cdot 139151.989 &= 20872.798 \; \;\textrm{(kg)}
\\[10pt]
A &= \left( L + 2 \cdot \mathrm{wc} \right) \cdot t  = \left( 300 + 2 \cdot 15 \right) \cdot 15 &= 4950 \; \;\textrm{($cm^2$)}
\\[10pt]
\mathrm{v1} &= v \cdot \frac{ \mathrm{An} }{ A }  = 5.933 \cdot \frac{ 2358.871 }{ 4950 } &= 2.827 \; \;\textrm{($kg/cm^2$)}
\\[10pt]
V &= \mathrm{np.minimum} { \left( 0.8 \cdot \left( 0.5 \cdot \mathrm{v1} \cdot A + 0.3 \cdot \mathrm{Pu} \right) ,\  1.05 \cdot v \cdot A \right) } \\&= np.minimum { \left( 0.8 \cdot \left( 0.5 \cdot 2.827 \cdot 4950 + 0.3 \cdot 20872.798 \right) ,\  1.05 \cdot 5.933 \cdot 4950 \right) } \\&= 10607.505 \; \;\textrm{(kg)}\\[10pt]
\\[10pt]
& \textrm{ \textbf{4. Trilinear BackBone curve}}\\[10pt]
& \textrm{ \small \textit{Reference: Lateral Load Deformation Models for seismic Analysis}}\\[10pt]
& \textrm{ \small \textit{and Performance based Design of Confined Masonry Walls (Borah, Kaushik and Singhal, 2012)}}\\[10pt]
& \textrm{ 4.1. Aspect Ratio}\\[10pt]
\mathrm{AR} &= \frac{ H }{ L }  = \frac{ 300 }{ 300 } &= 1.000 \; \;\textrm{(-)}
\\[10pt]
& \textrm{ 4.2. Area of Confined Elements}\\[10pt]
\mathrm{Ac} &= \left( \mathrm{wc} \right) ^{ 2 }  = \left( 15 \right) ^{ 2 } &= 225 \; \;\textrm{($cm^2$)}
\\[10pt]
& \textrm{ 4.3. Number of Confined Elements}\\[10pt]
n &= 2 \; \;\textrm{(-)}
\\[10pt]
& \textrm{ 4.4. Axial stress based on gross area}\\[10pt]
\sigma &= \frac{ \mathrm{Pu} }{ A }  = \frac{ 20872.798 }{ 4950 } &= 4.217 \; \;\textrm{($kg/cm^2$)}
\\[10pt]
& \textrm{ 4.5. Masonry compression stress based on gross area}\\[10pt]
\mathrm{fm}_{gross} &= \mathrm{fm} \cdot \frac{ \mathrm{An} }{ A }  = 55 \cdot \frac{ 2358.871 }{ 4950 } &= 26.210 \; \;\textrm{($kg/cm^2$)}
\\[10pt]
& \textrm{ 4.6. Maximum Shear Resistant of the wall}\\[10pt]
\mathrm{Vm} &= \left( \frac{ \left( \mathrm{fm}_{gross} \right) ^{ 0.4 } \cdot \left( n \cdot \frac{ \mathrm{Ac} }{ A } \right) ^{ 0.9 } }{ \left( \mathrm{AR} \right) ^{ 0.7 } } \right) \cdot \left( 1 + \sigma \right) \cdot A \\&= \left( \frac{ \left( 26.210 \right) ^{ 0.4 } \cdot \left( 2 \cdot \frac{ 225 }{ 4950 } \right) ^{ 0.9 } }{ \left( 1.000 \right) ^{ 0.7 } } \right) \cdot \left( 1 + 4.217 \right) \cdot 4950 \\&= 11018.807 \; \;\textrm{(kg)}\\[10pt]
\\[10pt]
& \textrm{ 4.7. Cracking Shear Resistant of the wall}\\[10pt]
\mathrm{Vcr} &= 0.7 \cdot \mathrm{Vm}  = 0.7 \cdot 11018.807 &= 7713.165 \; \;\textrm{(kg)}
\\[10pt]
& \textrm{ 4.8. Ultimate Shear Resistant of the wall}\\[10pt]
\mathrm{Vu} &= 0.8 \cdot \mathrm{Vm}  = 0.8 \cdot 11018.807 &= 8815.045 \; \;\textrm{(kg)}
\\[10pt]
& \textrm{ 4.9. Cracking Drift of the wall}\\[10pt]
\mathrm{Driftcr} &= \left( \mathrm{AR} \right) ^{ -4.1 } \cdot \left( \mathrm{fm}_{gross} \right) ^{ -1.5 }  = \left( 1.000 \right) ^{ -4.1 } \cdot \left( 26.210 \right) ^{ -1.5 } &= 0.007 \; \;\textrm{(-)}
\\[10pt]
& \textrm{ 4.10. Drift at Maximum Shear Resistant of the wall}\\[10pt]
\mathrm{Driftm} &= 3.7 \cdot \mathrm{AR} \cdot \mathrm{Driftcr}  = 3.7 \cdot 1.000 \cdot 0.007 &= 0.028 \; \;\textrm{(-)}
\\[10pt]
& \textrm{ 4.11. Drift at ultimate stage of the wall}\\[10pt]
\mathrm{Driftu} &= 1.8 \cdot \mathrm{Driftm}  = 1.8 \cdot 0.028 &= 0.050 \; \;\textrm{(-)}
\end{aligned}
\]