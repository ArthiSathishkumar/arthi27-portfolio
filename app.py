import streamlit as st
import json
from pathlib import Path
from datetime import date

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Arthi Sathishkumar | Portfolio",
    page_icon="A",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).parent

DATA_DIR = BASE_DIR / "portfolio_data"
UPLOAD_DIR = BASE_DIR / "uploads"

DATA_DIR.mkdir(exist_ok=True)
UPLOAD_DIR.mkdir(exist_ok=True)

PROJECTS_FILE = DATA_DIR / "projects.json"
EXPERIENCE_FILE = DATA_DIR / "experience.json"
CERTIFICATES_FILE = DATA_DIR / "certificates.json"
ACHIEVEMENTS_FILE = DATA_DIR / "achievements.json"

# ============================================================
# DEFAULT DATA
# ============================================================

DEFAULT_PROJECTS = [
    {
        "name": "Business Dashboard",
        "description": "An interactive dashboard designed to visualize and understand business data through clear analytics and insights.",
        "technologies": "Python, Streamlit, Pandas, Plotly",
        "github": "https://github.com/ArthiSathishkumar/bussiness-dashboard",
        "live": "https://bussiness-dashboard-ydgnjbs5uhwvvzhdx5h9sn.streamlit.app/",
        "image": "",
    },
    {
        "name": "AI Auto Smart Finance Manager",
        "description": "An AI-powered finance management application for tracking transactions, analyzing spending, and identifying financial waste.",
        "technologies": "Python, Streamlit, Pandas, AI",
        "github": "https://github.com/ArthiSathishkumar/AI-Auto-Finance-Manager",
        "live": "https://ai-auto-finance-manager-9hbantsdjnxqzduxjah2c7.streamlit.app/",
        "image": "",
    },
    {
        "name": "Skill Gap Analyzer",
        "description": "A career-focused application that compares skills with target job requirements and provides missing skills, ranking, and learning roadmap insights.",
        "technologies": "Python, Streamlit, Data Science",
        "github": "https://github.com/ArthiSathishkumar/skill-gap-analyser",
        "live": "https://skill-gap-analyser-hg9jurdi2tdb3bitjj2wxq.streamlit.app/",
        "image": "",
    },
    {
        "name": "Smart AutoML Platform",
        "description": "An automated machine learning platform that processes uploaded datasets and provides model evaluation and performance insights.",
        "technologies": "Python, Streamlit, Pandas, NumPy, Scikit-learn",
        "github": "https://github.com/ArthiSathishkumar/data-process",
        "live": "https://data-process-c4ntmm9qdj93dtcdwqmdam.streamlit.app/",
        "image": "",
    },
]

DEFAULT_EXPERIENCE = [
    {
        "company": "Codomax Digital Solutions",
        "role": "Full Stack Intern",
        "type": "Full Stack Internship",
        "duration": "Internship",
        "start": "",
        "end": "",
        "description": "Worked on a Blog Application and developed registration, login, and blog-related APIs using Node.js and Express.",
        "skills": "Node.js, Express.js, REST APIs, GitHub",
        "website": "",
        "certificate": "",
        "offer_letter": "",
    }
]

DEFAULT_CERTIFICATES = [
    {
        "name": "YAASC Certificate",
        "organization": "YAASC",
        "date": "",
        "file": "",
        "credential": "",
    }
]

DEFAULT_ACHIEVEMENTS = [
    {
        "title": "Smart India Hackathon Participation",
        "description": "Participated in Smart India Hackathon with a weather-focused big data analytics platform idea.",
        "date": "",
        "proof": "",
        "link": "",
    },
    {
        "title": "Hackathon Participation",
        "description": "Participated in hackathon activities and worked on technology-based problem solving with a team.",
        "date": "",
        "proof": "",
        "link": "",
    },
    {
        "title": "Workshops and Seminars",
        "description": "Participated in technical workshops and seminars to explore emerging technologies and improve practical knowledge.",
        "date": "",
        "proof": "",
        "link": "",
    },
    {
        "title": "Workshops and Seminars Conducted",
        "description": "Conducted workshops and seminars to share technical knowledge and support peer learning.",
        "date": "",
        "proof": "",
        "link": "",
    },
]

