import streamlit as st
import requests
import json
from datetime import datetime
import pandas as pd

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
</style>
""", unsafe_allow_html=True)

# Fonctions pour récupérer les données depuis l'API
@st.cache_data(ttl=3600)  # Cache pour 1 heure
def fetch_data(endpoint):
    try:
        response = requests.get(f"{API_BASE_URL}/{endpoint}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Erreur lors de la récupération des données: {e}")
        return None

# Chargement des données
profile = fetch_data("profile")
education = fetch_data("education")
experience = fetch_data("experience")
skills = fetch_data("skills")

# Sidebar
with st.sidebar:
    st.image("https://via.placeholder.com/150x150/3B82F6/FFFFFF?text=AS", width=150)
    
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
        social_html = ""
        for link in profile.get('socialLinks', []):
            social_html += f'<a href="{link["url"]}" target="_blank" class="social-icon">{link["icon"]} {link["platform"]}</a><br>'
        st.markdown(social_html, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 📊 Compétences clés")
    if skills:
        for skill_category in skills:
            st.markdown(f"**{skill_category['category']}**")
            for item in skill_category['items']:
                st.markdown(f"• {item}")

# En-tête principal
if profile:
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f'<h1 class="main-header">{profile.get("name")}</h1>', unsafe_allow_html=True)
        st.markdown(f'<h2 class="sub-header">{profile.get("title")}</h2>', unsafe_allow_html=True)
        
        # Bio
        st.markdown("### À propos")
        st.info(profile.get("bio", ""))
    
    with col2:
        st.image("https://via.placeholder.com/200x200/3B82F6/FFFFFF?text=Photo+Pro", 
                caption="AHMED SEFDINE", width=200)

# Sections principales
tabs = st.tabs(["📈 Expérience", "🎓 Formation", "🛠️ Compétences", "📂 Projets"])

# Onglet Expérience
with tabs[0]:
    if experience:
        st.markdown('<h2 class="section-title">Expérience Professionnelle</h2>', unsafe_allow_html=True)
        
        for exp in experience:
            with st.container():
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
        st.markdown('<h2 class="section-title">Formation Académique</h2>', unsafe_allow_html=True)
        
        for edu in education:
            with st.container():
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
        st.markdown('<h2 class="section-title">Compétences Techniques</h2>', unsafe_allow_html=True)
        
        cols = st.columns(2)
        for idx, skill_category in enumerate(skills):
            with cols[idx % 2]:
                st.markdown(f"""
                <div class="skill-category">
                    <h4>{skill_category['category']}</h4>
                    <ul>
                """, unsafe_allow_html=True)
                
                for item in skill_category['items']:
                    st.markdown(f"• **{item}**")
                
                st.markdown("</ul></div>", unsafe_allow_html=True)

# Onglet Projets
with tabs[3]:
    st.markdown('<h2 class="section-title">Projets Data Analysis</h2>', unsafe_allow_html=True)
    
    # Exemples de projets (à remplacer par vos projets réels)
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
            tech_cols = st.columns(4)
            for idx, tech in enumerate(projet['technologies']):
                tech_cols[idx % 4].markdown(f"`{tech}`")

# Section de contact
st.markdown("---")
st.markdown('<h2 class="section-title">Contactez-moi</h2>', unsafe_allow_html=True)

if profile:
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="contact-info">
            <h4>📧 Email</h4>
            <p>{email}</p>
        </div>
        """.format(email=profile.get('email')), unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="contact-info">
            <h4>📱 Téléphone</h4>
            <p>{phone}</p>
        </div>
        """.format(phone=profile.get('phone')), unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="contact-info">
            <h4>📍 Localisation</h4>
            <p>{location}</p>
        </div>
        """.format(location=profile.get('location')), unsafe_allow_html=True)

# Pied de page
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6B7280; padding: 2rem;">
    <p>© 2024 AHMED SEFDINE - Portfolio Data Analyst</p>
    <p>Dernière mise à jour : {date}</p>
</div>
""".format(date=datetime.now().strftime("%d/%m/%Y")), unsafe_allow_html=True)
