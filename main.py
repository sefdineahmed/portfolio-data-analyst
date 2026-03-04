import streamlit as st
from datetime import datetime
import math

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Ahmed Sefdine · BI Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ─────────────────────────────────────────────
# DATA
# ─────────────────────────────────────────────
PROFILE = {
    "name": "Ahmed Sefdine",
    "title": "Business Intelligence Analyst Junior",
    "tagline": "Transformer la donnée brute en décisions éclairées.",
    "bio": (
        "Jeune diplômé passionné par l'analyse de données, la statistique appliquée "
        "et la Business Intelligence. Fort d'expériences variées en environnements "
        "académiques, institutionnels et médicaux, je maîtrise l'ensemble de la chaîne "
        "analytique — de la collecte à la visualisation — avec des outils comme Python, "
        "SQL, Power BI et Talend. Je cherche à apporter de la valeur dans un poste "
        "BI Analyst / Data Analyst Junior."
    ),
    "email": "ahmed.sefdine@uadb.edu.sn",
    "phone": "+221 77 808 09 42",
    "location": "Dakar, Sénégal",
    "linkedin": "https://www.linkedin.com/in/sefdineahmed/",
    "github": "https://github.com/sefdineahmed",
    "disponible": True,
}

EXPERIENCES = [
    {
        "titre": "Analyste de Données Junior (Stage en cours)",
        "entreprise": "Agence Nationale de Statistique et Démographique",
        "lieu": "Diourbel, Sénégal",
        "periode": "Oct. 2025 – Aujourd'hui",
        "icone": "🏛️",
        "couleur": "#0EA5E9",
        "points": [
            "Collecte, nettoyage et traitement de données économiques et sociales",
            "Contribution à la rédaction du Rapport sur la Situation Économique et Sociale 2024",
            "Centralisation et consolidation des données issues des services sectoriels",
            "Mise à jour et maintenance de maquettes statistiques",
        ],
    },
    {
        "titre": "Data Analyst – Modélisation de Survie (Stage)",
        "entreprise": "Hôpital Aristide Le Dantec",
        "lieu": "Dakar, Sénégal",
        "periode": "Déc. 2024 – Avr. 2025",
        "icone": "🏥",
        "couleur": "#10B981",
        "points": [
            "Analyse de survie sur données patients atteints de cancer de l'estomac",
            "Modélisation statistique : Kaplan-Meier, modèle de Cox proportionnel",
            "Implémentation ML : Random Survival Forest, Deep Survival Networks",
            "Comparaison de performances et aide à la décision clinique",
        ],
    },
    {
        "titre": "Assistant Statistique (Stage)",
        "entreprise": "Institut National de Statistique (INSEED)",
        "lieu": "Moroni, Comores",
        "periode": "Mai 2021 – Déc. 2021",
        "icone": "📈",
        "couleur": "#8B5CF6",
        "points": [
            "Collecte, traitement et analyse des indices des prix à la consommation",
            "Rédaction de rapports trimestriels et présentation des résultats",
            "Participation à l'amélioration des méthodologies de collecte terrain",
        ],
    },
    {
        "titre": "Analyste de Données Aériennes (Stage)",
        "entreprise": "Agence Nationale de l'Aviation Civile et de la Météorologie",
        "lieu": "Moroni, Comores",
        "periode": "Juil. 2019 – Sept. 2019",
        "icone": "✈️",
        "couleur": "#F59E0B",
        "points": [
            "Analyse descriptive du trafic aérien sur la période 2005–2017",
            "Création de visualisations et synthèse des indicateurs clés de performance",
        ],
    },
]

FORMATIONS = [
    {
        "diplome": "Master II – Statistique et Informatique Décisionnelle",
        "institution": "Université Alioune Diop",
        "lieu": "Bambey, Sénégal",
        "periode": "2022 – 2025",
        "niveau": 5,
    },
    {
        "diplome": "Licence Pro – Mathématiques, Statistique & Informatique Décisionnelle",
        "institution": "Université des Comores",
        "lieu": "Moroni, Comores",
        "periode": "2019 – 2020",
        "niveau": 4,
    },
    {
        "diplome": "DUT – Statistique",
        "institution": "Université des Comores",
        "lieu": "Moroni, Comores",
        "periode": "2017 – 2019",
        "niveau": 3,
    },
    {
        "diplome": "Baccalauréat Scientifique (TD)",
        "institution": "École Franco-Arabe de Dimani",
        "lieu": "Ntsoralé, Comores",
        "periode": "2016 – 2017",
        "niveau": 2,
    },
]

