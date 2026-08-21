import streamlit as st

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Arthi Sathishkumar | Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# SESSION STATE
# =========================================================

if "projects" not in st.session_state:
    st.session_state.projects = [
        {
            "name": "Smart AutoML Platform",
            "description": (
                "A Streamlit-based platform for automated data "
                "preprocessing, machine learning model training "
                "and evaluation."
            ),
            "technologies": "Python, Streamlit",
            "status": "In Progress",
            "github": "",
            "demo": ""
        },
        {
            "name": "College Timetable Notification System",
            "description": (
                "A system designed to manage college timetables "
                "and provide notifications to students and staff."
            ),
            "technologies": "Python, Streamlit",
            "status": "Ongoing",
            "github": "",
            "demo": ""
        },
        {
            "name": "Business Dashboard",
            "description": (
                "A business-related dashboard designed to display "
                "business information and insights through an "
                "interactive interface."
            ),
            "technologies": "Python, Streamlit",
            "status": "Completed",
            "github": "",
            "demo": ""
        }
    ]

if "python_materials" not in st.session_state:
    st.session_state.python_materials = []

if "certificates" not in st.session_state:
    st.session_state.certificates = []

if "achievements" not in st.session_state:
    st.session_state.achievements = []


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <link rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">

    <style>

    .stApp {
        background-color: #ffffff;
        color: #1f2937;
    }

    #MainMenu {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    .block-container {
        max-width: 1150px;
        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }

    /* Navigation */

    .navbar {
        text-align: center;
        padding: 18px 5px;
        border-bottom: 1px solid #e5e7eb;
        margin-bottom: 30px;
    }

    .navbar a {
        text-decoration: none;
        color: #374151;
        margin: 0 12px;
        font-size: 14px;
        font-weight: 500;
    }

    .navbar a:hover {
        color: #2563eb;
    }

    .nav-icon {
        color: #2563eb;
        margin-right: 5px;
    }

    /* Hero */

    .hero {
        text-align: center;
        padding: 65px 20px;
    }

    .hero-name {
        font-size: 48px;
        font-weight: 750;
        color: #111827;
        margin-bottom: 12px;
    }

    .hero-title {
        font-size: 21px;
        color: #4b5563;
        margin-bottom: 20px;
    }

    .hero-bio {
        max-width: 850px;
        margin: auto;
        color: #6b7280;
        line-height: 1.8;
        font-size: 16px;
    }

    /* Sections */

    .section-title {
        font-size: 30px;
        font-weight: 700;
        color: #111827;
        margin-top: 45px;
        margin-bottom: 8px;
    }

    .section-line {
        width: 55px;
        height: 4px;
        background-color: #2563eb;
        border-radius: 5px;
        margin-bottom: 28px;
    }

    /* Cards */

    .card {
        background-color: #f8fafc;
        border: 1px solid #e5e7eb;
        border-radius: 14px;
        padding: 25px;
        margin-bottom: 20px;
    }

    .card-title {
        font-size: 20px;
        font-weight: 650;
        color: #111827;
        margin-bottom: 12px;
    }

    .card-text {
        font-size: 15px;
        color: #6b7280;
        line-height: 1.75;
    }

    /* Icons */

    .icon {
        color: #2563eb;
        margin-right: 10px;
    }

    /* Skills */

    .skill {
        display: inline-block;
        padding: 9px 17px;
        margin: 5px;
        border: 1px solid #d1d5db;
        border-radius: 20px;
        background-color: #ffffff;
        color: #374151;
        font-size: 14px;
    }

    /* Project status */

    .status {
        display: inline-block;
        padding: 5px 12px;
        border-radius: 20px;
        background-color: #e0f2fe;
        color: #0369a1;
        font-size: 12px;
        margin-bottom: 15px;
    }

    /* Footer */

    .footer {
        text-align: center;
        padding: 30px 10px;
        margin-top: 60px;
        border-top: 1px solid #e5e7eb;
        color: #6b7280;
        font-size: 14px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# NAVIGATION
# =========================================================

st.markdown(
    """
    <div class="navbar">

    <a href="#home">
    <i class="fa-solid fa-house nav-icon"></i>Home
    </a>

    <a href="#about">
    <i class="fa-solid fa-user nav-icon"></i>About
    </a>

    <a href="#education">
    <i class="fa-solid fa-graduation-cap nav-icon"></i>Education
    </a>

    <a href="#skills">
    <i class="fa-solid fa-code nav-icon"></i>Skills
    </a>

    <a href="#projects">
    <i class="fa-solid fa-folder-open nav-icon"></i>Projects
    </a>

    <a href="#certificates">
    <i class="fa-solid fa-certificate nav-icon"></i>Certificates
    </a>

    <a href="#achievements">
    <i class="fa-solid fa-trophy nav-icon"></i>Achievements
    </a>

    <a href="#contact">
    <i class="fa-solid fa-envelope nav-icon"></i>Contact
    </a>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HOME
# =========================================================

st.markdown('<div id="home"></div>', unsafe_allow_html=True)

st.markdown(
    """
    <div style="text-align:center; padding:60px 20px;">

        <h1 style="font-size:48px; color:#111827;">
            Arthi Sathishkumar
        </h1>

        <h3 style="color:#4b5563;">
            B.Tech Artificial Intelligence and Data Science Student
        </h3>

        <p style="max-width:850px; margin:auto; line-height:1.8; color:#6b7280;">
            Inspired by my senior, Mr. M. Siva Subramaniyam.
            Passionate about Artificial Intelligence, Data Science, and Python.
            Currently exploring Machine Learning and building practical projects
            using Python and Streamlit. Continuously learning new technologies
            and working towards achieving my goals early in life.
        </p>

    </div>
    """,
    unsafe_allow_html=True
)
# =========================================================
# PROFILE PHOTO
# =========================================================

photo_col1, photo_col2, photo_col3 = st.columns([1, 2, 1])

with photo_col2:

    profile_photo = st.file_uploader(
        "Upload Profile Photo",
        type=["png", "jpg", "jpeg"],
        key="profile_photo"
    )

    if profile_photo:
        st.image(
            profile_photo,
            width=180
        )


# =========================================================
# HOME BUTTONS
# =========================================================

button1, button2 = st.columns(2)

with button1:

    st.markdown(
        """
        <a href="#projects">
        <button style="
        width:100%;
        padding:12px;
        border:none;
        border-radius:8px;
        background:#2563eb;
        color:white;
        font-size:15px;
        cursor:pointer;">
        <i class="fa-solid fa-folder-open"></i>
        View Projects
        </button>
        </a>
        """,
        unsafe_allow_html=True
    )


with button2:

    resume_home = st.file_uploader(
        "Upload Resume PDF",
        type=["pdf"],
        key="resume_home"
    )

    if resume_home:

        st.download_button(
            "Download Resume",
            data=resume_home,
            file_name="Arthi_Sathishkumar_Resume.pdf",
            mime="application/pdf",
            use_container_width=True
        )


# =========================================================
# ABOUT
# =========================================================

st.markdown('<div id="about"></div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="section-title">
    <i class="fa-solid fa-user icon"></i>
    About Me
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="section-line"></div>', unsafe_allow_html=True)

st.write(
    """
    I am a B.Tech Artificial Intelligence and Data Science student
    with a strong interest in exploring new technologies. I am
    developing my technical skills through academic projects and
    practical learning.

    I believe in continuous learning, taking inspiration from my
    seniors, and consistently working towards my future goals.
    """
)


# =========================================================
# PERSONAL GOAL
# =========================================================

st.markdown(
    """
    <div class="card">

    <div class="card-title">
    <i class="fa-solid fa-bullseye icon"></i>
    Personal Goal
    </div>

    <div class="card-text">

    My goal is to continuously improve my technical skills,
    build meaningful projects, and grow as an AI & Data Science
    professional.

    I also aim to build my career and work at
    <strong>SS40 Network Pvt. Ltd.</strong>.

    </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# EDUCATION
# =========================================================

st.markdown('<div id="education"></div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="section-title">
    <i class="fa-solid fa-graduation-cap icon"></i>
    Education
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="section-line"></div>', unsafe_allow_html=True)

edu1, edu2 = st.columns(2)

with edu1:

    st.markdown(
        """
        <div class="card">

        <div class="card-title">
        B.Tech - Artificial Intelligence and Data Science
        </div>

        <div class="card-text">
        Thamirabharani Engineering College<br>
        2nd Year - 3rd Semester
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with edu2:

    st.markdown(
        """
        <div class="card">

        <div class="card-title">
        School Education
        </div>

        <div class="card-text">
        12th - Government Higher Secondary School, Kuttam<br>
        10th - Government Higher Secondary School, Kuttam
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# SKILLS
# =========================================================

st.markdown('<div id="skills"></div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="section-title">
    <i class="fa-solid fa-code icon"></i>
    Skills
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="section-line"></div>', unsafe_allow_html=True)

skills = [
    "Python",
    "C",
    "Streamlit",
    "GitHub"
]

for skill in skills:

    st.markdown(
        f'<span class="skill">{skill}</span>',
        unsafe_allow_html=True
    )


# =========================================================
# CURRENTLY LEARNING
# =========================================================

st.markdown(
    """
    <div class="card">

    <div class="card-title">
    <i class="fa-solid fa-book-open icon"></i>
    Currently Learning
    </div>

    <div class="card-text">

    <span class="skill">Artificial Intelligence</span>
    <span class="skill">Data Science</span>
    <span class="skill">New Python Concepts</span>

    </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# NEW PYTHON CONCEPTS UPLOAD
# =========================================================

st.subheader("New Python Concepts")

python_material = st.file_uploader(
    "Upload your Python learning material",
    type=["pdf", "txt", "py", "docx"],
    key="python_material"
)

if python_material:

    if python_material.name not in st.session_state.python_materials:

        st.session_state.python_materials.append(
            python_material.name
        )

    st.success(
        f"{python_material.name} uploaded successfully."
    )

if st.session_state.python_materials:

    st.write("Uploaded Learning Materials")

    for material in st.session_state.python_materials:

        st.write(material)


# =========================================================
# PROJECTS
# =========================================================

st.markdown('<div id="projects"></div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="section-title">
    <i class="fa-solid fa-folder-open icon"></i>
    Projects
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="section-line"></div>', unsafe_allow_html=True)


# Existing Projects

for project in st.session_state.projects:

    st.markdown(
        f"""
        <div class="card">

        <div class="card-title">
        {project["name"]}
        </div>

        <span class="status">
        {project["status"]}
        </span>

        <div class="card-text">

        <strong>Short Description</strong><br>
        {project["description"]}

        <br><br>

        <strong>Technologies Used</strong><br>
        {project["technologies"]}

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    p1, p2 = st.columns(2)

    with p1:

        if project["github"]:

            st.link_button(
                "GitHub",
                project["github"],
                use_container_width=True
            )

    with p2:

        if project["demo"]:

            st.link_button(
                "Live Demo",
                project["demo"],
                use_container_width=True
            )


# =========================================================
# ADD PROJECT
# =========================================================

st.subheader("Add New Project")

with st.form("add_project_form"):

    new_name = st.text_input(
        "Project Name"
    )

    new_description = st.text_area(
        "Short Description"
    )

    new_technologies = st.text_input(
        "Technologies Used"
    )

    new_status = st.selectbox(
        "Status",
        [
            "Completed",
            "In Progress",
            "Ongoing"
        ]
    )

    new_github = st.text_input(
        "GitHub Link"
    )

    new_demo = st.text_input(
        "Live Demo Link"
    )

    submit_project = st.form_submit_button(
        "Add Project",
        use_container_width=True
    )

    if submit_project:

        if new_name and new_description:

            st.session_state.projects.append(
                {
                    "name": new_name,
                    "description": new_description,
                    "technologies": new_technologies,
                    "status": new_status,
                    "github": new_github,
                    "demo": new_demo
                }
            )

            st.success(
                "Project added successfully."
            )

            st.rerun()

        else:

            st.warning(
                "Project Name and Short Description are required."
            )


# =========================================================
# CERTIFICATES
# =========================================================

st.markdown('<div id="certificates"></div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="section-title">
    <i class="fa-solid fa-certificate icon"></i>
    Certificates
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="section-line"></div>', unsafe_allow_html=True)

certificate = st.file_uploader(
    "Upload Certificate PDF",
    type=["pdf"],
    key="certificate"
)

if certificate:

    if certificate.name not in st.session_state.certificates:

        st.session_state.certificates.append(
            certificate.name
        )

    st.success(
        f"{certificate.name} uploaded successfully."
    )

if st.session_state.certificates:

    for cert in st.session_state.certificates:

        st.write(cert)


# =========================================================
# ACHIEVEMENTS
# =========================================================

st.markdown('<div id="achievements"></div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="section-title">
    <i class="fa-solid fa-trophy icon"></i>
    Achievements
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="section-line"></div>', unsafe_allow_html=True)

achievement = st.file_uploader(
    "Upload Achievement PDF",
    type=["pdf"],
    key="achievement"
)

if achievement:

    if achievement.name not in st.session_state.achievements:

        st.session_state.achievements.append(
            achievement.name
        )

    st.success(
        f"{achievement.name} uploaded successfully."
    )

if st.session_state.achievements:

    for item in st.session_state.achievements:

        st.write(item)


# =========================================================
# CONTACT
# =========================================================

st.markdown('<div id="contact"></div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="section-title">
    <i class="fa-solid fa-envelope icon"></i>
    Contact
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="section-line"></div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:

    st.markdown(
        """
        <div class="card">

        <div class="card-title">
        <i class="fa-brands fa-github icon"></i>
        GitHub
        </div>

        <div class="card-text">
        ArthiSathishkumar
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.link_button(
        "Visit GitHub",
        "https://github.com/ArthiSathishkumar",
        use_container_width=True
    )


with c2:

    st.markdown(
        """
        <div class="card">

        <div class="card-title">
        <i class="fa-brands fa-linkedin icon"></i>
        LinkedIn
        </div>

        <div class="card-text">
        LinkedIn profile link will be added later.
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


with c3:

    st.markdown(
        """
        <div class="card">

        <div class="card-title">
        <i class="fa-solid fa-envelope icon"></i>
        Email
        </div>

        <div class="card-text">
        s.arthi1027@gmail.com
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.link_button(
        "Send Email",
        "mailto:s.arthi1027@gmail.com",
        use_container_width=True
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">

    © 2026 Arthi Sathishkumar |
    Built with Python and Streamlit

    </div>
    """,
    unsafe_allow_html=True
)
