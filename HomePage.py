from pathlib import Path
import pandas as pd
import streamlit as st
from PIL import Image

# --- Path Settings ---

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd() #cwd stands for current working directory

css_file = current_dir / "styles" / "main.css"



# --- GENERAL SETTINGS ---

PAGE_TITLE = "CMW JACH app"
PAGE_ICON = "🧱"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

hide_footer_style = """
    <style>
    footer{ 
        visibility:visible; 
    }
    footer:after{
        content:'Author: J. Ariel Chavarria H. Version: 1.0.0.';
        display:block;
        position:relative;
    }
    </style>  
    """
st.markdown(hide_footer_style, unsafe_allow_html = True)

# st.title("CMW JACH Web App")
st.sidebar.success("Please select a Page above. If it's first time using the app, start from the top to the bottom")
# st.sidebar.divider()
# st.sidebar.snow()

st.markdown("""
            
            ## Welcome to the Confined Masonry Wall Capacity Predictor!

🏗️ Are you involved in construction or engineering? Do you want to ensure the safety and efficiency 
of confined masonry walls in your projects? 
You've come to the **right place!**

### What We Do:

👌🏼 At Confined Masonry Wall Capacity Predictor, we've harnessed the power of Machine Learning 
(ML) algorithms to revolutionize the way you assess the structural integrity of masonry walls.
Our cutting-edge web application empowers you to calculate critical parameters for your walls 
with ease and precision.

### Key Features:

✅ Axial Load Capacity Prediction: Determine the axial load-carrying capacity of your 
confined masonry walls accurately.

✅ Bending Capacity Calculation: Get insights into the bending capacity of your walls, 
aiding in structural design decisions.

✅ Combined Axial-Bending Capacity: Assess how your walls perform under combined axial 
and bending loads for comprehensive analysis.

✅ In-Plane Shear Capacity: Obtain the capacity of the walls to withstand in-plane shear demands.

✅ Out of Plane Stress Capacity: Analyze the capacity of your walls to withstand out-of-plane 
stress for enhanced safety.

✅ Backbone Curve Visualization: Visualize the backbone curve (Bora & Kaushik et al., 2022),
enabling you to make informed structural choices.

### User-Friendly Interface:

👷🏼 Our user-friendly interface simplifies the process. Upload a series of walls with a csv file 
inside the **Walls Geometry** and **Walls Loading** ribbons shown on the 
left side of the screen, select the properties of such walls in **Project Location**, **Walls Material** 
and **Walls Boundary Condition** tabs, and effortlessly explore the results in **Wall Analysis** page. 
Our ML algorithms will then provide you with accurate and reliable capacity predictions.

### Why Choose Us:

📈 Accuracy: Trust in precise calculations powered by state-of-the-art ML algorithms.

🚀 Efficiency: Save time and resources with our streamlined assessment process.

👽 Versatility: Analyze multiple walls, compare results, and make informed decisions.

🆙 User-Centric: We've designed our application with you in mind, ensuring a seamless experience.

### Join Us in Shaping the Future of Construction:

⚡ Whether you're an engineer, architect, or builder, our Confined Masonry Wall Capacity Predictor
will be your indispensable companion. Empower your projects with data-driven decisions and 
unparalleled insights.

### Get Started Today:

🔥 Don't wait! Start exploring the capabilities of your confined masonry walls right now. 
Upload your walls, harness the power of ML, and pave the way for safer and more efficient
construction.

💥 Let's Build Together - Start Your Journey!

### Get in Touch!

❣️ Reach out to us and let us know your feedback: 


""")

SOCIAL_MEDIA = {
    "**LinkedIn**": "https://www.linkedin.com/in/ariel-chavarria-63514823a",
    "**Gitlab**" : "https://gitlab.com/jachavarria",
    }

# st.subheader("Social media")
    
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")
        
        
# # NAME = "J. Ariel Chavarria H."
# # DESCRIPTION = """