COMPETENCES = {
    "BI & Visualisation": [
        ("Power BI", 85, "#F2C811"),
        ("Tableau (notions)", 55, "#E97627"),
        ("Matplotlib / Seaborn", 88, "#11A1FD"),
        ("Excel avancé", 90, "#1D6F42"),
    ],
    "Langages & Données": [
        ("Python (pandas, numpy, sklearn)", 90, "#3776AB"),
        ("SQL (PostgreSQL, MySQL)", 85, "#336791"),
        ("R (notions)", 55, "#276DC3"),
        ("LaTeX", 80, "#008080"),
    ],
    "Data Engineering & ETL": [
        ("Talend Open Studio", 75, "#FF6D00"),
        ("KoboToolbox", 80, "#23B5D3"),
        ("Access & SGBD", 70, "#A4373A"),
    ],
    "Statistiques & ML": [
        ("Modèles de survie", 85, "#10B981"),
        ("Machine Learning supervisé", 75, "#8B5CF6"),
        ("Statistiques descriptives / inférentielles", 90, "#0EA5E9"),
        ("SPSS", 75, "#005C7B"),
    ],
}

PROJETS = [
    {
        "titre": "Analyse de Survie – Cancer de l'Estomac",
        "periode": "2024 – 2025",
        "tags": ["Python", "scikit-survival", "Kaplan-Meier", "Random Forest", "Deep Learning"],
        "desc": (
            "Modélisation complète de la survie de patients atteints de cancer de l'estomac. "
            "Comparaison de méthodes classiques (Cox, Kaplan-Meier) et ML (RSF, DeepSurv). "
            "Identification des facteurs de risque significatifs pour aide à la décision clinique."
        ),
        "icone": "🔬",
        "impact": "Précision prédictive > 78% (C-index)",
    },
    {
        "titre": "Dashboard BI – Trafic Aérien Comorien",
        "periode": "2019",
        "tags": ["Power BI", "SQL", "Excel", "DAX"],
        "desc": (
            "Conception d'un tableau de bord interactif analysant 12 ans de données du trafic aérien. "
            "KPIs dynamiques, segmentation par routes et périodes, filtres temporels et géographiques. "
            "Outil de pilotage stratégique pour la direction de l'ANACM."
        ),
        "icone": "✈️",
        "impact": "12 ans de données · KPIs temps réel",
    },
    {
        "titre": "Pipeline ETL – Indices des Prix à la Consommation",
        "periode": "2021",
        "tags": ["Python", "Talend", "SQL", "KoboToolbox"],
        "desc": (
            "Automatisation de la collecte et du traitement des données IPC. "
            "Mise en place d'un pipeline ETL avec Talend Open Studio pour centraliser "
            "les données terrain et alimenter des rapports trimestriels standardisés."
        ),
        "icone": "⚙️",
        "impact": "Réduction de 60% du temps de traitement",
    },
    {
        "titre": "Rapport RSES 2024 – Analyse Économique & Sociale",
        "periode": "2025",
        "tags": ["Python", "Excel", "Power BI", "Reporting institutionnel"],
        "desc": (
            "Contribution au Rapport sur la Situation Économique et Sociale du Sénégal 2024. "
            "Collecte multi-sources, nettoyage, consolidation des données sectorielles "
            "et rédaction de synthèses analytiques pour publication nationale."
        ),
        "icone": "📋",
        "impact": "Publication nationale officielle",
    },
]

LANGUES = [
    ("Français", 95, "Courant – professionnel"),
    ("Arabe", 80, "Langue maternelle"),
    ("Anglais", 60, "Intermédiaire – technique"),
    ("Shingazidja", 100, "Langue maternelle"),
]

# ─────────────────────────────────────────────
# CSS GLOBAL
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

/* ── Reset & Base ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"] {
    background: #07090F !important;
    color: #E8EAF0 !important;
    font-family: 'DM Sans', sans-serif !important;
}

[data-testid="stAppViewContainer"] { background: #07090F !important; }
[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stSidebar"] { display: none !important; }
section[data-testid="stSidebar"] { display: none !important; }

/* remove streamlit default padding */
.block-container { padding: 0 !important; max-width: 100% !important; }
.stMarkdown { width: 100%; }

