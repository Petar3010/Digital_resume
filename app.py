from pathlib import Path

import streamlit as st
from PIL import Image

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "Styles" / "main.css"
resume_file = current_dir / "Assets" / "Petar Pavlov Anev CV.pdf"
profile_pic = current_dir / "Assets" / "CV photo.jpg"


PAGE_TITLE = "Digital CV | Petar Anev"
PAGE_ICON = ":WAVE:"
NAME = "Petar Anev"
TELEPHONE = "+359897939928"
DESCRIPTION = """
My experience in quality assurance involves testing and validating 
insurance and financial software systems, ensuring accuracy, 
functionality, and compliance with industry standards while 
collaborating with teams to deliver reliable solutions. .
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
    "SoftUni/Programming basic (Python)": "https://softuni.bg/certificates/details/210029/dfe6664e",
    "Udemy/QA Automation Testing (Python)": "https://www.udemy.com/certificate/UC-059727cc-81a5-4624-bcd4-054859639231/",
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

for cert_name, cert_link in CERTIFICATES.items():
    st.markdown(f"➡️ [{cert_name}]({cert_link})")

# st.write("#")
# cols = st.columns(len(CERTIFICATES))
# for index, (platform, link) in enumerate(CERTIFICATES.items()):
#     cols[index].write(f"[{platform}]({link})")

st.markdown("----------------------------------------------------------")

st.write("#")
st.subheader("Previous Experience")
st.write(
    """
    ✓ QA Tester | Utest.com (freelance) (07.2023 – 05.2024).\n
    ✓ QA intern | Soft intellect (Full time) (05.2024 – 08.2024).\n
    ✓ QA specialist | Soft intellect (Full time) (09.2024).\n
    ✓ Auto - diagnostic Specialist (09.2011 – 05.2023).\n
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
     ✓ Knowledge of Python.\n
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