# #    Experienced and proactive Structural Civil Engineer with over 4 years of 
# #    expertise in conducting structural calculations for steel, wood, masonry, 
# #    and concrete materials. Highly skilled in designing a wide range of structures, 
# #    including buried, drainage, retention, and prestressed concrete structures, 
# #    multi-story steel/concrete/wood/masonry buildings, elevated water storage tanks, 
# #    as well as pedestrian and vehicular bridges. Proficient in programming and modeling 
# #    structures for seismic analysis. Strong organizational abilities and a dedication 
# #    to delivering high-quality results.

# # """

# # EMAIL = "jose_ariel_chavarria@hotmail.com"
# # SOCIAL_MEDIA = {
# #     "**LinkedIn**": "https://www.linkedin.com/in/ariel-chavarria-63514823a",
# #     "**Gitlab**" : "https://gitlab.com/jachavarria",
# #     }


# # st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# # # --- LOAD CSS, PDF & PROFILE PIC ---

# # with open(css_file) as f:
# #     st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html = True)
    
# # with open(resume_file, "rb") as pdf_file:
# #     PDFbyte = pdf_file.read()
# #     profile_pic = Image.open(profile_pic)
    
    
    
    
# # # --- HERO SECTION ---

# # col1, col2 = st.columns(2, gap = "small")
# # with col1:
    
# #     st.image(profile_pic, width = 275)
    
    
    
    
  
    
# #      # --- References  ---
    
# #     st.write("#")
# #     st.subheader("References")
# #     st.write(
# #     """
# #     - 👷‍♂️ **Carlos Zepeda**
# #     - Principal Structural Engineer
# #     - 📱 Cellphone: 
# #     - +505 81289109
# #     ---
# #     - 👷‍♀️ **Maria Rivas** 
# #     - Sr. Structural Engineer
# #     - 📱Cellphone: 
# #     - +505 86886240
# #     ---
# #     - 👷‍♂️ **Juan Aleman**
# #     - PhD Principal Structural Engineer | TangoBuilder's Co-founder
# #     - 📧 email: 
# #     - jbaleman@gmail.com
# #     ---
# #     """
    
# #     )  
    
# #     # --- SOCIAL LINKS ---
# #     st.write("#")
# #     st.subheader("Social media")
    
# #     cols = st.columns(len(SOCIAL_MEDIA))
# #     for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
# #         cols[index].write(f"[{platform}]({link})") 
    
# # with col2:
    
# #     st.title(NAME)
# #     st.subheader("About me")
# #     st.write(DESCRIPTION)
# #     st.download_button(
# #         label = "📃 Download Resume",
# #         data = PDFbyte,
# #         file_name = resume_file.name,
# #         mime = "application/octet-stream",
        
# #     )        
    
# #      # --- CONTACT INFO ---
    
# #     st.write("#")
# #     st.subheader("Contact Information")
# #     st.write(
# #     f"""
# #     - **📱Cellphone:** 
# #     - +50584082774
# #     - **📬e-mail:** 
# #     - {EMAIL}
# #     - **📍Location:**
# #     - Veracruz, Managua, Nicaragua.
# #     - **🌎Nationality:** 
# #     - Nicaraguan 🇳🇮
    
# #     """
    
# #     )  
    
      

    
    

   

# # ### --- WORK HISTORY ---


# # st.write("#")
# # st.header("Work History")
# # st.write("---")


# # # --- JOB1

# # st.subheader("Structural Engineer | TangoBuilder")
# # st.write("***April 2022 - Present***")
# # st.write("""
# #          - 🏗️ Structural Analysis and Design  of Ground Up and Existing
# #         up to 4 stories wood residencies in San Francisco's Bay Area.
         
# #          - 🏗️ Contribution to the improvement of internal structural processes 
# #          by raising issues in Gitlab to prepare manuals. 
         
# #          - 🏗️ Validation of TangoBuilder's software by comparing its results 
# #          with manual structural design.
         
# #          - 🧑🏽‍💻 Revision and generation of structural calculations spreadsheets to be integrated
# #          into TangoBuilder's software.
         
# #          - 🧑🏽‍💻 Coordination and management of projects between different PEs to ensure high quality performance of the structural 
# #          team and meeting the due dates.
         
# #          """)


# # # --- JOB2