/* ── HERO ── */
.hero-wrap {
    background: linear-gradient(135deg, #07090F 0%, #0D1117 40%, #101827 100%);
    border-bottom: 1px solid rgba(14,165,233,0.15);
    padding: 5rem 6rem 4rem;
    position: relative;
    overflow: hidden;
}
.hero-wrap::before {
    content: '';
    position: absolute; inset: 0;
    background:
        radial-gradient(ellipse 80% 60% at 70% 30%, rgba(14,165,233,0.07) 0%, transparent 60%),
        radial-gradient(ellipse 50% 40% at 20% 80%, rgba(139,92,246,0.05) 0%, transparent 50%);
    pointer-events: none;
}
.hero-grid {
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 3rem;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
    position: relative;
    z-index: 1;
}
.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: rgba(14,165,233,0.12);
    border: 1px solid rgba(14,165,233,0.3);
    color: #38BDF8;
    font-size: 0.75rem;
    font-weight: 500;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    padding: 0.4rem 1rem;
    border-radius: 100px;
    margin-bottom: 1.5rem;
}
.hero-badge .dot {
    width: 6px; height: 6px;
    background: #22C55E;
    border-radius: 50%;
    box-shadow: 0 0 6px #22C55E;
    animation: pulse-dot 2s ease-in-out infinite;
}
@keyframes pulse-dot {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.5; transform: scale(1.4); }
}
.hero-name {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.8rem, 5vw, 4.2rem);
    font-weight: 800;
    color: #F0F4FF;
    line-height: 1.1;
    letter-spacing: -0.02em;
    margin-bottom: 0.6rem;
}
.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(1rem, 2vw, 1.3rem);
    font-weight: 600;
    color: #38BDF8;
    letter-spacing: 0.05em;
    margin-bottom: 1.5rem;
}
.hero-tagline {
    font-size: 1rem;
    color: #8B9CBB;
    font-style: italic;
    margin-bottom: 1.8rem;
    font-weight: 300;
}
.hero-bio {
    font-size: 0.95rem;
    color: #A8B8D0;
    line-height: 1.8;
    max-width: 600px;
    margin-bottom: 2.5rem;
}
.hero-cta-row {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
    align-items: center;
}
.btn-primary {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: #0EA5E9;
    color: #07090F !important;
    font-weight: 700;
    font-size: 0.88rem;
    text-decoration: none !important;
    padding: 0.75rem 1.6rem;
    border-radius: 8px;
    transition: background 0.2s, transform 0.15s;
    letter-spacing: 0.02em;
}
.btn-primary:hover { background: #38BDF8; transform: translateY(-1px); }
.btn-outline {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: transparent;
    color: #8B9CBB !important;
    font-weight: 500;
    font-size: 0.88rem;
    text-decoration: none !important;
    padding: 0.75rem 1.4rem;
    border-radius: 8px;
    border: 1px solid rgba(139,156,187,0.3);
    transition: border-color 0.2s, color 0.2s, transform 0.15s;
}
.btn-outline:hover {
    border-color: #38BDF8;
    color: #38BDF8 !important;
    transform: translateY(-1px);
}

/* avatar */
.avatar-block {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
}
.avatar-ring {
    width: 160px; height: 160px;
    border-radius: 50%;
    background: linear-gradient(135deg, #0EA5E9, #8B5CF6);
    padding: 3px;
    box-shadow: 0 0 40px rgba(14,165,233,0.25);
}
.avatar-inner {
    width: 100%; height: 100%;
    border-radius: 50%;
    background: linear-gradient(135deg, #0D1B2E, #111827);
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Syne', sans-serif;
    font-size: 3rem;
    font-weight: 800;
    color: #E8EAF0;
    letter-spacing: -0.02em;
}
.location-tag {
    display: flex;
    align-items: center;
    gap: 0.4rem;
    color: #64748B;
    font-size: 0.82rem;
    letter-spacing: 0.05em;
}

/* ── NAV ── */
.nav-bar {
    background: rgba(7,9,15,0.95);
    border-bottom: 1px solid rgba(14,165,233,0.1);
    padding: 0 6rem;
    position: sticky;
    top: 0;
    z-index: 100;
    backdrop-filter: blur(12px);
}
.nav-inner {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    gap: 0;
}
.nav-link {
    display: inline-block;
    padding: 1rem 1.4rem;
    font-size: 0.82rem;
    font-weight: 500;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #64748B;
    text-decoration: none !important;
    transition: color 0.2s;
    border-bottom: 2px solid transparent;
    white-space: nowrap;
}
.nav-link:hover { color: #38BDF8; border-bottom-color: #38BDF8; }

/* ── SECTION LAYOUT ── */
.section-wrap {
    max-width: 1200px;
    margin: 0 auto;
    padding: 4rem 6rem;
}
.section-label {
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #0EA5E9;
    margin-bottom: 0.6rem;
}
.section-heading {
    font-family: 'Syne', sans-serif;
    font-size: 2rem;
    font-weight: 700;
    color: #F0F4FF;
    margin-bottom: 0.5rem;
    letter-spacing: -0.01em;
}
.section-sub {
    color: #64748B;
    font-size: 0.92rem;
    line-height: 1.6;
    margin-bottom: 3rem;
    max-width: 540px;
}
.divider {
    height: 1px;
    background: linear-gradient(90deg, rgba(14,165,233,0.3), transparent);
    margin: 3.5rem 0;
    max-width: 1200px;
    margin-left: auto;
    margin-right: auto;
    padding: 0 6rem;
}

/* ── STATS ROW ── */
.stats-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1.5rem;
    margin-top: 2rem;
    padding: 6rem;
    padding-top: 0;
    max-width: 1200px;
    margin: 0 auto;
}
.stat-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 12px;
    padding: 1.8rem;
    text-align: center;
    transition: border-color 0.2s, transform 0.2s;
}
.stat-card:hover {
    border-color: rgba(14,165,233,0.3);
    transform: translateY(-2px);
}
.stat-number {
    font-family: 'Syne', sans-serif;
    font-size: 2.2rem;
    font-weight: 800;
    color: #38BDF8;
}
.stat-label {
    font-size: 0.8rem;
    color: #64748B;
    margin-top: 0.3rem;
    letter-spacing: 0.05em;
}

/* ── TIMELINE ── */
.timeline { display: flex; flex-direction: column; gap: 0; }
.tl-item {
    display: grid;
    grid-template-columns: 48px 1fr;
    gap: 1.5rem;
    position: relative;
}
.tl-left {
    display: flex;
    flex-direction: column;
    align-items: center;
}
.tl-dot {
    width: 48px; height: 48px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.3rem;
    flex-shrink: 0;
    z-index: 1;
}
.tl-line {
    flex: 1;
    width: 2px;
    background: rgba(255,255,255,0.06);
    margin: 0.5rem 0;
    min-height: 2rem;
}
.tl-content {
    padding-bottom: 2.5rem;
}
.tl-header {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 1rem;
    flex-wrap: wrap;
    margin-bottom: 0.5rem;
}
.tl-role {
    font-family: 'Syne', sans-serif;
    font-size: 1.05rem;
    font-weight: 700;
    color: #F0F4FF;
}
.tl-company {
    font-size: 0.88rem;
    color: #38BDF8;
    font-weight: 500;
    margin-bottom: 0.3rem;
}
.tl-place {
    font-size: 0.8rem;
    color: #64748B;
    margin-bottom: 0.8rem;
}
.tl-badge {
    background: rgba(14,165,233,0.1);
    border: 1px solid rgba(14,165,233,0.2);
    color: #64748B;
    font-size: 0.75rem;
    padding: 0.3rem 0.8rem;
    border-radius: 100px;
    white-space: nowrap;
    font-weight: 500;
}
.tl-ul { list-style: none; padding: 0; }
.tl-ul li {
    position: relative;
    padding-left: 1.2rem;
    color: #8B9CBB;
    font-size: 0.88rem;
    line-height: 1.7;
    margin-bottom: 0.3rem;
}
.tl-ul li::before {
    content: '▸';
    position: absolute;
    left: 0;
    color: #0EA5E9;
    font-size: 0.7rem;
    top: 0.3rem;
}

/* ── FORMATION CARDS ── */
.edu-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5rem;
}
.edu-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 14px;
    padding: 1.8rem;
    transition: border-color 0.2s, transform 0.2s;
    position: relative;
    overflow: hidden;
}
.edu-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    right: 0; height: 3px;
    background: linear-gradient(90deg, #0EA5E9, #8B5CF6);
}
.edu-card:hover {
    border-color: rgba(14,165,233,0.25);
    transform: translateY(-2px);
}
.edu-level {
    display: flex;
    gap: 0.3rem;
    margin-bottom: 1rem;
}
.edu-star { color: #F59E0B; font-size: 0.9rem; }
.edu-star.empty { color: rgba(255,255,255,0.1); }
.edu-diplome {
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    font-size: 0.95rem;
    color: #F0F4FF;
    margin-bottom: 0.5rem;
    line-height: 1.4;
}
.edu-institution {
    font-size: 0.85rem;
    color: #38BDF8;
    font-weight: 500;
    margin-bottom: 0.3rem;
}
.edu-meta {
    font-size: 0.78rem;
    color: #64748B;
}

/* ── COMPETENCES ── */
.skills-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 2.5rem;
}
.skill-group-title {
    font-family: 'Syne', sans-serif;
    font-size: 0.85rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #38BDF8;
    margin-bottom: 1.2rem;
    padding-bottom: 0.6rem;
    border-bottom: 1px solid rgba(14,165,233,0.2);
}
.skill-row { margin-bottom: 1rem; }
.skill-top {
    display: flex;
    justify-content: space-between;
    margin-bottom: 0.4rem;
}
.skill-name { font-size: 0.85rem; color: #C4CDD8; font-weight: 500; }
.skill-pct { font-size: 0.8rem; color: #64748B; }
.skill-bar-bg {
    height: 5px;
    background: rgba(255,255,255,0.06);
    border-radius: 100px;
    overflow: hidden;
}
.skill-bar-fill {
    height: 100%;
    border-radius: 100px;
    transition: width 0.6s ease;
}

/* ── PROJET CARDS ── */
.proj-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5rem;
}
.proj-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 14px;
    padding: 2rem;
    transition: border-color 0.2s, transform 0.2s, box-shadow 0.2s;
    position: relative;
}
.proj-card:hover {
    border-color: rgba(14,165,233,0.3);
    transform: translateY(-3px);
    box-shadow: 0 12px 40px rgba(14,165,233,0.08);
}
.proj-icon {
    font-size: 2rem;
    margin-bottom: 1rem;
}
.proj-period {
    position: absolute;
    top: 1.5rem; right: 1.5rem;
    font-size: 0.72rem;
    color: #64748B;
    font-weight: 500;
    letter-spacing: 0.05em;
}
.proj-title {
    font-family: 'Syne', sans-serif;
    font-size: 1rem;
    font-weight: 700;
    color: #F0F4FF;
    margin-bottom: 0.8rem;
    line-height: 1.3;
    padding-right: 4rem;
}
.proj-desc {
    font-size: 0.83rem;
    color: #8B9CBB;
    line-height: 1.7;
    margin-bottom: 1.2rem;
}
.proj-impact {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    background: rgba(34,197,94,0.1);
    border: 1px solid rgba(34,197,94,0.2);
    color: #4ADE80;
    font-size: 0.75rem;
    font-weight: 600;
    padding: 0.3rem 0.8rem;
    border-radius: 100px;
    margin-bottom: 1.2rem;
}
.tags-row { display: flex; flex-wrap: wrap; gap: 0.4rem; margin-top: 1rem; }
.tag {
    background: rgba(139,92,246,0.1);
    border: 1px solid rgba(139,92,246,0.2);
    color: #A78BFA;
    font-size: 0.72rem;
    font-weight: 500;
    padding: 0.25rem 0.7rem;
    border-radius: 100px;
}

