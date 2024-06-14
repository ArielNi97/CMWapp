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
    "**Github**" : "https://github.com/ArielNi97",
    }

# st.subheader("Social media")
    
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")
        
    