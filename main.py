import streamlit as st
from datetime import datetime
import json

# Configuration de la page
st.set_page_config(
    page_title="AHMED SEFDINE - Data Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Données statiques du profil
PROFILE_DATA = {
    "id": 1,
    "name": "AHMED SEFDINE",
    "title": "Data Analyst",
    "bio": "Jeune diplômé en statistique et informatique décisionnelle, avec une expérience en analyse de données, statistiques appliquées, SQL et Business Intelligence. Compétences en Python, Power BI et reporting décisionnel. Intéressé par des postes de Data Analyst / BI Junior.",
    "email": "ahmed.sefdine@uadb.edu.sn",
    "phone": "+221 77 808 09 42",
    "location": "Dakar, Sénégal",
    "socialLinks": [
        {"url": "https://www.linkedin.com/in/sefdineahmed/", "icon": "🔗", "platform": "LinkedIn"},
        {"url": "https://github.com/sefdineahmed", "icon": "💻", "platform": "GitHub"}
    ],
    "avatarUrl": None
}

EDUCATION_DATA = [
    {
        "id": 4,
        "degree": "Baccalauréat Scientifique (TD)",
        "institution": "École Privée Communautaire Franco Arabe de Dimani",
        "location": "Ntsoralé, Comores",
        "period": "2016 – 2017"
    },
    {
        "id": 3,
        "degree": "Diplôme Universitaire de Technologie, Statistique",
        "institution": "Université des Comores",
        "location": "Moroni, Comores",
        "period": "2017 – 2019"
    },
    {
        "id": 2,
        "degree": "Licence Pro, Mathématique, Statistique et Informatique Décisionnelle",
        "institution": "Université des Comores",
        "location": "Moroni, Comores",
        "period": "2019 – 2020"
    },
    {
        "id": 1,
        "degree": "Master II, Statistique et informatique décisionnelle",
        "institution": "Université Alioune Diop",
        "location": "Bambey, Sénégal",
        "period": "2022 – 2025"
    }
]

EXPERIENCE_DATA = [
    {
        "id": 4,
        "title": "Analyste de Données Aériennes (Stage)",
        "company": "Agence Nationale de l'Aviation Civile et de la Météorologie",
        "location": "Moroni, Comores",
        "period": "juil. 2019 – sept. 2019",
        "description": [
            "Analyse descriptive du trafic aérien (2005–2017)",
            "Visualisation et synthèse des indicateurs clés"
        ]
    },
    {
        "id": 3,
        "title": "Assistant Statistique (Stage)",
        "company": "Institut National de Statistique des Études Économiques et Démographiques",
        "location": "Moroni, Comores",
        "period": "mai 2021 – déc. 2021",
        "description": [
            "Collecte, traitement et analyse des données relatives aux indices des prix",
            "Rédaction de rapports trimestriels et présentation des résultats",
            "Participation à l'amélioration des méthodologies de collecte"
        ]
    },
    {
        "id": 2,
        "title": "Data Analyst - Modélisation de Survie (Stage)",
        "company": "Hôpital Aristide Le Dantec",
        "location": "Dakar, Sénégal",
        "period": "déc. 2024 – avr. 2025",
        "description": [
            "Analyse de survie sur des données de patients atteints de cancer de l'estomac",
            "Modélisation statistique (Kaplan-Meier, Cox)",
            "Implémentation de modèles ML (Random Survival Forest, Deep Survival)",
            "Comparaison des performances et aide à la décision"
        ]
    },
    {
        "id": 1,
        "title": "Analyste de Données Junior (Stage)",
        "company": "Agence Nationale de Statistique et Démographique",
        "location": "Diourbel, Sénégal",
        "period": "oct. 2025 – aujourd'hui",
        "description": [
            "Collecte, nettoyage et traitement de données économiques et sociales",
            "Contribution à la rédaction du Rapport sur la Situation Économique et Sociale 2024",
            "Centralisation et consolidation des données issues des services sectoriels",
            "Mise à jour de maquettes statistiques"
        ]
    }
]

SKILLS_DATA = [
    {
        "id": 1,
        "category": "Languages & Tools",
        "items": [
            "Python (pandas, numpy, matplotlib, seaborn, scikit-learn)",
            "SQL (PostgreSQL, MySQL)",
            "Power BI",
            "KoboToolbox",
            "Talend Open Studio (ETL)",
            "LaTeX",
            "SPSS",
            "Excel",
            "Access"
        ]
    },
    {
        "id": 2,
        "category": "Data & Analysis",
        "items": [
            "Data Cleaning",
            "Statistical Modeling",
            "Machine Learning",
            "Reporting",
            "Business Intelligence",
            "KPIs"
        ]
    },
    {
        "id": 3,
        "category": "Soft Skills",
        "items": [
            "Curiosité Intellectuelle",
            "Résolution de Problème",
            "Sens Produit",
            "Communication"
        ]
    },
    {
        "id": 4,
        "category": "Languages",
        "items": [
            "Français (Courant)",
            "Anglais (Intermédiaire)"
        ]
    }
]

PROJECTS_DATA = [
    {
        "titre": "Analyse de Survie - Cancer de l'Estomac",
        "description": "Modélisation statistique de la survie des patients avec Kaplan-Meier, Cox et Random Survival Forest",
        "technologies": ["Python", "scikit-survival", "pandas", "matplotlib", "seaborn"],
        "periode": "2024-2025",
        "details": "Analyse de données médicales pour prédire la survie des patients et identifier les facteurs de risque significatifs."
    },
    {
        "titre": "Dashboard Business Intelligence - Trafic Aérien",
        "description": "Visualisation des indicateurs clés du trafic aérien sur 12 ans",
        "technologies": ["Power BI", "SQL", "Excel"],
        "periode": "2019",
        "details": "Création d'un tableau de bord interactif pour l'analyse du trafic aérien et la prise de décision stratégique."
    },
    {
        "titre": "Système de Suivi des Indices des Prix",
        "description": "Collecte et analyse des données d'inflation pour rapports trimestriels",
        "technologies": ["Python", "SQL", "KoboToolbox", "Talend"],
        "periode": "2021",
        "details": "Automatisation du processus de collecte et d'analyse des données des indices des prix à la consommation."
    }
]

# Style CSS personnalisé
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E3A8A;
        font-weight: 700;
        margin-bottom: 0.5rem;
        padding-top: 1rem;
    }
    
    .sub-header {
        font-size: 1.5rem;
        color: #3B82F6;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    .section-title {
        font-size: 1.8rem;
        color: #1E3A8A;
        border-bottom: 3px solid #3B82F6;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
        margin-bottom: 1.5rem;
    }
    
    .card {
        background-color: #F8FAFC;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-left: 5px solid #3B82F6;
    }
    
    .skill-category {
        background-color: #EFF6FF;
        border-radius: 8px;
        padding: 1rem;
        margin-bottom: 1rem;
        border: 1px solid #DBEAFE;
    }
    
    .contact-info {
        background-color: #F0F9FF;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        text-align: center;
        border: 1px solid #BAE6FD;
    }
    
    .social-link {
        display: inline-block;
        background-color: #3B82F6;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        margin: 0.5rem;
        text-decoration: none;
        transition: background-color 0.3s;
    }
    
    .social-link:hover {
        background-color: #2563EB;
        color: white;
        text-decoration: none;
    }
    
    .experience-period {
        color: #6B7280;
        font-style: italic;
        font-size: 0.9rem;
        background-color: #F3F4F6;
        padding: 0.3rem 0.6rem;
        border-radius: 4px;
        display: inline-block;
    }
    
    .tech-badge {
        display: inline-block;
        background-color: #E0F2FE;
        color: #0369A1;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        margin: 0.2rem;
        font-size: 0.9rem;
        font-weight: 500;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #F8FAFC;
        border-radius: 5px 5px 0px 0px;
        gap: 1rem;
        padding: 10px 16px;
    }
    
    .download-btn {
        background-color: #10B981;
        color: white;
        padding: 0.5rem 1.5rem;
        border-radius: 5px;
        border: none;
        cursor: pointer;
        font-weight: 600;
        margin-top: 1rem;
    }
    
    .download-btn:hover {
        background-color: #059669;
    }
