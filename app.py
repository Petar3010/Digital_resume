from pathlib import Path

import streamlit as st
from PIL import Image

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "Styles" / "main.css"
resume_file = current_dir / "Assets" / "Petar Anev CV.pdf"
profile_pic = current_dir / "Assets" / "CV photo.jpg"


PAGE_TITLE = "Digital CV | Petar Anev"
PAGE_ICON = ":WAVE:"
NAME = "Petar Anev"
TELEPHONE = "+359897939928"
DESCRIPTION = """
A Software Test Engineer seeking a challenging and progressive position to gain
knowledge and experience from it.
"""
EMAIL = "petaranevq@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/petar-anev/",
    "GitHub": "https://github.com/Petar3010?tab=repositories",
}

CERTIFICATES = {
    "SoftUni/QA Fundamental": "https://softuni.bg/certificates/details/200643/af74fe7d",
    "SoftUni/Software Technologies": "https://softuni.bg/certificates/details/191687/e8effe5f",
    "SoftUni/QA Basic": "https://softuni.bg/certificates/details/176971/cab66d43",
    "Udemy/Software Testing Bootcamp": "https://www.udemy.com/certificate/UC-29ad752f-fa1a-4941-9f23-3d08e776247d/",
    "Udemy/QA Manual Testing": "https://www.udemy.com/certificate/UC-4e00286f-c3ba-423c-9f0a-9ff510f0b1b6/",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, 'rb') as pdf_file:
    PDFbyte = pdf_file.read()


profile_pic = Image.open(profile_pic)

col1, col2 = st.columns(2, gap='small')
with col1:
    st.image(profile_pic, width=200)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("Email:", EMAIL)
    st.write("Phone Number:", TELEPHONE)

st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

st.write("#")
st.subheader("Online Certificates")

st.write("#")
cols = st.columns(len(CERTIFICATES))
for index, (platform, link) in enumerate(CERTIFICATES.items()):
    cols[index].write(f"[{platform}]({link})")

st.markdown("----------------------------------------------------------")

st.write("#")
st.subheader("Previous Experience")
st.write(
    """
    QA tester at Utest as a freelancer. 
    Contributed to crowd-sourced testing projects for globally recognized brands,
including “Tidal”, “Nike”, and “Moncler”
    """
)
st.markdown("----------------------------------------------------------------------------")

st.write("#")
st.subheader("Hard Skills")
st.write(
    """
     ✓ Bug Reporting & Test Case writing skills.\n
     ✓ Knowledge of Agile software methodologies.\n
     ✓ Knowledge of SQL database.\n
     ✓ Knowledge of API Testing (Postman), Performance Testing(JMeter) , Mobile Testing.\n
     ✓ knowledge of Python.\n
     ✓ Basic knowledge of HTML and CSS.\n
     ✓ Basic knowledge of Git and GitHub.\n
     ✓ Basic knowledge of Operations Systems.\n
     ✓ Basic knowledge of Internet and Protocols.\n
     """
)

st.markdown("----------------------------------------------------------------------------------")

st.write("#")
st.subheader("Soft Skills")
st.write(
    """
    ✓ Communication Skills\n
    ✓ Teamwork and Collaboration\n
    ✓ Problem-Solving and Critical Thinking\n
    
    """
)

st.markdown("-----------------------------------------------------------------------------------")

