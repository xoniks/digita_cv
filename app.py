from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Egezon Baruti"
PAGE_ICON = ":wave:"
NAME = "Egezon Baruti"
DESCRIPTION = """
Data Scientist specializing in spatial-sensor data and data-driven decision-making.
"""
EMAIL = "egzonbaruti@yahoo.com"
SOCIAL_MEDIA = {
    "LinkedIn: https://www.linkedin.com/in/egezonbaruti",
    # "GitHub": "https://github.com",
    # "Twitter": "https://twitter.com",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write("\n")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ Extensive experience with spatial-sensor data and algorithm development.
- ✔️ Skilled in Python (FastAPI, Pandas, Numpy), SQL, DBT, and Airflow.
- ✔️ Experienced in visualizing and analyzing sensor data to deliver insights.
- ✔️ Proficient in PowerBI and interactive dashboard development.
"""
)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (FastAPI, Scikit-learn, Pandas), SQL, DBT
- 📊 Data Visualization: PowerBI, Streamlit
- 🗄️ Databases: Snowflake, AWS, PostgreSQL
- 🤖 Machine Learning: Neural networks, classification algorithms
"""
)

# --- WORK HISTORY ---
st.write("\n")
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Scientist | TIVE Inc., Prishtina**")
st.write("11/2023 - 11/2024")
st.write(
    """
- ► Built classification algorithms for spatial-sensor data using Python (FastAPI), SQL, DBT, and Airflow.
- ► Analyzed and visualized sensor data trends to support decision-making.
"""
)

# --- JOB 2
st.write("\n")
st.write("🚧", "**Data Scientist | Raiffeisen Bank Kosovo, Prishtina**")
st.write("10/2021 - 08/2023")
st.write(
    """
- ► Validated ML scorecards in collaboration with Raiffeisen Bank International.
- ► Forecasted patterns using advanced data science techniques.
- ► Developed impactful PowerBI dashboards for business insights.
"""
)

# --- JOB 3
st.write("\n")
st.write("🚧", "**AI Instructor | OSCE, Prishtina**")
st.write("05/2023 (Fixed-term)")
st.write(
    """
- ► Delivered training on large language models (LLMs) and generative AI.
- ► Equipped participants with tools to integrate AI in public relations strategies.
"""
)

# --- JOB 4
st.write("\n")
st.write("🚧", "**Coding Instructor | BIT Academy, Prishtina**")
st.write("05/2022 - 05/2023")
st.write(
    """
- ► Taught Python, SQL, and Django with applications in data science.
- ► Guided students in machine learning and data visualization projects.
- ► Conducted backend development workshops and GUI programming with Tkinter.
"""
)

# --- JOB 5
st.write("\n")
st.write("🚧", "**Teaching Assistant | London School of Economics / Kolegji Riinvest, Prishtina**")
st.write("10/2022 - Present (Part-time)")
st.write(
    """
- ► Assisted in teaching Machine Learning and Business Analytics.
- ► Supported students in building machine learning models and data strategies.
"""
)

# --- JOB 6
st.write("\n")
st.write("🚧", "**Data Analyst | Finca Kosovo, Prishtina**")
st.write("06/2021 - 10/2021")
st.write(
    """
- ► Developed and implemented machine learning models for scoring.
- ► Automated daily reports and created data visualizations for stakeholders.
"""
)

# --- JOB 7
st.write("\n")
st.write("🚧", "**Math and IT Teacher | International School of Prishtina, Prishtina**")
st.write("09/2015 - 05/2021")
st.write(
    """
- ► Taught Mathematics, IT, and introductory machine learning.
- ► Served as Vice Principal, showcasing leadership in curriculum development.
- ► Instructed robotics and coding with Python and Scratch.
"""
)

# --- Projects & Accomplishments ---
# st.write("\n")
# st.subheader("Projects & Accomplishments")
# st.write("---")
# for project, link in SOCIAL_MEDIA.items():
#     st.write(f"[{project}]({link})")
