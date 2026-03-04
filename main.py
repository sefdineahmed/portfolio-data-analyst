import streamlit as st
from datetime import datetime

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
}

EXPERIENCES = [
    {
        "titre": "Analyste de Données Junior (Stage en cours)",
        "entreprise": "Agence Nationale de Statistique et Démographique",
        "lieu": "Diourbel, Sénégal",
        "periode": "Oct. 2025 – Aujourd'hui",
        "icone": "🏛️",
        "rgb": "14,165,233",
        "hex": "#0EA5E9",
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
        "rgb": "16,185,129",
        "hex": "#10B981",
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
        "rgb": "139,92,246",
        "hex": "#8B5CF6",
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
        "rgb": "245,158,11",
        "hex": "#F59E0B",
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
        ("Power BI", 85, "#F59E0B"),
        ("Matplotlib / Seaborn", 88, "#0EA5E9"),
        ("Tableau (notions)", 55, "#E97627"),
        ("Excel avancé", 90, "#16A34A"),
    ],
    "Langages & Données": [
        ("Python (pandas, numpy, sklearn)", 90, "#3776AB"),
        ("SQL (PostgreSQL, MySQL)", 85, "#336791"),
        ("LaTeX", 80, "#008080"),
        ("R (notions)", 55, "#276DC3"),
    ],
    "Data Engineering & ETL": [
        ("Talend Open Studio", 75, "#FF6D00"),
        ("KoboToolbox", 80, "#23B5D3"),
        ("Access & SGBD", 70, "#A4373A"),
    ],
    "Statistiques & ML": [
        ("Statistiques descriptives / inférentielles", 90, "#0EA5E9"),
        ("Modèles de survie", 85, "#10B981"),
        ("Machine Learning supervisé", 75, "#8B5CF6"),
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
        "impact": "C-index > 78%",
    },
    {
        "titre": "Dashboard BI – Trafic Aérien Comorien",
        "periode": "2019",
        "tags": ["Power BI", "SQL", "Excel", "DAX"],
        "desc": (
            "Conception d'un tableau de bord interactif analysant 12 ans de données du trafic aérien. "
            "KPIs dynamiques, segmentation par routes et périodes, filtres temporels et géographiques."
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
            "Pipeline ETL avec Talend Open Studio pour alimenter des rapports trimestriels standardisés."
        ),
        "icone": "⚙️",
        "impact": "−60% temps de traitement",
    },
    {
        "titre": "Rapport RSES 2024 – Analyse Économique & Sociale",
        "periode": "2025",
        "tags": ["Python", "Excel", "Power BI", "Reporting institutionnel"],
        "desc": (
            "Contribution au Rapport sur la Situation Économique et Sociale du Sénégal 2024. "
            "Collecte multi-sources, consolidation des données sectorielles et rédaction analytique."
        ),
        "icone": "📋",
        "impact": "Publication nationale officielle",
    },
]

LANGUES = [
    ("Français",    95,  "Courant – professionnel", "🇫🇷"),
    ("Arabe",       80,  "Langue maternelle",       "🇰🇲"),
    ("Anglais",     60,  "Intermédiaire – technique","🇬🇧"),
    ("Shingazidja", 100, "Langue maternelle",       "🌍"),
]

# ─────────────────────────────────────────────
# CSS — WHITE PROFESSIONAL THEME
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

*, *::before, *::after { box-sizing: border-box; }