/* ── LANGUES ── */
.lang-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
}
.lang-card {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 10px;
    padding: 1.2rem 1.5rem;
    display: flex;
    align-items: center;
    gap: 1rem;
}
.lang-flag { font-size: 1.6rem; }
.lang-name { font-weight: 600; font-size: 0.9rem; color: #E8EAF0; }
.lang-level { font-size: 0.78rem; color: #64748B; margin-top: 0.1rem; }
.lang-bars { display: flex; gap: 4px; margin-left: auto; }
.lang-bar {
    width: 10px; height: 28px;
    border-radius: 3px;
    background: rgba(255,255,255,0.06);
}
.lang-bar.filled { background: #0EA5E9; }

/* ── CONTACT ── */
.contact-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 3rem;
    align-items: start;
}
.contact-info-block { display: flex; flex-direction: column; gap: 1.2rem; }
.contact-item {
    display: flex;
    align-items: center;
    gap: 1rem;
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 10px;
    padding: 1rem 1.2rem;
}
.contact-icon {
    width: 40px; height: 40px;
    border-radius: 8px;
    background: rgba(14,165,233,0.1);
    border: 1px solid rgba(14,165,233,0.2);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.1rem;
    flex-shrink: 0;
}
.contact-label { font-size: 0.72rem; color: #64748B; text-transform: uppercase; letter-spacing: 0.08em; }
.contact-value { font-size: 0.88rem; color: #E8EAF0; font-weight: 500; }
.contact-link {
    font-size: 0.88rem;
    color: #38BDF8;
    text-decoration: none !important;
    font-weight: 500;
}
.contact-link:hover { color: #7DD3FC; }

/* ── FOOTER ── */
.footer {
    background: #040508;
    border-top: 1px solid rgba(255,255,255,0.05);
    padding: 2.5rem 6rem;
    text-align: center;
    color: #64748B;
    font-size: 0.8rem;
    letter-spacing: 0.03em;
}

/* ── streamlit overrides ── */
.stTabs { background: transparent !important; }
[data-baseweb="tab-list"] {
    background: rgba(255,255,255,0.03) !important;
    border: 1px solid rgba(255,255,255,0.07) !important;
    border-radius: 10px !important;
    padding: 4px !important;
    gap: 0 !important;
}
[data-baseweb="tab"] {
    border-radius: 7px !important;
    color: #64748B !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.82rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.05em !important;
    padding: 0.6rem 1.4rem !important;
}
[aria-selected="true"] {
    background: rgba(14,165,233,0.15) !important;
    color: #38BDF8 !important;
}
button[data-testid="baseButton-secondary"] {
    background: rgba(14,165,233,0.1) !important;
    color: #38BDF8 !important;
    border: 1px solid rgba(14,165,233,0.3) !important;
    border-radius: 8px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 500 !important;
}
button[data-testid="baseButton-secondary"]:hover {
    background: rgba(14,165,233,0.2) !important;
}

/* responsive ish */
@media (max-width: 900px) {
    .hero-wrap { padding: 3rem 2rem 2.5rem; }
    .hero-grid { grid-template-columns: 1fr; }
    .avatar-block { display: none; }
    .section-wrap { padding: 3rem 2rem; }
    .stats-row { grid-template-columns: repeat(2,1fr); padding: 2rem; }
    .edu-grid, .skills-grid, .proj-grid, .contact-grid, .lang-grid { grid-template-columns: 1fr; }
    .nav-bar { padding: 0 2rem; }
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# HERO
# ─────────────────────────────────────────────
st.markdown(f"""
<div class="hero-wrap">
  <div class="hero-grid">
    <div>
      <div class="hero-badge">
        <span class="dot"></span>
        Disponible · Open to opportunities
      </div>
      <div class="hero-name">{PROFILE['name']}</div>
      <div class="hero-title">{PROFILE['title']}</div>
      <div class="hero-tagline">« {PROFILE['tagline']} »</div>
      <div class="hero-bio">{PROFILE['bio']}</div>
      <div class="hero-cta-row">
        <a href="mailto:{PROFILE['email']}" class="btn-primary">✉️ Me contacter</a>
        <a href="{PROFILE['linkedin']}" target="_blank" class="btn-outline">🔗 LinkedIn</a>
        <a href="{PROFILE['github']}" target="_blank" class="btn-outline">💻 GitHub</a>
      </div>
    </div>
    <div class="avatar-block">
      <div class="avatar-ring">
        <div class="avatar-inner">AS</div>
      </div>
      <div class="location-tag">📍 {PROFILE['location']}</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# STATS
# ─────────────────────────────────────────────
st.markdown("""
<div class="stats-row">
  <div class="stat-card">
    <div class="stat-number">4+</div>
    <div class="stat-label">Années d'études spécialisées</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">4</div>
    <div class="stat-label">Expériences professionnelles</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">10+</div>
    <div class="stat-label">Outils & technologies maîtrisés</div>
  </div>
  <div class="stat-card">
    <div class="stat-number">3</div>
    <div class="stat-label">Pays d'expérience</div>
  </div>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# NAV TABS (Streamlit native for interactivity)
# ─────────────────────────────────────────────
st.markdown('<div style="background:#07090F; padding: 1rem 6rem 0;">', unsafe_allow_html=True)
tab_exp, tab_form, tab_skills, tab_proj, tab_contact = st.tabs([
    "  💼  Expérience  ",
    "  🎓  Formation  ",
    "  ⚡  Compétences  ",
    "  🚀  Projets  ",
    "  📬  Contact  ",
])
st.markdown("</div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════
# TAB 1 – EXPÉRIENCE
# ══════════════════════════════════════════════
with tab_exp:
    st.markdown('<div class="section-wrap">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">Parcours professionnel</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading">Expériences</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">Des environnements variés — institutionnels, médicaux, aéronautiques — '
        'qui m\'ont forgé une vision à 360° de l\'analyse de données.</div>',
        unsafe_allow_html=True,
    )

    tl_html = '<div class="timeline">'
    for i, exp in enumerate(EXPERIENCES):
        is_last = i == len(EXPERIENCES) - 1
        tl_html += f"""
        <div class="tl-item">
          <div class="tl-left">
            <div class="tl-dot" style="background: rgba({','.join(str(int(exp['couleur'].lstrip('#')[j:j+2], 16)) for j in (0,2,4))}, 0.15); border: 1px solid {exp['couleur']}40;">
              {exp['icone']}
            </div>
            {'<div class="tl-line"></div>' if not is_last else ''}
          </div>
          <div class="tl-content">
            <div class="tl-header">
              <div>
                <div class="tl-role">{exp['titre']}</div>
                <div class="tl-company">{exp['entreprise']}</div>
                <div class="tl-place">📍 {exp['lieu']}</div>
              </div>
              <div class="tl-badge">{exp['periode']}</div>
            </div>
            <ul class="tl-ul">
              {''.join(f'<li>{p}</li>' for p in exp['points'])}
            </ul>
          </div>
        </div>
        """
    tl_html += "</div>"
    st.markdown(tl_html, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════
# TAB 2 – FORMATION
# ══════════════════════════════════════════════
with tab_form:
    st.markdown('<div class="section-wrap">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">Parcours académique</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading">Formation</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">Un cursus solide en mathématiques, statistiques et informatique décisionnelle, '
        'couronné par un Master II spécialisé.</div>',
        unsafe_allow_html=True,
    )

    edu_html = '<div class="edu-grid">'
    for edu in FORMATIONS:
        stars = "".join(
            f'<span class="edu-star{"" if s <= edu["niveau"] else " empty"}">★</span>'
            for s in range(1, 6)
        )
        edu_html += f"""
        <div class="edu-card">
          <div class="edu-level">{stars}</div>
          <div class="edu-diplome">{edu['diplome']}</div>
          <div class="edu-institution">🏛️ {edu['institution']}</div>
          <div class="edu-meta">📍 {edu['lieu']} &nbsp;·&nbsp; 📅 {edu['periode']}</div>
        </div>
        """
    edu_html += "</div>"
    st.markdown(edu_html, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════
# TAB 3 – COMPÉTENCES
# ══════════════════════════════════════════════
with tab_skills:
    st.markdown('<div class="section-wrap">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">Stack technique</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading">Compétences</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">Un ensemble cohérent d\'outils couvrant la collecte, '
        'le traitement, la modélisation et la visualisation des données.</div>',
        unsafe_allow_html=True,
    )

    skills_html = '<div class="skills-grid">'
    for groupe, items in COMPETENCES.items():
        skills_html += f'<div><div class="skill-group-title">{groupe}</div>'
        for nom, pct, color in items:
            skills_html += f"""
            <div class="skill-row">
              <div class="skill-top">
                <span class="skill-name">{nom}</span>
                <span class="skill-pct">{pct}%</span>
              </div>
              <div class="skill-bar-bg">
                <div class="skill-bar-fill" style="width:{pct}%; background: linear-gradient(90deg, {color}, {color}88);"></div>
              </div>
            </div>
            """
        skills_html += "</div>"
    skills_html += "</div>"
    st.markdown(skills_html, unsafe_allow_html=True)

    # Langues
    st.markdown('<br><div class="section-label" style="margin-top:2rem;">Communication</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading" style="font-size:1.3rem;">Langues</div>', unsafe_allow_html=True)

    LANG_FLAGS = {"Français": "🇫🇷", "Arabe": "🇰🇲", "Anglais": "🇬🇧", "Shingazidja": "🌍"}
    lang_html = '<div class="lang-grid" style="margin-top:1.5rem;">'
    for nom, pct, desc in LANGUES:
        filled = round(pct / 20)
        bars = "".join(
            f'<div class="lang-bar{"  filled" if b <= filled else ""}"></div>'
            for b in range(1, 6)
        )
        lang_html += f"""
        <div class="lang-card">
          <div class="lang-flag">{LANG_FLAGS.get(nom, '🌐')}</div>
          <div>
            <div class="lang-name">{nom}</div>
            <div class="lang-level">{desc}</div>
          </div>
          <div class="lang-bars">{bars}</div>
        </div>
        """
    lang_html += "</div>"
    st.markdown(lang_html, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════
# TAB 4 – PROJETS
# ══════════════════════════════════════════════
with tab_proj:
    st.markdown('<div class="section-wrap">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">Réalisations</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading">Projets Data & BI</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">Projets concrets alliant rigueur statistique, ingénierie de données '
        'et visualisation pour des prises de décision à fort impact.</div>',
        unsafe_allow_html=True,
    )

    proj_html = '<div class="proj-grid">'
    for p in PROJETS:
        tags_html = "".join(f'<span class="tag">{t}</span>' for t in p["tags"])
        proj_html += f"""
        <div class="proj-card">
          <div class="proj-period">{p['periode']}</div>
          <div class="proj-icon">{p['icone']}</div>
          <div class="proj-title">{p['titre']}</div>
          <div class="proj-desc">{p['desc']}</div>
          <div class="proj-impact">✦ {p['impact']}</div>
          <div class="tags-row">{tags_html}</div>
        </div>
        """
    proj_html += "</div>"
    st.markdown(proj_html, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════
# TAB 5 – CONTACT
# ══════════════════════════════════════════════
with tab_contact:
    st.markdown('<div class="section-wrap">', unsafe_allow_html=True)
    st.markdown('<div class="section-label">Restons en contact</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-heading">Contact</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">Disponible pour des opportunités en Data Analysis / BI Junior. '
        'N\'hésitez pas à me contacter directement.</div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="contact-grid">', unsafe_allow_html=True)

    # LEFT: info
    st.markdown(f"""
    <div class="contact-info-block">
      <div class="contact-item">
        <div class="contact-icon">✉️</div>
        <div>
          <div class="contact-label">Email professionnel</div>
          <a href="mailto:{PROFILE['email']}" class="contact-link">{PROFILE['email']}</a>
        </div>
      </div>
      <div class="contact-item">
        <div class="contact-icon">📱</div>
        <div>
          <div class="contact-label">Téléphone / WhatsApp</div>
          <a href="tel:{PROFILE['phone'].replace(' ','')}" class="contact-link">{PROFILE['phone']}</a>
        </div>
      </div>
      <div class="contact-item">
        <div class="contact-icon">🔗</div>
        <div>
          <div class="contact-label">LinkedIn</div>
          <a href="{PROFILE['linkedin']}" target="_blank" class="contact-link">linkedin.com/in/sefdineahmed</a>
        </div>
      </div>
      <div class="contact-item">
        <div class="contact-icon">💻</div>
        <div>
          <div class="contact-label">GitHub</div>
          <a href="{PROFILE['github']}" target="_blank" class="contact-link">github.com/sefdineahmed</a>
        </div>
      </div>
      <div class="contact-item">
        <div class="contact-icon">📍</div>
        <div>
          <div class="contact-label">Localisation</div>
          <div class="contact-value">{PROFILE['location']} · Remote OK</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # Quick message
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background: rgba(14,165,233,0.06); border: 1px solid rgba(14,165,233,0.2);
                border-radius: 14px; padding: 2rem; margin-top: 1rem;">
      <div style="font-family:'Syne',sans-serif; font-size:1rem; font-weight:700; color:#F0F4FF; margin-bottom:1rem;">
        💬 Envoyez-moi un message rapide
      </div>
    """, unsafe_allow_html=True)

    col_n, col_e = st.columns(2)
    with col_n:
        nom = st.text_input("Votre nom", placeholder="Marie Dupont")
    with col_e:
        email_input = st.text_input("Votre email", placeholder="marie@entreprise.com")
    message = st.text_area("Votre message", placeholder="Bonjour Ahmed, je suis ...", height=120)
    if st.button("📨 Envoyer le message", use_container_width=False):
        if nom and email_input and message:
            st.success("✅ Message envoyé ! Je vous répondrai sous 24h.")
        else:
            st.warning("Veuillez remplir tous les champs.")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────
st.markdown(f"""
<div class="footer">
  <div style="font-family:'Syne',sans-serif; font-size:1rem; font-weight:700; color:#E8EAF0; margin-bottom:0.5rem;">
    Ahmed Sefdine
  </div>
  <div>Business Intelligence Analyst Junior · Dakar, Sénégal</div>
  <div style="margin-top:0.8rem; display:flex; justify-content:center; gap:1.5rem; flex-wrap:wrap;">
    <a href="mailto:{PROFILE['email']}" style="color:#38BDF8; text-decoration:none;">✉️ Email</a>
    <a href="{PROFILE['linkedin']}" target="_blank" style="color:#38BDF8; text-decoration:none;">🔗 LinkedIn</a>
    <a href="{PROFILE['github']}" target="_blank" style="color:#38BDF8; text-decoration:none;">💻 GitHub</a>
  </div>
  <div style="margin-top:1rem; color:#334155;">
    © {datetime.now().year} Ahmed Sefdine · Fait avec ❤️ & Streamlit
  </div>
</div>
""", unsafe_allow_html=True)