# # st.subheader("Structural Engineer | General Direction of Managua Municipality")
# # st.write("***January 2020 - April 2022***")
# # st.write("""
# #          - 🌊 Structural Drainage	design,	such as:	Channels,	box	culverts,  retention walls, wing walls, among others.
# #          - 🌉 Superstructure	and	substructure	design	of	steel	pedestrian  bridges.
# #          - 🌉 Prestressed	concrete	girders	design	for	vehicular	and  pedestrian bridges.
# #          - 🌊Steel Elevated water storage tanks Substructure and superstructure.
# #          - 🏢Structural Design of a Steel 2-storey shopping mall of 600 m2.
         
# #          """)

# # # --- JOB3

# # st.subheader("Structural Engineer intern | General Direction of Managua Municipality")
# # st.write("***July 2019 – December 2019***")
# # st.write("""
# #         - 🌊 Drainage	structures	design,	such	as:	manholes	of	the Juan  Pablo II road’s project.
# #         - 🌉 Structural Steel Bus stop booths design of Juan Pablo II road’s project.
# #         - 🌉 Prestressed concrete girders of a pedestrian bridge revision  of the Juan Pablo II road’s project.
         
# #          """)

# # # --- JOB4

# # st.subheader("Resident   building  manager’s    Assistant | CONIASA - CCA School Confined Masonry Building Project")
# # st.write("***February 2018 – August 2018***")
# # st.write("""
# #         - ✏️ In-situ	plan	drawings	to	support	the	resident	building  manager and the construction foreman.
# #         - 🧮 Take-off of the components of the project.
# #         - 📅 Weekly reports of the construction’s progress.
# #         - 👷 Supervision of the activities developed by the contractors.
        
# #          """)

# # # --- JOB5

# # st.subheader("Resident building manager’s Assistant |  CONIASA - BDF bank and ASSA insurance  company’s 8-story Steel building")
# # st.write("***June 2017 – February 2018***")
# # st.write("""
# #         - ✏️ Provide	plans	and	coordinate	the	scope	of	work	with	the  contractors.
# #         - 🧮 Material	volume’s	calculations	in	case	of	minor	works  adendum in the project.
# #         - 👷 In-situ drawing to support to the foreman team.
# #          """)


# # # --- Education ---

# # st.write("#")
# # st.header("Education")
# # st.write("---")
# # st.write("""
         
# #     - 🎓  **Student Candidate of a  Master Degree in Structural Engineering with Emphasis in Seismic Resistant Structures** |
# #         ***American University (UAM)*** | *2020 - Present*
        
# #     - 🎓 **Bachelor of Science in Civil Engineering** | ***National University of Engineering  (UNI)*** | *2015 - 2019*
    
# #     - 🎓 **High-School Graduate** | ***Latinamerican School*** | *2010-2014*
       
         
# #          """)


# # # --- Personal Projects  ---

# # st.write("#")
# # st.header("Personal Projects")
# # st.write("---")

# # st.write("""
# #      -   🏫 **Structural Assessment of a 2 story old masonry building Scholar Building in Granada, Nicaragua** |
# #         ***June 2023 - Present***
        
# #     -   🏫 **Structural Analysis and Design of a 2 story steel Scholar Building in Diriamba, Nicaragua** |
# #         ***March 2023*** 
             
# #     -  🏪 **Structural Analysis and Design of a 2 story steel commercial building in Chinandega, Nicaragua** |
# #         ***October 2021*** 
        
# #     -  🏠 **Structural Analysis and Design of a 1 story masonry residence building in Managua, Nicaragua** |
# #         ***February 2021***
         
# #          """)


# # # --- Courses ---

# # st.write("#")
# # st.header("Courses")
# # st.write("---")
# # st.write("""
        
# #     - 🎓  **Mathematics for Machine Learning: Linear Algebra** |
# #         ***Imperial College London - Coursera*** 
             
# #     - 🎓  **Cost and Budget course applied to civil  construction** |
# #         ***National University of Engineering  (UNI)*** 
        
# #     - 🎓 **Formulation and Evaluation of Projects  Course** |
# #         ***National University of Engineering  (UNI)***
    
# #     - 🎓 **Advanced Microsoft Excel Course.** | ***CAD center*** 
    
# #     - 🎓 **AutoCad 2D Course.** | ***Computation	Nicaraguan	Institute  (INC)*** 
       
         
# #          """)



