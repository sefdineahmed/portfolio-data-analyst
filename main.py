import streamlit as st
import requests
import json
from datetime import datetime
import time

# Configuration de la page
st.set_page_config(
    page_title="AHMED SEFDINE - Data Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Variables d'API
API_BASE_URL = "http://localhost:5000/api"  # À modifier pour la production

# Style CSS personnalisé
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E3A8A;
        font-weight: 700;
        margin-bottom: 0.5rem;
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
    }
    
    .contact-info {
        background-color: #F0F9FF;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .social-icon {
        font-size: 1.5rem;
        margin-right: 10px;
        color: #3B82F6;
    }
    
    .experience-period {
        color: #6B7280;
        font-style: italic;
        font-size: 0.9rem;
    }
    
    /* Ajout pour éviter les conflits de rendu */
    .stApp {
        overflow-x: hidden;
    }
    
    /* Correction pour les transitions */
    [data-testid="stVerticalBlock"] {
        transition: none !important;
    }
</style>
""", unsafe_allow_html=True)

# Fonctions pour récupérer les données depuis l'API avec retry
@st.cache_data(ttl=3600, show_spinner="Chargement des données...")
def fetch_data(endpoint):
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = requests.get(f"{API_BASE_URL}/{endpoint}", timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1:
                time.sleep(1)
                continue
            st.error(f"Erreur lors de la récupération des données {endpoint}: {e}")
            return None
    return None

# Initialisation de session state pour stocker les données
if 'data_loaded' not in st.session_state:
    st.session_state.data_loaded = False
    st.session_state.profile = None
    st.session_state.education = None
    st.session_state.experience = None
    st.session_state.skills = None

# Chargement des données avec un spinner
with st.spinner("Chargement du portfolio..."):
    if not st.session_state.data_loaded:
        st.session_state.profile = fetch_data("profile")
        st.session_state.education = fetch_data("education")
        st.session_state.experience = fetch_data("experience")
        st.session_state.skills = fetch_data("skills")
        st.session_state.data_loaded = True

# Assignation des variables
profile = st.session_state.profile
education = st.session_state.education
experience = st.session_state.experience
skills = st.session_state.skills

# Sidebar - Utiliser un conteneur pour isoler
with st.sidebar:
    sidebar_container = st.container()
    with sidebar_container:
        # Ajout d'un placeholder pour éviter les conflits
        col_img, _ = st.columns([1, 1])
        with col_img:
            st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
            st.image("https://img.icons8.com/fluency/96/000000/user-male-circle.png", 
                    width=150)
            st.markdown('</div>', unsafe_allow_html=True)
        
        if profile:
            st.markdown(f"## {profile.get('name', 'AHMED SEFDINE')}")
            st.markdown(f"### {profile.get('title', 'Data Analyst')}")
            st.markdown(f"📍 {profile.get('location', 'Dakar, Sénégal')}")
        
        st.markdown("---")
        
        # Informations de contact
        if profile:
            st.markdown("### 📞 Contact")
            st.markdown(f"**Email:** {profile.get('email')}")
            st.markdown(f"**Téléphone:** {profile.get('phone')}")
            
            # Liens sociaux
            st.markdown("### 🔗 Réseaux")
            for link in profile.get('socialLinks', []):
                st.markdown(f"[{link['icon']} {link['platform']}]({link['url']})")
        
        st.markdown("---")
        st.markdown("### 📊 Compétences clés")
        if skills:
            for skill_category in skills[:2]:  # Limiter à 2 catégories dans la sidebar
                st.markdown(f"**{skill_category['category']}**")
                for item in skill_category['items'][:3]:  # Limiter à 3 items par catégorie
                    st.markdown(f"• {item}")

# Contenu principal - Utiliser des conteneurs pour structurer
main_container = st.container()
with main_container:
    # En-tête principal
    if profile:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f'<h1 class="main-header">{profile.get("name")}</h1>', unsafe_allow_html=True)
            st.markdown(f'<h2 class="sub-header">{profile.get("title")}</h2>', unsafe_allow_html=True)
            
            # Bio
            st.markdown("### À propos")
            bio_container = st.container()
            with bio_container:
                st.write(profile.get("bio", ""))
        
        with col2:
            avatar_container = st.container()
            with avatar_container:
                st.image("https://img.icons8.com/fluency/240/000000/user-male-circle.png", 
                        caption="AHMED SEFDINE", width=200)
    
    # Sections principales avec des conteneurs individuels
    tabs_container = st.container()
    with tabs_container:
        # Utiliser st.tabs() seulement une fois
        tab_names = ["📈 Expérience", "🎓 Formation", "🛠️ Compétences", "📂 Projets"]
        tabs = st.tabs(tab_names)
        
        # Onglet Expérience
        with tabs[0]:
            if experience:
                exp_container = st.container()
                with exp_container:
                    st.markdown('<h2 class="section-title">Expérience Professionnelle</h2>', unsafe_allow_html=True)
                    
                    for exp in experience:
                        exp_item = st.container()
                        with exp_item:
                            col1, col2 = st.columns([3, 1])
                            with col1:
                                st.markdown(f"### {exp['title']}")
                                st.markdown(f"**{exp['company']}** - {exp['location']}")
                                
                                # Description sous forme de liste
                                for desc in exp['description']:
                                    st.markdown(f"• {desc}")
                            
                            with col2:
                                st.markdown(f'<p class="experience-period">{exp["period"]}</p>', unsafe_allow_html=True)
                            
                            st.markdown("---")
        
        # Onglet Formation
        with tabs[1]:
            if education:
                edu_container = st.container()
                with edu_container:
                    st.markdown('<h2 class="section-title">Formation Académique</h2>', unsafe_allow_html=True)
                    
                    for edu in education:
                        edu_item = st.container()
                        with edu_item:
                            st.markdown(f"""
                            <div class="card">
                                <h3>{edu['degree']}</h3>
                                <p><strong>{edu['institution']}</strong> - {edu['location']}</p>
                                <p><em>{edu['period']}</em></p>
                            </div>
                            """, unsafe_allow_html=True)
        
        # Onglet Compétences
        with tabs[2]:
            if skills:
                skills_container = st.container()
                with skills_container:
                    st.markdown('<h2 class="section-title">Compétences Techniques</h2>', unsafe_allow_html=True)
                    
                    # Utiliser des colonnes stables
                    cols = st.columns(2)
                    for idx, skill_category in enumerate(skills):
                        with cols[idx % 2]:
                            cat_container = st.container()
                            with cat_container:
                                st.markdown(f"""
                                <div class="skill-category">
                                    <h4>{skill_category['category']}</h4>
                                </div>
                                """, unsafe_allow_html=True)
                                
                                for item in skill_category['items']:
                                    st.markdown(f"• **{item}**")
        
        # Onglet Projets
        with tabs[3]:
            projets_container = st.container()
            with projets_container:
                st.markdown('<h2 class="section-title">Projets Data Analysis</h2>', unsafe_allow_html=True)
                
                # Exemples de projets
                projets = [
                    {
                        "titre": "Analyse de Survie - Cancer de l'Estomac",
                        "description": "Modélisation statistique de la survie des patients avec Kaplan-Meier, Cox et Random Survival Forest",
                        "technologies": ["Python", "scikit-survival", "pandas", "matplotlib"],
                        "periode": "2024-2025"
                    },
                    {
                        "titre": "Dashboard Business Intelligence - Trafic Aérien",
                        "description": "Visualisation des indicateurs clés du trafic aérien sur 12 ans",
                        "technologies": ["Power BI", "SQL", "Excel"],
                        "periode": "2019"
                    },
                    {
                        "titre": "Système de Suivi des Indices des Prix",
                        "description": "Collecte et analyse des données d'inflation pour rapports trimestriels",
                        "technologies": ["Python", "SQL", "KoboToolbox", "Talend"],
                        "periode": "2021"
                    }
                ]
                
                for projet in projets:
                    with st.expander(f"{projet['titre']} ({projet['periode']})"):
                        st.markdown(f"**Description:** {projet['description']}")
                        st.markdown("**Technologies utilisées:**")
                        # Utiliser st.columns de manière stable
                        tech_text = " ".join([f"`{tech}` " for tech in projet['technologies']])
                        st.markdown(tech_text)

# Section de contact
contact_container = st.container()
with contact_container:
    st.markdown("---")
    st.markdown('<h2 class="section-title">Contactez-moi</h2>', unsafe_allow_html=True)
    
    if profile:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            contact_item = st.container()
            with contact_item:
                st.markdown("""
                <div class="contact-info">
                    <h4>📧 Email</h4>
                    <p>{email}</p>
                </div>
                """.format(email=profile.get('email')), unsafe_allow_html=True)
        
        with col2:
            contact_item = st.container()
            with contact_item:
                st.markdown("""
                <div class="contact-info">
                    <h4>📱 Téléphone</h4>
                    <p>{phone}</p>
                </div>
                """.format(phone=profile.get('phone')), unsafe_allow_html=True)
        
        with col3:
            contact_item = st.container()
            with contact_item:
                st.markdown("""
                <div class="contact-info">
                    <h4>📍 Localisation</h4>
                    <p>{location}</p>
                </div>
                """.format(location=profile.get('location')), unsafe_allow_html=True)

# Pied de page
footer_container = st.container()
with footer_container:
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #6B7280; padding: 2rem;">
        <p>© 2024 AHMED SEFDINE - Portfolio Data Analyst</p>
        <p>Dernière mise à jour : {date}</p>
    </div>
    """.format(date=datetime.now().strftime("%d/%m/%Y")), unsafe_allow_html=True)

# Ajout d'un script JavaScript pour stabiliser le DOM
st.markdown("""
<script>
    // Prévenir les conflits de rendu
    document.addEventListener('DOMContentLoaded', function() {
        // Désactiver les transitions problématiques
        const style = document.createElement('style');
        style.textContent = `
            * {
                transition: none !important;
                animation: none !important;
            }
        `;
        document.head.appendChild(style);
    });
</script>
""", unsafe_allow_html=True)

# Message de débogage (optionnel - à désactiver en production)
# st.sidebar.markdown("---")
# st.sidebar.markdown("**État de l'application:**")
# st.sidebar.markdown(f"Données chargées: {st.session_state.data_loaded}")
