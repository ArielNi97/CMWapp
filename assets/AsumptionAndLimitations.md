## Overview

- This app is intended to be used by Structural Engineers, contractors, or architects.
- It only calculates the Confined Masonry Walls capacities. Other type of similar walls, such as reinforced Masonry Walls, Unreinforced Masonry Walls, or masonry infill walls are out of the scope of this app.
- The Axial-Bending, Pure bending, Combined axial-bending and Back Bone curve are obtained by a Machine Learning model trained and validated with more than 3 Million walls varying its geometrical and material properties complying with the Nicaragua MP-001 standard and the trilinear Shear-drift curves were calculated based on the research made by borah, Singhal, 2022, “Add the name of the paper”.
- Several Machine Learning Models were perfomed (Decision Trees, Random Forest,XG boost, Adaptive Boosting, KN-Neighbors, Light gradient boosting, categorical boosting), however the chosen one to predict the capacities, was categorical boosting since it was the more accurate among them all.
- Out of plane wall capacities are calculated via python scripts and based in Peruvian code (E070, 2019).
- The data base was made combining different parameters of walls, such as: Wall Length, Wall Height, Wall thickness, column width, number and type of rebars,  Masonry compressive strength, Concrete compressive strength, Steel yielding strength.
- The interface of this app is made using streamlit.
- The deployment was made with render.io.
- The user inputs are limited to Project Location, Wall Loads, Walls Geometry, Walls Material and Walls Boundary Conditions.
- The outputs are limited to the information displayed in the Analysis Tab.

## Inputs

### Project Location

- The Project location information is used to calculate the out of plane capacities and demands of the walls.
- The location is only limited to the main cities of Nicaragua, other than that are not available for the user.
- The Soil Amplification Factor and Accelerations depends totally on the location, specific accelerations or Soil Amplification factors are not included in the user interface.
- The importance factor available are based on Nicaragua code NSM-21, other than that are not available for the user.
  
### Walls Material

- In material properties the user only can define the compressive masonry strength, concrete compressive strength, steel yielding strength and upload a bar type file.
- A range from 45 to 55 kg/cm2 can be selected for compressive masonry strength.
- Only two types of compressive concrete strength can be selected, 210 and 245 kg/cm2.
- Same as above, only two types of steel yielding strength can be selected 2800 and 4200 kg/cm2.
- The input of bar types is set by 2 columns, the first one must have a column called literally Wall Label, and the user has the freedom two use any identifier for the walls. For instance, the Wall Label that the author propose is using Wn, where W means Wall and n varies in an ascendant order, starting from 0 to the total number of walls. For instance, W1, W2, W3…Wn. In case of the second column, it must be named “Rebars” literally, the user can add the quantity and type of bars (Q#T) where Q is the quantity of bars and T is the type of bars, for instance the user can specify a 4#4 arrangement, or a 12#6 arrangement.
- The columns names must not be changed by the user for the Rebars input uploaded to the app.
- The user must respect the format of the rebars arrangement, other style must be avoided. For instance, 12N°4 is unacceptable.
- The user can only choose between #3 to #8 bars, and a combination of arrangements that makes no more than 40 cm2. Arrangements with higher arrangement may give unprecise results.
- The number of rows in the input rebars file need to be consistent with the number of rows and columns. The user always needs to make sure that every row is filled with desire values.
- Unexperienced user should download the available template file that will help to build the final input rebars file.
- The Rebars are read by the algorithms per each column. 
- Masonry units are based only in concrete units, other materials like clay bricks or Local Stones are not part of the scope of this app.

### Walls Geometry

- The options for walls geometry input are the length of the wall, the height of the wall, the thickness and the confined element dimensions.
- The user should download the input template file available to get familiarized with the content.
- As all the input files, the user can only edit the rows of the files but not the headers of the columns.
- The level means the story that the wall belongs to, please start always with 1. If it’s a multistory Masonry Building, always use the levels in integer format and also in an ascendant order.
- The available heights of the masonry walls are in a range from 2.50 to 4 meters, other heights may give unprecise results.
- The available thicknesses are 0.10,0.15,0.20 meters, other thicknesses may give bad results.
- The wall lengths are set to be minimum 1.2 meters to 3.0 meters. Different Walls lengths may give wrong outputs.
- All confined reinforce concrete elements must have squared sections, rectangular sections may lead towards wrong output.
- Beams and Columns widths and heights are limited to 0.10-0.40m, beyond those ranges may give poor results.
- 
### Walls Boundary Conditions

- The user is free to choose whether the wall is restrained in all directions or if it’s released in the top side but restricted in all the other three sides. Hence, only two options are available for now. The value 1 for Case 1 and 2 for case 2 need to be chosen.

### Walls Loading

- The user should download the template file first to be familiar with the input file of the loading.
- Axial, in plane shear, In plane moment and out of plane moment are required to build the input files.
- The column header must not be changed and must remain the same as the input template file. 
- The out of plane moment is not used for internal calculations in this version, it will be for future version. For that reason, currently the output won’t be changed if this value is changed in the input file.


## Internal Calculations (For User Reference)

Our app employs a combination of advanced techniques to accurately calculate various wall capacities and demands. Here's a brief overview of the methods and considerations involved:

### Machine Learning-Powered Capacities
- We utilize a powerful Categorical Boosting Machine Learning model to calculate capacities for Axial, Pure Bending, Combined Axial-Bending, In-Plane Shear, and Back Bone curve. This model has been trained on an extensive dataset comprising over 3 million walls. Initially, Python scripts were used to calculate axial capacities, which served as the foundational data for the machine learning model. The model's ability to predict axial capacities was fine-tuned through learning from this extensive dataset.

### Internal Algorithms for Out-of-Plane (OOP) Stress Capacities
- In contrast, OOP stress capacities are computed using internal algorithms. Machine Learning models were not applied in this case due to the need for a more substantial database and the complexity involved in training such a model with our current computational resources.

### Compliance with Masonry Codes
- Our calculations strictly adhere to the standards set forth by the Nicaraguan Masonry Code (MP-001, 2017) for various capacities. These include:
  - Axial capacities in compliance with Section 8.2.
  - Pure Bending Capacities following Section 8.3.
  - Axial-Bending Capacities computed according to Section 8.4.
  - In-Plane Shear Capacities calculated in accordance with Section 8.6.

### Out-of-Plane Shear Capacities
- For Out of Plane Shear Capacities, we refer to the Peruvian Masonry Code (E-070, 2019), specifically Chapter 19. It's important to note that we introduce a limit value of 0.8 of fr (as set in MP-001, Table 5.1) into our calculations to ensure safety.

### Demands and Additional Considerations
- Our app also computes demands:
  - To determine the Axial-Bending Capacity, we use 35% of Pn as the Axial Demand.
  - In calculating the Axial Capacity, we exclude the contribution of the intermediate confined beam. Therefore, the 'h' in equation 8.1 (as defined in MP-001) is equal to the Height of the wall.
  - For In-Plane Shear Capacity, we utilize a conservative approach, setting it at 15% of the Axial Capacity, acknowledging that higher axial demand leads to greater shear capacity.
  - We normalize the Shear Vm in equation 8.5 based on gross area, even though the input f'm is based on net area. This normalization process is a crucial aspect considered internally across our scripts.

### Future Enhancements
- It's worth noting that our app does not currently consider multi-pier walls, but this feature is slated for inclusion in future versions as we continue to improve and expand the capabilities of our application.