/* ── Force white background everywhere ── */
html, body,
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
.stApp, .main, section.main {
    background-color: #F8FAFC !important;
    color: #1E293B !important;
    font-family: 'DM Sans', sans-serif !important;
}
[data-testid="stHeader"]  { display: none !important; }
[data-testid="stSidebar"] { display: none !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ─ HERO ─ */
.hero {
    background: linear-gradient(150deg, #FFFFFF 0%, #F0F7FF 55%, #EEF2FF 100%);
    border-bottom: 1px solid #E2E8F0;
    padding: 4.5rem 8rem 3.5rem;
    position: relative; overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute; inset: 0;
    background:
        radial-gradient(ellipse 70% 55% at 85% 15%, rgba(14,165,233,0.07) 0%, transparent 55%),
        radial-gradient(ellipse 45% 50% at 8%  90%, rgba(99,102,241,0.05) 0%, transparent 50%);
    pointer-events: none;
}
.hero-g {
    display: grid;
    grid-template-columns: 1fr 200px;
    gap: 3rem; align-items: center;
    max-width: 1100px; margin: 0 auto;
    position: relative; z-index: 1;
}
.badge {
    display: inline-flex; align-items: center; gap: .5rem;
    background: rgba(14,165,233,.08);
    border: 1px solid rgba(14,165,233,.22);
    color: #0284C7;
    font-size: .71rem; font-weight: 600; letter-spacing: .15em; text-transform: uppercase;
    padding: .38rem 1rem; border-radius: 100px; margin-bottom: 1.4rem;
}
.badge .dot {
    width: 7px; height: 7px; background: #22C55E; border-radius: 50%;
    box-shadow: 0 0 6px #22C55E; animation: pdot 2s ease-in-out infinite;
}
@keyframes pdot { 0%,100%{opacity:1;transform:scale(1)} 50%{opacity:.45;transform:scale(1.55)} }
.h-name {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.4rem, 4.5vw, 3.5rem);
    font-weight: 800; color: #0F172A;
    line-height: 1.08; letter-spacing: -.025em; margin-bottom: .5rem;
}
.h-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.1rem; font-weight: 600; color: #0284C7;
    letter-spacing: .04em; margin-bottom: 1.1rem;
}
.h-quote {
    font-size: .93rem; color: #64748B; font-style: italic; font-weight: 300; margin-bottom: 1.5rem;
}
.h-bio {
    font-size: .92rem; color: #475569; line-height: 1.85; max-width: 575px; margin-bottom: 2rem;
}
.cta { display: flex; gap: .8rem; flex-wrap: wrap; align-items: center; }
.btn-p {
    display: inline-flex; align-items: center; gap: .4rem;
    background: #0EA5E9; color: #FFF !important; font-weight: 700; font-size: .84rem;
    text-decoration: none !important; padding: .68rem 1.5rem; border-radius: 8px;
    transition: background .2s, transform .15s;
}
.btn-p:hover { background: #0284C7; transform: translateY(-1px); }
.btn-o {
    display: inline-flex; align-items: center; gap: .4rem;
    background: #FFF; color: #475569 !important; font-weight: 500; font-size: .84rem;
    text-decoration: none !important; padding: .68rem 1.3rem; border-radius: 8px;
    border: 1px solid #CBD5E1; transition: border-color .2s, color .2s, transform .15s;
}
.btn-o:hover { border-color: #0EA5E9; color: #0284C7 !important; transform: translateY(-1px); }
/* avatar */
.av-block { display: flex; flex-direction: column; align-items: center; gap: .8rem; }
.av-ring {
    width: 148px; height: 148px; border-radius: 50%;
    background: linear-gradient(135deg, #0EA5E9, #6366F1);
    padding: 3px; box-shadow: 0 8px 28px rgba(14,165,233,.18);
}
.av-inner {
    width: 100%; height: 100%; border-radius: 50%;
    background: linear-gradient(135deg, #EFF6FF, #EEF2FF);
    display: flex; align-items: center; justify-content: center;
    font-family: 'Syne', sans-serif; font-size: 2.7rem; font-weight: 800; color: #0284C7;
}
.loc { font-size: .77rem; color: #94A3B8; letter-spacing: .04em; }

/* ─ STATS BAND ─ */
.stats-band {
    background: #FFFFFF; border-bottom: 1px solid #E2E8F0;
}
.stats-row {
    display: grid; grid-template-columns: repeat(4, 1fr);
    max-width: 1100px; margin: 0 auto; padding: 0 8rem;
}
.s-cell {
    padding: 1.7rem 1rem; text-align: center;
    border-right: 1px solid #F1F5F9;
}
.s-cell:last-child { border-right: none; }
.s-n { font-family: 'Syne', sans-serif; font-size: 2rem; font-weight: 800; color: #0284C7; }
.s-l { font-size: .77rem; color: #94A3B8; margin-top: .22rem; letter-spacing: .04em; }

/* ─ WRAP ─ */
.wrap { max-width: 1100px; margin: 0 auto; padding: 3.5rem 8rem; }
.lbl {
    font-size: .69rem; font-weight: 600; letter-spacing: .18em;
    text-transform: uppercase; color: #0EA5E9; margin-bottom: .45rem;
}
.hd {
    font-family: 'Syne', sans-serif; font-size: 1.85rem; font-weight: 700;
    color: #0F172A; margin-bottom: .4rem; letter-spacing: -.01em;
}
.sub { color: #94A3B8; font-size: .88rem; line-height: 1.65; margin-bottom: 2.5rem; max-width: 510px; }

/* ─ TIMELINE ─ */
.tl { display: flex; flex-direction: column; }
.tl-item { display: grid; grid-template-columns: 52px 1fr; gap: 1.4rem; }
.tl-left { display: flex; flex-direction: column; align-items: center; }
.tl-dot {
    width: 48px; height: 48px; border-radius: 12px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.25rem; flex-shrink: 0;
}
.tl-line { flex: 1; width: 2px; background: #E2E8F0; margin: .4rem 0; min-height: 1.5rem; }
.tl-body { padding-bottom: 2.2rem; }
.tl-hdr {
    display: flex; align-items: flex-start; justify-content: space-between;
    gap: 1rem; flex-wrap: wrap; margin-bottom: .45rem;
}
.tl-role {
    font-family: 'Syne', sans-serif; font-size: .98rem; font-weight: 700; color: #0F172A;
}
.tl-co  { font-size: .85rem; color: #0284C7; font-weight: 500; margin-bottom: .2rem; }
.tl-pl  { font-size: .77rem; color: #94A3B8; margin-bottom: .7rem; }
.tl-bdg {
    background: #F1F5F9; border: 1px solid #E2E8F0; color: #64748B;
    font-size: .71rem; padding: .28rem .75rem; border-radius: 100px;
    white-space: nowrap; font-weight: 500;
}
.tl-ul  { list-style: none; padding: 0; margin: 0; }
.tl-ul li {
    position: relative; padding-left: 1.1rem; color: #475569;
    font-size: .85rem; line-height: 1.75; margin-bottom: .22rem;
}
.tl-ul li::before {
    content: '▸'; position: absolute; left: 0;
    color: #0EA5E9; font-size: .64rem; top: .37rem;
}

/* ─ EDU CARDS ─ */
.edu-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1.2rem; }
.edu-card {
    background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 14px;
    padding: 1.6rem; position: relative; overflow: hidden;
    transition: border-color .2s, transform .2s, box-shadow .2s;
}
.edu-card::before {
    content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px;
    background: linear-gradient(90deg, #0EA5E9, #6366F1);
}
.edu-card:hover {
    border-color: #BAE6FD; transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(14,165,233,.08);
}
.edu-stars { display: flex; gap: .22rem; margin-bottom: .8rem; }
.edu-star       { color: #F59E0B; font-size: .82rem; }
.edu-star.empty { color: #E2E8F0; font-size: .82rem; }
.edu-deg {
    font-family: 'Syne', sans-serif; font-weight: 700; font-size: .9rem;
    color: #0F172A; margin-bottom: .42rem; line-height: 1.4;
}
.edu-inst { font-size: .82rem; color: #0284C7; font-weight: 500; margin-bottom: .22rem; }
.edu-meta { font-size: .75rem; color: #94A3B8; }

/* ─ SKILLS ─ */
.sk-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 2.5rem; }
.sk-grp {
    font-family: 'Syne', sans-serif; font-size: .78rem; font-weight: 700;
    letter-spacing: .1em; text-transform: uppercase; color: #0284C7;
    margin-bottom: 1.1rem; padding-bottom: .5rem; border-bottom: 2px solid #EFF6FF;
}
.sk-row { margin-bottom: .92rem; }
.sk-top { display: flex; justify-content: space-between; margin-bottom: .32rem; }
.sk-nm  { font-size: .83rem; color: #334155; font-weight: 500; }
.sk-pc  { font-size: .77rem; color: #94A3B8; }
.sk-bg  { height: 6px; background: #F1F5F9; border-radius: 100px; overflow: hidden; }
.sk-fill{ height: 100%; border-radius: 100px; }

/* ─ LANG ─ */
.lg-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 1.5rem; }
.lg-card {
    background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 10px;
    padding: 1.1rem 1.3rem; display: flex; align-items: center; gap: .9rem;
}
.lg-flag { font-size: 1.55rem; }
.lg-nm   { font-weight: 600; font-size: .87rem; color: #1E293B; }
.lg-lv   { font-size: .74rem; color: #94A3B8; margin-top: .1rem; }
.lg-bars { display: flex; gap: 4px; margin-left: auto; }
.lbar    { width: 10px; height: 26px; border-radius: 3px; background: #F1F5F9; }
.lbar.on { background: #0EA5E9; }

/* ─ PROJECTS ─ */
.pj-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1.3rem; }
.pj-card {
    background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 14px;
    padding: 1.8rem; position: relative;
    transition: border-color .2s, transform .2s, box-shadow .2s;
}
.pj-card:hover {
    border-color: #BAE6FD; transform: translateY(-3px);
    box-shadow: 0 12px 36px rgba(14,165,233,.08);
}
.pj-period {
    position: absolute; top: 1.4rem; right: 1.4rem;
    font-size: .69rem; color: #94A3B8; font-weight: 500;
}
.pj-ico   { font-size: 1.8rem; margin-bottom: .85rem; }
.pj-title {
    font-family: 'Syne', sans-serif; font-size: .95rem; font-weight: 700;
    color: #0F172A; margin-bottom: .65rem; line-height: 1.35; padding-right: 4.5rem;
}
.pj-desc  { font-size: .82rem; color: #64748B; line-height: 1.75; margin-bottom: .95rem; }
.pj-imp {
    display: inline-flex; align-items: center; gap: .32rem;
    background: #F0FDF4; border: 1px solid #BBF7D0; color: #16A34A;
    font-size: .72rem; font-weight: 600; padding: .25rem .72rem; border-radius: 100px;
    margin-bottom: .9rem;
}
.tags { display: flex; flex-wrap: wrap; gap: .32rem; margin-top: .75rem; }
.tag {
    background: #EEF2FF; border: 1px solid #C7D2FE; color: #4F46E5;
    font-size: .69rem; font-weight: 500; padding: .2rem .62rem; border-radius: 100px;
}

/* ─ CONTACT ─ */
.ct-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; align-items: start; }
.ct-list { display: flex; flex-direction: column; gap: .9rem; }
.ct-item {
    display: flex; align-items: center; gap: .9rem;
    background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 10px;
    padding: .88rem 1.1rem;
}
.ct-ico {
    width: 38px; height: 38px; border-radius: 8px;
    background: #EFF6FF; border: 1px solid #DBEAFE;
    display: flex; align-items: center; justify-content: center;
    font-size: .95rem; flex-shrink: 0;
}
.ct-lbl { font-size: .68rem; color: #94A3B8; text-transform: uppercase; letter-spacing: .07em; }
.ct-val { font-size: .85rem; color: #1E293B; font-weight: 500; }
.ct-lnk { font-size: .85rem; color: #0284C7; text-decoration: none !important; font-weight: 500; }
.ct-lnk:hover { color: #0EA5E9; }
.msg-box {
    background: #F8FAFF; border: 1px solid #DBEAFE; border-radius: 14px; padding: 1.8rem;
}
.msg-title {
    font-family: 'Syne', sans-serif; font-size: .93rem; font-weight: 700;
    color: #0F172A; margin-bottom: 1.1rem;
}

/* ─ FOOTER ─ */
.footer {
    background: #FFFFFF; border-top: 1px solid #E2E8F0;
    padding: 2.2rem 8rem; text-align: center;
    color: #94A3B8; font-size: .77rem; letter-spacing: .03em;
}
.footer .fn { font-family:'Syne',sans-serif; font-size:.93rem; font-weight:700; color:#334155; margin-bottom:.38rem; }
.footer .fl { display:flex; justify-content:center; gap:1.4rem; flex-wrap:wrap; margin-top:.65rem; }
.footer .fl a { color:#0284C7; text-decoration:none !important; }
.footer .fl a:hover { color:#0EA5E9; }

/* ─ Streamlit overrides ─ */
[data-baseweb="tab-list"] {
    background: #F1F5F9 !important;
    border: 1px solid #E2E8F0 !important;
    border-radius: 10px !important;
    padding: 4px !important; gap: 0 !important;
}
[data-baseweb="tab"] {
    border-radius: 7px !important; color: #64748B !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: .81rem !important; font-weight: 500 !important;
    letter-spacing: .05em !important; padding: .58rem 1.35rem !important;
    background: transparent !important;
}
[aria-selected="true"] {
    background: #FFFFFF !important; color: #0284C7 !important;
    box-shadow: 0 1px 4px rgba(0,0,0,.07) !important;
}
button[data-testid="baseButton-secondary"] {
    background: #EFF6FF !important; color: #0284C7 !important;
    border: 1px solid #DBEAFE !important; border-radius: 8px !important;
    font-family: 'DM Sans', sans-serif !important; font-weight: 500 !important;
}
.stTextInput input, .stTextArea textarea {
    background: #FFFFFF !important; border: 1px solid #E2E8F0 !important;
    color: #1E293B !important; border-radius: 8px !important;
    font-family: 'DM Sans', sans-serif !important;
}
label { color: #475569 !important; font-size: .85rem !important; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# HERO
# ─────────────────────────────────────────────
st.markdown(f"""
<div class="hero">
  <div class="hero-g">
    <div>
      <div class="badge"><span class="dot"></span>Disponible · Open to opportunities</div>
      <div class="h-name">{PROFILE['name']}</div>
      <div class="h-title">{PROFILE['title']}</div>
      <div class="h-quote">« {PROFILE['tagline']} »</div>
      <div class="h-bio">{PROFILE['bio']}</div>
      <div class="cta">
        <a href="mailto:{PROFILE['email']}" class="btn-p">✉️ Me contacter</a>
        <a href="{PROFILE['linkedin']}" target="_blank" class="btn-o">🔗 LinkedIn</a>
        <a href="{PROFILE['github']}" target="_blank" class="btn-o">💻 GitHub</a>
      </div>
    </div>
    <div class="av-block">
      <div class="av-ring"><div class="av-inner">AS</div></div>
      <div class="loc">📍 {PROFILE['location']}</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# STATS
# ─────────────────────────────────────────────
st.markdown("""
<div class="stats-band">
  <div class="stats-row">
    <div class="s-cell"><div class="s-n">4+</div><div class="s-l">Années études spécialisées</div></div>
    <div class="s-cell"><div class="s-n">4</div><div class="s-l">Expériences professionnelles</div></div>
    <div class="s-cell"><div class="s-n">10+</div><div class="s-l">Outils &amp; technologies</div></div>
    <div class="s-cell"><div class="s-n">3</div><div class="s-l">Pays d'expérience</div></div>
  </div>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# TABS
# ─────────────────────────────────────────────
st.markdown('<div style="background:#F8FAFC;padding:1.5rem 8rem 0;">', unsafe_allow_html=True)
tab_exp, tab_form, tab_sk, tab_proj, tab_ct = st.tabs([
    "  💼  Expérience  ",
    "  🎓  Formation  ",
    "  ⚡  Compétences  ",
    "  🚀  Projets  ",
    "  📬  Contact  ",
])
st.markdown("</div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════
# EXPÉRIENCE
# ══════════════════════════════════════════════
with tab_exp:
    st.markdown('<div class="wrap">', unsafe_allow_html=True)
    st.markdown('<div class="lbl">Parcours professionnel</div>', unsafe_allow_html=True)
    st.markdown('<div class="hd">Expériences</div>', unsafe_allow_html=True)
    st.markdown(
        "<div class='sub'>Des environnements variés — institutionnels, médicaux, aéronautiques — "
        "qui m'ont forgé une vision à 360° de la donnée et de son impact décisionnel.</div>",
        unsafe_allow_html=True,
    )

    tl = '<div class="tl">'
    for i, e in enumerate(EXPERIENCES):
        last = (i == len(EXPERIENCES) - 1)
        tl += f"""
        <div class="tl-item">
          <div class="tl-left">
            <div class="tl-dot" style="background:rgba({e['rgb']},.11);border:1px solid {e['hex']}38;">
              {e['icone']}
            </div>
            {'<div class="tl-line"></div>' if not last else ''}
          </div>
          <div class="tl-body">
            <div class="tl-hdr">
              <div>
                <div class="tl-role">{e['titre']}</div>
                <div class="tl-co">{e['entreprise']}</div>
                <div class="tl-pl">📍 {e['lieu']}</div>
              </div>
              <div class="tl-bdg">{e['periode']}</div>
            </div>
            <ul class="tl-ul">{''.join(f"<li>{p}</li>" for p in e['points'])}</ul>
          </div>
        </div>"""
    tl += "</div>"
    st.markdown(tl, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════
# FORMATION
# ══════════════════════════════════════════════
with tab_form:
    st.markdown('<div class="wrap">', unsafe_allow_html=True)
    st.markdown('<div class="lbl">Parcours académique</div>', unsafe_allow_html=True)
    st.markdown('<div class="hd">Formation</div>', unsafe_allow_html=True)
    st.markdown(
        "<div class='sub'>Un cursus rigoureux en mathématiques, statistiques et informatique "
        "décisionnelle, couronné par un Master II spécialisé.</div>",
        unsafe_allow_html=True,
    )
    eg = '<div class="edu-grid">'
    for f in FORMATIONS:
        stars = "".join(
            f'<span class="edu-star{" empty" if s > f["niveau"] else ""}">★</span>'
            for s in range(1, 6)
        )
        eg += f"""
        <div class="edu-card">
          <div class="edu-stars">{stars}</div>
          <div class="edu-deg">{f['diplome']}</div>
          <div class="edu-inst">🏛️ {f['institution']}</div>
          <div class="edu-meta">📍 {f['lieu']} &nbsp;·&nbsp; 📅 {f['periode']}</div>
        </div>"""
    eg += "</div>"
    st.markdown(eg, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════
# COMPÉTENCES
# ══════════════════════════════════════════════
with tab_sk:
    st.markdown('<div class="wrap">', unsafe_allow_html=True)
    st.markdown('<div class="lbl">Stack technique</div>', unsafe_allow_html=True)
    st.markdown('<div class="hd">Compétences</div>', unsafe_allow_html=True)
    st.markdown(
        "<div class='sub'>Un ensemble cohérent d'outils couvrant la collecte, "
        "le traitement, la modélisation et la visualisation des données.</div>",
        unsafe_allow_html=True,
    )
    sk = '<div class="sk-grid">'
    for grp, items in COMPETENCES.items():
        sk += f'<div><div class="sk-grp">{grp}</div>'
        for nm, pct, col in items:
            sk += f"""
            <div class="sk-row">
              <div class="sk-top"><span class="sk-nm">{nm}</span><span class="sk-pc">{pct}%</span></div>
              <div class="sk-bg">
                <div class="sk-fill" style="width:{pct}%;background:linear-gradient(90deg,{col},{col}88);"></div>
              </div>
            </div>"""
        sk += "</div>"
    sk += "</div>"
    st.markdown(sk, unsafe_allow_html=True)

    st.markdown('<div class="lbl" style="margin-top:2.5rem;">Communication</div>', unsafe_allow_html=True)
    st.markdown('<div class="hd" style="font-size:1.3rem;">Langues</div>', unsafe_allow_html=True)

    lg = '<div class="lg-grid">'
    for nm, pct, desc, flag in LANGUES:
        filled = round(pct / 20)
        bars = "".join(
            f'<div class="lbar{"  on" if b <= filled else ""}"></div>'
            for b in range(1, 6)
        )
        lg += f"""
        <div class="lg-card">
          <div class="lg-flag">{flag}</div>
          <div><div class="lg-nm">{nm}</div><div class="lg-lv">{desc}</div></div>
          <div class="lg-bars">{bars}</div>
        </div>"""
    lg += "</div>"
    st.markdown(lg, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════
# PROJETS
# ══════════════════════════════════════════════
with tab_proj:
    st.markdown('<div class="wrap">', unsafe_allow_html=True)
    st.markdown('<div class="lbl">Réalisations</div>', unsafe_allow_html=True)
    st.markdown('<div class="hd">Projets Data &amp; BI</div>', unsafe_allow_html=True)
    st.markdown(
        "<div class='sub'>Projets concrets alliant rigueur statistique, ingénierie de données "
        "et visualisation pour des prises de décision à fort impact.</div>",
        unsafe_allow_html=True,
    )
    pg = '<div class="pj-grid">'
    for p in PROJETS:
        tags = "".join(f'<span class="tag">{t}</span>' for t in p["tags"])
        pg += f"""
        <div class="pj-card">
          <div class="pj-period">{p['periode']}</div>
          <div class="pj-ico">{p['icone']}</div>
          <div class="pj-title">{p['titre']}</div>
          <div class="pj-desc">{p['desc']}</div>
          <div class="pj-imp">✦ {p['impact']}</div>
          <div class="tags">{tags}</div>
        </div>"""
    pg += "</div>"
    st.markdown(pg, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════
# CONTACT
# ══════════════════════════════════════════════
with tab_ct:
    st.markdown('<div class="wrap">', unsafe_allow_html=True)
    st.markdown('<div class="lbl">Restons en contact</div>', unsafe_allow_html=True)
    st.markdown('<div class="hd">Contact</div>', unsafe_allow_html=True)
    st.markdown(
        "<div class='sub'>Disponible pour des opportunités BI / Data Analyst Junior. "
        "N'hésitez pas à me contacter directement.</div>",
        unsafe_allow_html=True,
    )

    st.markdown(f"""
    <div class="ct-list">
      <div class="ct-item">
        <div class="ct-ico">✉️</div>
        <div><div class="ct-lbl">Email professionnel</div>
          <a href="mailto:{PROFILE['email']}" class="ct-lnk">{PROFILE['email']}</a></div>
      </div>
      <div class="ct-item">
        <div class="ct-ico">📱</div>
        <div><div class="ct-lbl">Téléphone / WhatsApp</div>
          <a href="tel:{PROFILE['phone'].replace(' ','')}" class="ct-lnk">{PROFILE['phone']}</a></div>
      </div>
      <div class="ct-item">
        <div class="ct-ico">🔗</div>
        <div><div class="ct-lbl">LinkedIn</div>
          <a href="{PROFILE['linkedin']}" target="_blank" class="ct-lnk">linkedin.com/in/sefdineahmed</a></div>
      </div>
      <div class="ct-item">
        <div class="ct-ico">💻</div>
        <div><div class="ct-lbl">GitHub</div>
          <a href="{PROFILE['github']}" target="_blank" class="ct-lnk">github.com/sefdineahmed</a></div>
      </div>
      <div class="ct-item">
        <div class="ct-ico">📍</div>
        <div><div class="ct-lbl">Localisation</div>
          <div class="ct-val">{PROFILE['location']} · Remote OK</div></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="msg-box" style="margin-top:2rem;">
      <div class="msg-title">💬 Envoyez-moi un message</div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        nom_v = st.text_input("Votre nom", placeholder="Marie Dupont")
    with c2:
        email_v = st.text_input("Votre email", placeholder="marie@entreprise.com")
    msg_v = st.text_area("Votre message", placeholder="Bonjour Ahmed, je suis ...", height=120)
    if st.button("📨 Envoyer le message"):
        if nom_v and email_v and msg_v:
            st.success("✅ Message reçu ! Je vous répondrai dans les 24h.")
        else:
            st.warning("Veuillez remplir tous les champs.")
    st.markdown("</div>", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────
st.markdown(f"""
<div class="footer">
  <div class="fn">Ahmed Sefdine</div>
  <div>Business Intelligence Analyst Junior · Dakar, Sénégal</div>
  <div class="fl">
    <a href="mailto:{PROFILE['email']}">✉️ Email</a>
    <a href="{PROFILE['linkedin']}" target="_blank">🔗 LinkedIn</a>
    <a href="{PROFILE['github']}" target="_blank">💻 GitHub</a>
  </div>
  <div style="margin-top:.8rem;color:#CBD5E1;">© {datetime.now().year} Ahmed Sefdine · Fait avec ❤️ &amp; Streamlit</div>
</div>
""", unsafe_allow_html=True)