</style>
""", unsafe_allow_html=True)

# Initialisation de session state
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = "Accueil"

# Fonction pour générer un CV PDF (simulé)
def generate_cv_pdf():
    # Cette fonction simule la génération d'un CV PDF
    # En production, vous pourriez utiliser ReportLab ou WeasyPrint
    st.success("✅ CV généré avec succès! (Fonctionnalité de téléchargement)")
    
    # Créer un faux PDF (texte pour l'exemple)
    cv_content = f"""
    CV - {PROFILE_DATA['name']}
    =============================
    
    Titre: {PROFILE_DATA['title']}
    Email: {PROFILE_DATA['email']}
    Téléphone: {PROFILE_DATA['phone']}
    Localisation: {PROFILE_DATA['location']}
    
    PROFIL
    ------
    {PROFILE_DATA['bio']}
    
    EXPÉRIENCE PROFESSIONNELLE
    --------------------------
    """
    
    for exp in EXPERIENCE_DATA:
        cv_content += f"""
    {exp['title']}
    {exp['company']} - {exp['location']} ({exp['period']})
    """
        for desc in exp['description']:
            cv_content += f"    • {desc}\n"
    
    return cv_content

# Sidebar
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 1rem 0;">
        <div style="background: linear-gradient(135deg, #3B82F6, #1D4ED8); 
                    width: 150px; 
                    height: 150px; 
                    border-radius: 50%; 
                    margin: 0 auto 1rem auto;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 3rem;
                    color: white;">
            AS
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"## {PROFILE_DATA['name']}")
    st.markdown(f"### {PROFILE_DATA['title']}")
    st.markdown(f"📍 **{PROFILE_DATA['location']}**")
    
    st.markdown("---")
    
    # Téléchargement CV
    st.markdown("### 📄 Télécharger CV")
    if st.button("📥 Télécharger mon CV", use_container_width=True):
        cv_content = generate_cv_pdf()
        st.download_button(
            label="⬇️ Cliquer pour télécharger",
            data=cv_content,
            file_name="CV_AHMED_SEFDINE_Data_Analyst.pdf",
            mime="application/pdf"
        )
    
    st.markdown("---")
    
    # Liens sociaux
    st.markdown("### 🌐 Me suivre")
    for link in PROFILE_DATA['socialLinks']:
        st.markdown(f"""
        <a href="{link['url']}" target="_blank" class="social-link">
            {link['icon']} {link['platform']}
        </a>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Compétences clés (résumé)
    st.markdown("### 💡 Compétences clés")
    key_skills = [
        "Python & Data Science",
        "SQL & Databases", 
        "Power BI & DataViz",
        "Statistical Analysis",
        "Machine Learning",
        "Business Intelligence"
    ]
    
    for skill in key_skills:
        st.markdown(f"✅ **{skill}**")