# ============================================================
# DATA FUNCTIONS
# ============================================================

def load_json(file_path, default_data):
    if not file_path.exists():
        save_json(file_path, default_data)
        return default_data

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception:
        return default_data


def save_json(file_path, data):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


projects = load_json(PROJECTS_FILE, DEFAULT_PROJECTS)
experience = load_json(EXPERIENCE_FILE, DEFAULT_EXPERIENCE)
certificates = load_json(CERTIFICATES_FILE, DEFAULT_CERTIFICATES)
achievements = load_json(ACHIEVEMENTS_FILE, DEFAULT_ACHIEVEMENTS)

# ============================================================
# CUSTOM CSS
# ============================================================

st.html(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(90, 80, 180, 0.12), transparent 25%),
        radial-gradient(circle at 90% 20%, rgba(30, 120, 180, 0.10), transparent 25%),
        #080b12;
    color: #f5f7fb;
}

section[data-testid="stSidebar"] {
    background: #0d111a;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* Navigation */

.nav-box {
    background: rgba(17, 23, 34, 0.82);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 15px 22px;
    margin-bottom: 35px;
    backdrop-filter: blur(10px);
}

.brand {
    font-size: 22px;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: -0.5px;
}

.brand span {
    color: #8b7cff;
}

/* Hero */

.hero {
    padding: 65px 10px 70px 10px;
}

.hero-small {
    color: #8b7cff;
    font-size: 16px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 12px;
}

.hero-title {
    font-size: clamp(42px, 7vw, 78px);
    line-height: 1.02;
    font-weight: 800;
    letter-spacing: -4px;
    margin: 0;
    color: #ffffff;
}

.hero-title span {
    color: #8b7cff;
}

.hero-subtitle {
    font-size: 21px;
    line-height: 1.7;
    max-width: 760px;
    color: #aeb6c7;
    margin-top: 25px;
}

.hero-tagline {
    font-size: 17px;
    color: #dce1ea;
    margin-top: 25px;
    font-weight: 600;
}

/* Section */

.section-title {
    font-size: 34px;
    font-weight: 800;
    margin-top: 50px;
    margin-bottom: 8px;
    color: #ffffff;
    letter-spacing: -1px;
}

.section-line {
    width: 55px;
    height: 4px;
    background: #8b7cff;
    border-radius: 20px;
    margin-bottom: 30px;
}

.section-description {
    color: #9fa8b9;
    font-size: 16px;
    line-height: 1.7;
    max-width: 800px;
    margin-bottom: 30px;
}

/* Cards */

.card {
    background: rgba(17, 23, 34, 0.78);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 20px;
    padding: 26px;
    height: 100%;
    transition: 0.2s ease;
}

.card:hover {
    border-color: rgba(139,124,255,0.45);
    transform: translateY(-2px);
}

.card-title {
    color: #ffffff;
    font-size: 21px;
    font-weight: 700;
    margin-bottom: 10px;
}

.card-text {
    color: #aeb6c7;
    line-height: 1.7;
    font-size: 15px;
}

.tag {
    display: inline-block;
    padding: 7px 11px;
    margin: 5px 5px 0 0;
    background: rgba(139,124,255,0.10);
    border: 1px solid rgba(139,124,255,0.20);
    border-radius: 9px;
    color: #c8c1ff;
    font-size: 13px;
}

/* Skill */

.skill-box {
    background: #111722;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px;
    padding: 18px;
    margin-bottom: 15px;
}

.skill-heading {
    color: #ffffff;
    font-weight: 700;
    margin-bottom: 12px;
}

/* Education */

.timeline-card {
    border-left: 3px solid #8b7cff;
    background: rgba(17,23,34,0.7);
    padding: 24px 28px;
    border-radius: 0 18px 18px 0;
    margin-bottom: 20px;
}

.timeline-year {
    color: #8b7cff;
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 7px;
}

.timeline-title {
    font-size: 20px;
    font-weight: 700;
    color: white;
}

.timeline-text {
    color: #aeb6c7;
    line-height: 1.7;
    margin-top: 8px;
}

/* Contact */

.contact-card {
    text-align: center;
    padding: 35px 20px;
    background: rgba(17,23,34,0.8);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 20px;
}

.contact-label {
    color: #8f99ab;
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 8px;
}

.contact-value {
    color: #ffffff;
    font-size: 16px;
    font-weight: 600;
    word-break: break-word;
}

/* Footer */

.footer {
    text-align: center;
    color: #697386;
    padding: 60px 0 20px;
    font-size: 14px;
}

/* Buttons */

.stButton > button {
    border-radius: 10px;
    border: 1px solid rgba(139,124,255,0.35);
    background: #8b7cff;
    color: white;
    font-weight: 600;
    min-height: 42px;
}

.stButton > button:hover {
    border-color: #8b7cff;
    background: #7565ef;
    color: white;
}

/* Inputs */

div[data-baseweb="input"] > div,
div[data-baseweb="textarea"] > div,
div[data-baseweb="select"] > div {
    background-color: #111722;
    border-color: rgba(255,255,255,0.10);
}

label {
    color: #cdd3df !important;
}

/* Mobile */

@media (max-width: 768px) {
    .hero {
        padding-top: 35px;
    }

    .hero-title {
        letter-spacing: -2px;
    }

    .hero-subtitle {
        font-size: 17px;
    }

    .section-title {
        font-size: 28px;
    }
}

</style>
"""
    )

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def section(title, description=""):
    st.html(f'<div class="section-title">{title}</div>')
    st.html('<div class="section-line"></div>')

    if description:
        st.html(
            f'<div class="section-description">{description}</div>'
    )


def save_uploaded_file(uploaded_file, folder_name):
    if uploaded_file is None:
        return ""

    folder = UPLOAD_DIR / folder_name
    folder.mkdir(exist_ok=True)

    file_path = folder / uploaded_file.name

    with open(file_path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    return str(file_path.relative_to(BASE_DIR))


def tags_html(technologies):
    if not technologies:
        return ""

    items = [x.strip() for x in technologies.split(",") if x.strip()]

    return "".join(
        f'<span class="tag">{item}</span>'
        for item in items
    )


# ============================================================
# NAVIGATION
# ============================================================

st.html(
    """
<div class="nav-box">
    <div class="brand">Arthi<span>.</span></div>
</div>
"""
    )

nav_options = [
    "Home",
    "About",
    "Skills",
    "Projects",
    "Education",
    "Experience",
    "Certificates",
    "Achievements",
    "Resume",
    "Contact",
]

selected_page = st.radio(
    "Navigation",
    nav_options,
    horizontal=True,
    label_visibility="collapsed",
)

# ============================================================
# HOME
# ============================================================

if selected_page == "Home":

    st.html(
        """
<div class="hero">

    <div class="hero-small">
        B.Tech AI & Data Science Student
    </div>

    <div class="hero-title">
        Arthi<br>
        <span>Sathishkumar</span>
    </div>

    <div class="hero-subtitle">
        Exploring AI. Building for the Web. Creating with Purpose.
    </div>

    <div class="hero-tagline">
        Interested in Web Development, Artificial Intelligence,
        and Data Science.
    </div>

</div>
"""
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.html(
            """
<div class="card">
    <div class="card-title">AI & Data Science</div>
    <div class="card-text">
        Exploring intelligent technologies, data analysis,
        visualization, and practical AI applications.
    </div>
</div>
"""
    )

    with col2:
        st.html(
            """
<div class="card">
    <div class="card-title">Web Development</div>
    <div class="card-text">
        Building useful digital applications and interactive
        experiences using modern development tools.
    </div>
</div>
"""
    )

    with col3:
        st.html(
            """
<div class="card">
    <div class="card-title">Problem Solving</div>
    <div class="card-text">
        Turning ideas into practical solutions through teamwork,
        creativity, and structured problem solving.
    </div>
</div>
"""
    )

# ============================================================
# ABOUT
# ============================================================

elif selected_page == "About":

    section("About Me")

    st.html(
        """
<div class="card">
    <div class="card-text" style="font-size:17px;">
        I’m <strong style="color:white;">Arthi Sathishkumar</strong>,
        a second-year B.Tech Artificial Intelligence and Data Science
        student with a growing interest in Web Development,
        Artificial Intelligence, and Data Science.
        <br><br>
        I enjoy turning ideas into practical digital solutions and
        exploring how technology can solve real-world problems.
        <br><br>
        Through academic projects, hackathons, and hands-on
        development, I’m continuously building my technical skills
        while learning to approach challenges with creativity and
        problem-solving.
        <br><br>
        I’m particularly interested in creating useful,
        user-focused applications that combine intelligent
        technologies with modern web experiences.
        <br><br>
        I believe every project is an opportunity to learn something
        new, improve my skills, and create something meaningful.
    </div>
</div>
"""
    )

# ============================================================
# SKILLS
# ============================================================

elif selected_page == "Skills":

    section(
        "Skills",
        "Technical and professional skills I currently work with.",
    )

    skill_categories = {
        "Programming": [
            "Python",
            "C",
        ],
        "Data Science": [
            "Pandas",
            "NumPy",
            "Matplotlib",
            "Data Science",
        ],
        "Artificial Intelligence": [
            "Artificial Intelligence",
        ],
        "Tools & Platforms": [
            "Streamlit",
            "Git",
            "GitHub",
            "VS Code",
        ],
        "Soft Skills": [
            "Problem Solving",
            "Teamwork",
            "Leadership",
            "Communication",
            "Creativity",
            "Time Management",
        ],
    }

    cols = st.columns(2)

    for index, (category, skills) in enumerate(skill_categories.items()):

        with cols[index % 2]:

            skill_html = "".join(
                f'<span class="tag">{skill}</span>'
                for skill in skills
            )

            st.html(
                f"""
<div class="skill-box">
    <div class="skill-heading">{category}</div>
    {skill_html}
</div>
"""
    )

# ============================================================
# PROJECTS
# ============================================================

elif selected_page == "Projects":

    section(
        "Projects",
        "A collection of applications and practical projects I have built.",
    )

    for index, project in enumerate(projects):

        if index % 2 == 0:
            col1, col2 = st.columns(2)

        with (col1 if index % 2 == 0 else col2):

            image_path = project.get("image", "")

            if image_path:
                full_image_path = BASE_DIR / image_path

                if full_image_path.exists():
                    st.image(str(full_image_path), use_container_width=True)

            st.html(
                f"""
<div class="card">

    <div class="card-title">
        {project.get("name", "Project")}
    </div>

    <div class="card-text">
        {project.get("description", "")}
    </div>

    <div style="margin-top:15px;">
        {tags_html(project.get("technologies", ""))}
    </div>

</div>
"""
    )

            button_col1, button_col2 = st.columns(2)

            with button_col1:
                if project.get("github"):
                    st.link_button(
                        "GitHub",
                        project["github"],
                        use_container_width=True,
                    )

            with button_col2:
                if project.get("live"):
                    st.link_button(
                        "Live Demo",
                        project["live"],
                        use_container_width=True,
                    )

    st.divider()

    st.subheader("Add New Project")

    with st.form("add_project_form"):

        project_name = st.text_input("Project Name")

        project_description = st.text_area(
            "Project Description"
        )

        project_technologies = st.text_input(
            "Technologies Used",
            placeholder="Python, Streamlit, Pandas",
        )

        project_github = st.text_input(
            "GitHub URL"
        )

        project_live = st.text_input(
            "Live Demo URL"
        )

        project_image = st.file_uploader(
            "Project Image / Screenshot",
            type=["png", "jpg", "jpeg", "webp"],
        )

        submit_project = st.form_submit_button(
            "Add Project",
            use_container_width=True,
        )

        if submit_project:

            if not project_name or not project_description:
                st.error(
                    "Project name and description are required."
                )

            else:

                image_saved = save_uploaded_file(
                    project_image,
                    "projects",
                )

                new_project = {
                    "name": project_name,
                    "description": project_description,
                    "technologies": project_technologies,
                    "github": project_github,
                    "live": project_live,
                    "image": image_saved,
                }

                projects.append(new_project)

                save_json(
                    PROJECTS_FILE,
                    projects,
                )

                st.success(
                    "Project added successfully."
                )

                st.rerun()

# ============================================================
# EDUCATION
# ============================================================

elif selected_page == "Education":

    section("Education")

    st.html(
        """
<div class="timeline-card">

    <div class="timeline-year">
        2026 – Present
    </div>

    <div class="timeline-title">
        B.Tech – Artificial Intelligence and Data Science
    </div>

    <div class="timeline-text">
        Thamirabharani Engineering College (Autonomous),
        Tirunelveli
        <br><br>
        <strong style="color:white;">
            2nd Year – 3rd Semester
        </strong>
        <br><br>
        Semester 1 CGPA: <strong style="color:white;">8.55</strong>
        <br>
        Semester 2 CGPA: <strong style="color:white;">9.00</strong>
        <br>
        Expected Graduation: <strong style="color:white;">2029</strong>
    </div>

</div>
"""
    )

    st.html(
        """
<div class="timeline-card">

    <div class="timeline-year">
        2024 – 2025
    </div>

    <div class="timeline-title">
        Higher Secondary Education
    </div>

    <div class="timeline-text">
        Government Higher Secondary School, Kuttam
        <br><br>
        Percentage:
        <strong style="color:white;">79.5%</strong>
    </div>

</div>
"""
    )

    st.html(
        """
<div class="timeline-card">

    <div class="timeline-year">
        2022 – 2023
    </div>

    <div class="timeline-title">
        Secondary Education
    </div>

    <div class="timeline-text">
        Government Higher Secondary School, Kuttam
        <br><br>
        Percentage:
        <strong style="color:white;">69.4%</strong>
    </div>

</div>
"""
    )

# ============================================================
# EXPERIENCE
# ============================================================

elif selected_page == "Experience":

    section(
        "Experience",
        "Internships and practical experience.",
    )

    for item in experience:

        st.html(
            f"""
<div class="timeline-card">

    <div class="timeline-year">
        {item.get("type", "Experience")}
    </div>

    <div class="timeline-title">
        {item.get("role", "")}
    </div>

    <div style="color:#8b7cff;font-weight:600;margin-top:5px;">
        {item.get("company", "")}
    </div>

    <div class="timeline-text">
        {item.get("description", "")}
        <br><br>
        <strong style="color:white;">
            Skills:
        </strong>
        {item.get("skills", "")}
    </div>

</div>
"""
    )

    st.divider()

    st.subheader("Add Internship / Experience")

    with st.form("experience_form"):

        company = st.text_input("Company Name")

        role = st.text_input(
            "Role / Position"
        )

        experience_type = st.text_input(
            "Internship Type",
            placeholder="Full Stack Internship",
        )

        duration = st.text_input(
            "Duration",
            placeholder="1 Month",
        )

        col1, col2 = st.columns(2)

        with col1:
            start_date = st.date_input(
                "Start Date",
                value=None,
            )

        with col2:
            end_date = st.date_input(
                "End Date",
                value=None,
            )

        description = st.text_area(
            "Description"
        )

        skills = st.text_input(
            "Skills / Technologies",
            placeholder="Python, Node.js, Express",
        )

        website = st.text_input(
            "Company Website"
        )

        certificate = st.file_uploader(
            "Certificate Upload",
            type=["pdf", "png", "jpg", "jpeg"],
        )

        offer_letter = st.file_uploader(
            "Offer Letter Upload",
            type=["pdf", "png", "jpg", "jpeg"],
        )

        submit_experience = st.form_submit_button(
            "Add Experience",
            use_container_width=True,
        )

        if submit_experience:

            if not company or not role:
                st.error(
                    "Company name and role are required."
                )

            else:

                certificate_path = save_uploaded_file(
                    certificate,
                    "certificates",
                )

                offer_letter_path = save_uploaded_file(
                    offer_letter,
                    "offer_letters",
                )

                new_experience = {
                    "company": company,
                    "role": role,
                    "type": experience_type,
                    "duration": duration,
                    "start": str(start_date) if start_date else "",
                    "end": str(end_date) if end_date else "",
                    "description": description,
                    "skills": skills,
                    "website": website,
                    "certificate": certificate_path,
                    "offer_letter": offer_letter_path,
                }

                experience.append(
                    new_experience
                )

                save_json(
                    EXPERIENCE_FILE,
                    experience,
                )

                st.success(
                    "Experience added successfully."
                )

                st.rerun()

# ============================================================
# CERTIFICATES
# ============================================================

elif selected_page == "Certificates":

    section(
        "Certificates",
        "Certificates and learning credentials.",
    )

    for certificate in certificates:

        st.html(
            f"""
<div class="card" style="margin-bottom:20px;">

    <div class="card-title">
        {certificate.get("name", "")}
    </div>

    <div class="card-text">
        Issued by:
        <strong style="color:white;">
            {certificate.get("organization", "")}
        </strong>
        <br>
        {certificate.get("date", "")}
    </div>

</div>
"""
    )

        certificate_file = certificate.get("file", "")

        if certificate_file:

            full_path = BASE_DIR / certificate_file

            if full_path.exists():

                if full_path.suffix.lower() == ".pdf":

                    with open(full_path, "rb") as file:
                        st.download_button(
                            "View / Download Certificate",
                            file,
                            file_name=full_path.name,
                            mime="application/pdf",
                        )

                else:
                    st.image(
                        str(full_path),
                        use_container_width=True,
                    )

        if certificate.get("credential"):
            st.link_button(
                "Credential",
                certificate["credential"],
            )

    st.divider()

    st.subheader("Add Certificate")

    with st.form("certificate_form"):

        certificate_name = st.text_input(
            "Certificate Name"
        )

        organization = st.text_input(
            "Issuing Organization"
        )

        certificate_date = st.date_input(
            "Date",
            value=date.today(),
        )

        certificate_file = st.file_uploader(
            "Certificate Image / PDF",
            type=["pdf", "png", "jpg", "jpeg"],
        )

        credential_url = st.text_input(
            "Credential URL"
        )

        submit_certificate = st.form_submit_button(
            "Add Certificate",
            use_container_width=True,
        )

        if submit_certificate:

            if not certificate_name:
                st.error(
                    "Certificate name is required."
                )

            else:

                certificate_path = save_uploaded_file(
                    certificate_file,
                    "certificates",
                )

                new_certificate = {
                    "name": certificate_name,
                    "organization": organization,
                    "date": str(certificate_date),
                    "file": certificate_path,
                    "credential": credential_url,
                }

                certificates.append(
                    new_certificate
                )

                save_json(
                    CERTIFICATES_FILE,
                    certificates,
                )

                st.success(
                    "Certificate added successfully."
                )

                st.rerun()

# ============================================================
# ACHIEVEMENTS
# ============================================================

elif selected_page == "Achievements":

    section(
        "Achievements & Activities",
        "Hackathons, workshops, seminars, and other activities.",
    )

    for achievement in achievements:

        st.html(
            f"""
<div class="card" style="margin-bottom:20px;">

    <div class="card-title">
        {achievement.get("title", "")}
    </div>

    <div class="card-text">
        {achievement.get("description", "")}
    </div>

</div>
"""
    )

        if achievement.get("link"):
            st.link_button(
                "View Link",
                achievement["link"],
            )

    st.divider()

    st.subheader("Add Achievement")

    with st.form("achievement_form"):

        achievement_title = st.text_input(
            "Achievement Title"
        )

        achievement_description = st.text_area(
            "Description"
        )

        achievement_date = st.date_input(
            "Date",
            value=date.today(),
        )

        proof_file = st.file_uploader(
            "Certificate / Proof Upload",
            type=["pdf", "png", "jpg", "jpeg"],
        )

        achievement_link = st.text_input(
            "Link"
        )

        submit_achievement = st.form_submit_button(
            "Add Achievement",
            use_container_width=True,
        )

        if submit_achievement:

            if not achievement_title:
                st.error(
                    "Achievement title is required."
                )

            else:

                proof_path = save_uploaded_file(
                    proof_file,
                    "achievements",
                )

                new_achievement = {
                    "title": achievement_title,
                    "description": achievement_description,
                    "date": str(achievement_date),
                    "proof": proof_path,
                    "link": achievement_link,
                }

                achievements.append(
                    new_achievement
                )

                save_json(
                    ACHIEVEMENTS_FILE,
                    achievements,
                )

                st.success(
                    "Achievement added successfully."
                )

                st.rerun()

# ============================================================
# RESUME
# ============================================================

elif selected_page == "Resume":

    section(
        "Resume",
        "Download or view my latest resume.",
    )

    resume_path = BASE_DIR / "resume.pdf"

    if resume_path.exists():

        with open(resume_path, "rb") as resume_file:

            st.download_button(
                label="Download Resume",
                data=resume_file,
                file_name="Arthi_Sathishkumar_Resume.pdf",
                mime="application/pdf",
                use_container_width=True,
            )

    else:

        st.info(
            "Resume is not uploaded yet."
        )

        uploaded_resume = st.file_uploader(
            "Upload Resume PDF",
            type=["pdf"],
        )

        if uploaded_resume:

            with open(resume_path, "wb") as file:
                file.write(
                    uploaded_resume.getbuffer()
                )

            st.success(
                "Resume uploaded successfully."
            )

            st.rerun()

# ============================================================
# CONTACT
# ============================================================

elif selected_page == "Contact":

    section(
        "Contact",
        "Feel free to connect with me for opportunities, collaborations, or project discussions.",
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.html(
            """
<div class="contact-card">

    <div class="contact-label">
        Email
    </div>

    <div class="contact-value">
        s.arthi1027@gmail.com
    </div>

</div>
"""
    )

    with col2:

        st.html(
            """
<div class="contact-card">

    <div class="contact-label">
        Phone
    </div>

    <div class="contact-value">
        9363042827
    </div>

</div>
"""
    )

    with col3:

        st.html(
            """
<div class="contact-card">

    <div class="contact-label">
        GitHub
    </div>

    <div class="contact-value">
        ArthiSathishkumar
    </div>

</div>
"""
    )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        st.link_button(
            "GitHub Profile",
            "https://github.com/ArthiSathishkumar",
            use_container_width=True,
        )

    with col2:

        # Replace this URL with your exact LinkedIn profile URL
        st.link_button(
            "LinkedIn Profile",
            "https://www.linkedin.com/",
            use_container_width=True,
        )

# ============================================================
# FOOTER
# ============================================================

st.html(
    """
<div class="footer">
    © 2026 Arthi Sathishkumar · B.Tech Artificial Intelligence & Data Science
</div>
"""
    )