# # # --- Languages ---

# # st.write("#")
# # st.header("Languages")
# # st.write("---")
# # data = pd.DataFrame(
# #     {
# #         "English - Proficient": [870],
# #         "Spanish - Native": [990],
# #         "German - Intermediate": [500],
           
# #     }
# # )

# # st.data_editor(data, 
# #                column_config = {
# #                    "English - Proficient": st.column_config.BarChartColumn(
# #                        "English - Proficient",
# #                        help = "Language ability",
# #                        y_min = 0,
# #                        y_max = 1000,
# #                    ),
# #                    "Spanish - Native": st.column_config.BarChartColumn(
# #                        "Spanish - Native",
# #                        help = "Language ability",
# #                        y_min = 0,
# #                        y_max = 1000,
# #                      ),  
# #                    "German - Intermediate": st.column_config.BarChartColumn(
# #                        "German - Intermediate",
# #                        help = "Language abilty",
# #                        y_min = 0,
# #                        y_max = 1000,
# #                      ),
                   
# #                }, 
# #                hide_index = True,
# # )

    
# # ### --- SKILLS ---

# # data_df = pd.DataFrame(
# #     {
# #         "CSI - SAP2000": [85],
# #         "CSI - Etabs": [90],
# #         "CSI - SAFE": [80],
# #         "IDEA - Statica": [75],
           
# #     }
# # )

# # data_df1 = pd.DataFrame(
# #     {
# #         "Bentley - Ram Connection": [80],
# #         "WeyerHaeuser - ForteWeb webapp": [85],
# #         "PTC MATHCAD prime": [80],
# #         "Microsoft Office package": [85],
        
        
# #     }
# # )

# # data_df2 = pd.DataFrame(
# #     {
# #         "Jupyter notebook": [90],
# #         "Tekla Tedds": [90],
# #         "Autodesk - Autocad": [75], 
# #         "Autodesk - Revit": [75], 
        
# #     }
# # )

# # data_df3 = pd.DataFrame(
# #     {
# #       "Python": [80], 
# #         "Latex and Markdown": [85],
# #         "Matlab": [85],
# #         "VsCode editor and Anaconda": [85],
        
             
# #     }
# # )

# # data_df4 = pd.DataFrame(
# #     {
# #         "ClickUp": [85],
# #         "TangoBuilder's webapp": [95],
             
# #     }
# # )


# # st.write("#")
# # st.header("Hard Skills")
# # st.divider()
# # st.data_editor(data_df, 
# #                column_config = {
# #                    "CSI - SAP2000": st.column_config.ProgressColumn(
# #                        "CSI - SAP 2000",
# #                        help = "Software ability",
# #                        format = "%f",
# #                        min_value = 0,
# #                        max_value = 100,
# #                    ),
# #                    "CSI - Etabs": st.column_config.ProgressColumn(
# #                        "CSI - Etabs",
# #                        help = "Software ability",
# #                        format = "%f",
# #                        min_value = 0,
# #                        max_value = 100,
# #                      ),  
# #                    "CSI - SAFE": st.column_config.ProgressColumn(
# #                        "CSI - SAFE",
# #                        help = "Software abilty",
# #                        format = "%f",
# #                        min_value = 0,
# #                        max_value = 100,
# #                      ),
# #                    "IDEA - Statica": st.column_config.ProgressColumn(
# #                        "IDEA - Statica",
# #                        help = "Software ability",
# #                        format = "%f",
# #                        min_value = 0,
# #                        max_value = 100,
# #                      ),
                   
# #                }, 
# #                hide_index = True,
# # )