# Contenu principal
# En-tête
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown(f'<h1 class="main-header">{PROFILE_DATA["name"]}</h1>', unsafe_allow_html=True)
    st.markdown(f'<h2 class="sub-header">{PROFILE_DATA["title"]}</h2>', unsafe_allow_html=True)
    
    # Bio
    st.markdown("### 👋 À propos de moi")
    st.markdown(f'<div class="card">{PROFILE_DATA["bio"]}</div>', unsafe_allow_html=True)

with col2:
    # Badge de disponibilité
    st.markdown("""
    <div style="background: linear-gradient(135deg, #10B981, #059669); 
                color: white; 
                padding: 1rem; 
                border-radius: 10px; 
                text-align: center;
                margin-top: 2rem;">
        <h3 style="margin: 0;">📅 Disponible</h3>
        <p style="margin: 0.5rem 0 0 0;">Pour des opportunités en Data Analysis</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Contact rapide
    st.markdown("""
    <div style="margin-top: 2rem;">
        <h4>📬 Contact rapide</h4>
        <p><strong>Email:</strong><br>{email}</p>
        <p><strong>Téléphone:</strong><br>{phone}</p>
    </div>
    """.format(email=PROFILE_DATA['email'], phone=PROFILE_DATA['phone']), unsafe_allow_html=True)

# Navigation par onglets
st.markdown("---")
tab1, tab2, tab3, tab4 = st.tabs(["📊 Expérience", "🎓 Formation", "🛠️ Compétences", "🚀 Projets"])

# Onglet 1: Expérience
with tab1:
    st.markdown('<h2 class="section-title">Expérience Professionnelle</h2>', unsafe_allow_html=True)
    
    for exp in EXPERIENCE_DATA:
        with st.container():
            col1, col2 = st.columns([4, 1])
            with col1:
                st.markdown(f"### {exp['title']}")
                st.markdown(f"**🏢 {exp['company']}** • 📍 {exp['location']}")
                
                # Description
                for desc in exp['description']:
                    st.markdown(f"• {desc}")
            
            with col2:
                st.markdown(f'<div class="experience-period">{exp["period"]}</div>', unsafe_allow_html=True)
            
            st.markdown("---")

# Onglet 2: Formation
with tab2:
    st.markdown('<h2 class="section-title">Parcours Académique</h2>', unsafe_allow_html=True)
    
    for edu in EDUCATION_DATA:
        with st.container():
            st.markdown(f"""
            <div class="card">
                <h3>🎓 {edu['degree']}</h3>
                <p><strong>🏛️ {edu['institution']}</strong></p>
                <p>📍 {edu['location']}</p>
                <p><em>📅 {edu['period']}</em></p>
            </div>
            """, unsafe_allow_html=True)

# Onglet 3: Compétences
with tab3:
    st.markdown('<h2 class="section-title">Compétences Techniques</h2>', unsafe_allow_html=True)
    
    cols = st.columns(2)
    
    with cols[0]:
        for skill_cat in SKILLS_DATA[:2]:  # Languages & Tools, Data & Analysis
            st.markdown(f"""
            <div class="skill-category">
                <h4>🔧 {skill_cat['category']}</h4>
            </div>
            """, unsafe_allow_html=True)
            for item in skill_cat['items']:
                st.markdown(f"• **{item}**")
    
    with cols[1]:
        for skill_cat in SKILLS_DATA[2:]:  # Soft Skills, Languages
            st.markdown(f"""
            <div class="skill-category">
                <h4>🌟 {skill_cat['category']}</h4>
            </div>
            """, unsafe_allow_html=True)
            for item in skill_cat['items']:
                st.markdown(f"• **{item}**")
    
    # Graphique des compétences (simulé)
    st.markdown("### 📈 Niveau de compétences")
    skills_chart = {
        "Python Data Science": 90,
        "SQL & Bases de données": 85,
        "Power BI & DataViz": 80,
        "Statistiques": 85,
        "Machine Learning": 75,
        "Business Intelligence": 80
    }
    
    for skill, level in skills_chart.items():
        st.markdown(f"**{skill}**")
        st.progress(level/100)
        st.markdown(f"{level}%")

# Onglet 4: Projets
with tab4:
    st.markdown('<h2 class="section-title">Projets Data Analysis</h2>', unsafe_allow_html=True)
    
    for projet in PROJECTS_DATA:
        with st.expander(f"**{projet['titre']}** ({projet['periode']})", expanded=False):
            st.markdown(f"**Description:** {projet['description']}")
            st.markdown(f"**Détails:** {projet['details']}")
            
            st.markdown("**Technologies utilisées:**")
            col_techs = st.columns(4)
            for idx, tech in enumerate(projet['technologies']):
                with col_techs[idx % 4]:
                    st.markdown(f'<span class="tech-badge">{tech}</span>', unsafe_allow_html=True)

# Section Contact
st.markdown("---")
st.markdown('<h2 class="section-title">📬 Contactez-moi</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="contact-info">
        <h3>📧 Email</h3>
        <p>{PROFILE_DATA['email']}</p>
        <a href="mailto:{PROFILE_DATA['email']}" class="social-link" style="margin-top: 1rem;">
            ✉️ Envoyer un email
        </a>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="contact-info">
        <h3>📱 Téléphone</h3>
        <p>{PROFILE_DATA['phone']}</p>
        <a href="tel:{PROFILE_DATA['phone'].replace(' ', '')}" class="social-link" style="margin-top: 1rem;">
            📞 Appeler
        </a>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="contact-info">
        <h3>📍 Localisation</h3>
        <p>{PROFILE_DATA['location']}</p>
        <p style="margin-top: 1rem;">🌍 Ouvert aux opportunités à distance</p>
    </div>
    """, unsafe_allow_html=True)

# Formulaire de contact
st.markdown("### 💬 Envoyez-moi un message")
contact_form = """
<form action="https://formspree.io/f/{votre-form-id}" method="POST">
    <input type="hidden" name="_subject" value="Nouveau contact depuis le portfolio">
    <input type="text" name="name" placeholder="Votre nom" required style="width: 100%; padding: 10px; margin: 5px 0; border-radius: 5px; border: 1px solid #ccc;">
    <input type="email" name="email" placeholder="Votre email" required style="width: 100%; padding: 10px; margin: 5px 0; border-radius: 5px; border: 1px solid #ccc;">
    <textarea name="message" placeholder="Votre message" rows="4" required style="width: 100%; padding: 10px; margin: 5px 0; border-radius: 5px; border: 1px solid #ccc;"></textarea>
    <button type="submit" style="background-color: #3B82F6; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">Envoyer</button>
</form>
"""

# Pied de page
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: #6B7280; padding: 2rem;">
    <p>© {datetime.now().year} {PROFILE_DATA['name']} - Portfolio Data Analyst</p>
    <p>Dernière mise à jour : {datetime.now().strftime("%d/%m/%Y")}</p>
    <p style="font-size: 0.9rem; margin-top: 1rem;">📊 Passionné par la data, les statistiques et l'analyse décisionnelle</p>
</div>
""", unsafe_allow_html=True)