# # st.data_editor(data_df1, 
# #                column_config = {
# #                    "Bentley - Ram Connection": st.column_config.ProgressColumn(
# #                        "Bentley - Ram Connection",
# #                        help = "Software ability",
# #                        format = "%f",
# #                        min_value = 0,
# #                        max_value = 100,
# #                      ),
# #                    "WeyerHaeuser - ForteWeb webapp": st.column_config.ProgressColumn(
# #                        "WeyerHaeuser - ForteWeb webapp",
# #                        help = "Software ability",
# #                        format = "%f",
# #                        min_value = 0,
# #                        max_value = 100,
# #                      ),
# #                    "PTC MATHCAD prime": st.column_config.ProgressColumn(
# #                        "PTC MATHCAD prime",
# #                        help = "Software ability",
# #                        format = "%f",
# #                        min_value = 0,
# #                        max_value = 100,
# #                      ),
# #                    "Microsoft Office package": st.column_config.ProgressColumn(
# #                        "Microsoft Office package",
# #                        help = "Software ability",
# #                        format = "%f",
# #                        min_value = 0,
# #                        max_value = 100,
# #                      ),
                   
# #                }, 
# #                hide_index = True,
# # )

# # st.data_editor(data_df2, 
# #                column_config = {
                   
# #                    "Jupyter notebook": st.column_config.ProgressColumn(
# #                        "Jupyter notebook",
# #                        help = "Software ability",
# #                        format = "%f",
# #                        min_value = 0,
# #                        max_value = 100,
# #                      ),
                   
# #                    "Tekla Tedds": st.column_config.ProgressColumn(
# #                        "Tekla Tedds",
# #                        help = "Software ability",
# #                        format = "%f",
# #                        min_value = 0,
# #                        max_value = 100,
# #                      ),
                   
# #                    "Autodesk - Autocad": st.column_config.ProgressColumn(
# #                        "Autodesk - Autocad",
# #                        help = "Software ability",
# #                        format = "%f",
# #                        min_value = 0,
# #                        max_value = 100,
# #                      ),
                   
# #                    "Autodesk - Revit": st.column_config.ProgressColumn(
# #                        "Autodesk - Revit",
# #                        help = "Software ability",
# #                        format = "%f",
# #                        min_value = 0,
# #                        max_value = 100,
# #                      ),
                   
# #                }, 
# #                hide_index = True,
# # )

# # st.data_editor(data_df3, 
# #                column_config = {
                 
# #                    "Python": st.column_config.ProgressColumn(
# #                        "Python",
# #                        help = "Software ability",
# #                        format = "%f",
# #                        min_value = 0,
# #                        max_value = 100,
                    
                   
# #                      ),
# #                    "Latex and Markdown": st.column_config.ProgressColumn(
# #                        "Latex and Markdown",
# #                        help = "Software ability",
# #                        format = "%f",
# #                        min_value = 0,
# #                        max_value = 100,
# #                      ),
                   
# #                    "Matlab": st.column_config.ProgressColumn(
# #                        "Matlab",
# #                        help = "Software ability",
# #                        format = "%f",
# #                        min_value = 0,
# #                        max_value = 100, 
# #                        ),
                   
# #                       "VsCode editor and Anaconda": st.column_config.ProgressColumn(
# #                        "VsCode editor and Anaconda",
# #                        help = "Software ability",
# #                        format = "%f",
# #                        min_value = 0,
# #                        max_value = 100,
# #                      ),
# #                }, 
# #                hide_index = True,
# # )

# # st.data_editor(data_df4, 
# #                column_config = {
                   
                   
                   
                   
# #                    "ClickUp": st.column_config.ProgressColumn(
# #                        "ClickUp",
# #                        help = "Software ability",
# #                        format = "%f",
# #                        min_value = 0,
# #                        max_value = 100,
# #                      ),
                   
# #                    "TangoBuilder's webapp": st.column_config.ProgressColumn(
# #                        "TangoBuilder's webapp",
# #                        help = "Software ability",
# #                        format = "%f",
# #                        min_value = 0,
# #                        max_value = 100,
# #                      ),
                
                   
# #                }, 
# #                hide_index = True,
# # )


# # st.write("#")
# # st.header("Soft Skills")
# # st.divider()
# # st.write(
# #     """
# #     - 🗣️ Assertive communication and strong aptitude for teamwork.
# #     - 🔥 Productive and proactive.
# #     - 🤞 Easy-going person.
# #     - 🤓 Self - learner and hard - working.
# #     - 👂 Active and attentive listener.
# #     - ❗ Resolute decision-maker to take effective choices
# #     - 🏃‍♂️ Highly adaptable to quickly acclimate to new procedures and processes.
    
# #     """
    
# # ) 