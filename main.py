import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Ahmed Sefdine · BI Analyst",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ─── DATA ───────────────────────────────────────────────────────────────────
PROFILE = {
    "name": "Ahmed Sefdine",
    "title": "Business Intelligence Analyst Junior",
    "tagline": "Transformer la donnée brute en décisions éclairées.",
    "bio": (
        "Jeune diplômé passionné par l'analyse de données, la statistique appliquée "
        "et la Business Intelligence. Fort d'expériences variées en environnements "
        "académiques, institutionnels et médicaux, je maîtrise l'ensemble de la chaîne "
        "analytique — de la collecte à la visualisation — avec des outils comme Python, "
        "SQL, Power BI et Talend."
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
        ("Statistiques desc. / inférentielles", 90, "#0EA5E9"),
        ("Modèles de survie", 85, "#10B981"),
        ("Machine Learning supervisé", 75, "#8B5CF6"),
        ("SPSS", 75, "#005C7B"),
    ],
}

PROJETS = [
    {
        "titre": "Analyse de Survie – Cancer de l'Estomac",
        "periode": "2024–2025",
        "tags": ["Python", "scikit-survival", "Kaplan-Meier", "Random Forest"],
        "desc": (
            "Modélisation complète de la survie de patients (cancer de l'estomac). "
            "Comparaison Cox / Kaplan-Meier et ML (RSF, DeepSurv). "
            "Identification des facteurs de risque pour aide à la décision clinique."
        ),
        "icone": "🔬",
        "impact": "C-index > 78%",
    },
    {
        "titre": "Dashboard BI – Trafic Aérien Comorien",
        "periode": "2019",
        "tags": ["Power BI", "SQL", "Excel", "DAX"],
        "desc": (
            "Tableau de bord interactif analysant 12 ans de données du trafic aérien. "
            "KPIs dynamiques, segmentation par routes et périodes, filtres temporels."
        ),
        "icone": "✈️",
        "impact": "12 ans de données · KPIs temps réel",
    },
    {
        "titre": "Pipeline ETL – Indices des Prix (IPC)",
        "periode": "2021",
        "tags": ["Python", "Talend", "SQL", "KoboToolbox"],
        "desc": (
            "Automatisation de la collecte et du traitement des données IPC. "
            "Pipeline ETL Talend pour alimenter des rapports trimestriels standardisés."
        ),
        "icone": "⚙️",
        "impact": "−60% temps de traitement",
    },
    {
        "titre": "Rapport RSES 2024 – Sénégal",
        "periode": "2025",
        "tags": ["Python", "Excel", "Power BI", "Reporting"],
        "desc": (
            "Contribution au Rapport sur la Situation Économique et Sociale du Sénégal 2024. "
            "Collecte multi-sources, consolidation sectorielle, rédaction analytique."
        ),
        "icone": "📋",
        "impact": "Publication nationale officielle",
    },
]

LANGUES = [
    ("Français",    95,  "Courant – professionnel", "🇫🇷"),
    ("Arabe",       80,  "Langue maternelle",        "🇰🇲"),
    ("Anglais",     60,  "Intermédiaire – technique","🇬🇧"),
    ("Shingazidja", 100, "Langue maternelle",        "🌍"),
]

# ─── CSS ────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@300;400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; }

/* Force white */
html, body,
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
.stApp { background: #F8FAFC !important; color: #1E293B !important; font-family: 'DM Sans', sans-serif !important; }
[data-testid="stHeader"]  { display: none !important; }
[data-testid="stSidebar"] { display: none !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ── Hero ── */
.hero {
    background: linear-gradient(150deg, #FFFFFF 0%, #F0F7FF 60%, #EEF2FF 100%);
    border-bottom: 1px solid #E2E8F0;
    padding: 3.5rem 5rem 3rem;
}
.badge {
    display: inline-flex; align-items: center; gap: .45rem;
    background: rgba(14,165,233,.08); border: 1px solid rgba(14,165,233,.22);
    color: #0284C7; font-size: .7rem; font-weight: 600;
    letter-spacing: .14em; text-transform: uppercase;
    padding: .35rem .9rem; border-radius: 100px; margin-bottom: 1.2rem;
}
.badge .dot {
    width: 7px; height: 7px; background: #22C55E; border-radius: 50%;
    box-shadow: 0 0 6px #22C55E; animation: pdot 2s ease-in-out infinite;
}
@keyframes pdot { 0%,100%{opacity:1;transform:scale(1)} 50%{opacity:.4;transform:scale(1.55)} }
.h-name {
    font-family: 'Syne', sans-serif; font-size: 3rem; font-weight: 800;
    color: #0F172A; line-height: 1.08; letter-spacing: -.025em; margin-bottom: .4rem;
}
.h-title { font-family:'Syne',sans-serif; font-size:1.1rem; font-weight:700; color:#0284C7; margin-bottom:1rem; }
.h-quote { font-size:.9rem; color:#64748B; font-style:italic; font-weight:300; margin-bottom:1.3rem; }
.h-bio   { font-size:.9rem; color:#475569; line-height:1.85; margin-bottom:1.8rem; }
.av-ring {
    width:140px; height:140px; border-radius:50%;
    background:linear-gradient(135deg,#0EA5E9,#6366F1);
    padding:3px; box-shadow:0 8px 28px rgba(14,165,233,.18);
    margin:0 auto 0.6rem;
}
.av-inner {
    width:100%;height:100%;border-radius:50%;
    background:linear-gradient(135deg,#EFF6FF,#EEF2FF);
    display:flex;align-items:center;justify-content:center;
    font-family:'Syne',sans-serif;font-size:2.5rem;font-weight:800;color:#0284C7;
}
.loc-tag { text-align:center; font-size:.75rem; color:#94A3B8; }

/* ── Buttons ── */
.cta-row { display:flex; gap:.7rem; flex-wrap:wrap; align-items:center; }
.btn-p {
    display:inline-flex;align-items:center;gap:.4rem;
    background:#0EA5E9;color:#FFF!important;font-weight:700;font-size:.82rem;
    text-decoration:none!important;padding:.65rem 1.4rem;border-radius:8px;
    transition:background .2s,transform .15s;
}
.btn-p:hover { background:#0284C7; transform:translateY(-1px); }
.btn-o {
    display:inline-flex;align-items:center;gap:.4rem;
    background:#FFF;color:#475569!important;font-weight:500;font-size:.82rem;
    text-decoration:none!important;padding:.65rem 1.2rem;border-radius:8px;
    border:1px solid #CBD5E1;transition:border-color .2s,color .2s,transform .15s;
}
.btn-o:hover { border-color:#0EA5E9; color:#0284C7!important; transform:translateY(-1px); }

/* ── Stats band ── */
.stats-band { background:#FFF; border-bottom:1px solid #E2E8F0; }
.stat-cell {
    padding:1.5rem 1rem; text-align:center;
    border-right:1px solid #F1F5F9;
}
.stat-cell:last-child { border-right:none; }
.s-n { font-family:'Syne',sans-serif;font-size:1.9rem;font-weight:800;color:#0284C7; }
.s-l { font-size:.75rem;color:#94A3B8;margin-top:.2rem;letter-spacing:.04em; }

/* ── Section labels ── */
.lbl {
    font-size:.68rem;font-weight:600;letter-spacing:.18em;
    text-transform:uppercase;color:#0EA5E9;margin-bottom:.4rem;
}
.hd {
    font-family:'Syne',sans-serif;font-size:1.75rem;font-weight:700;
    color:#0F172A;margin-bottom:.35rem;letter-spacing:-.01em;
}
.sub { color:#94A3B8;font-size:.87rem;line-height:1.65;margin-bottom:2rem; }

/* ── Timeline card ── */
.tl-card {
    background:#FFF; border:1px solid #E2E8F0; border-radius:14px;
    padding:1.4rem 1.5rem; margin-bottom:1rem;
    border-left:4px solid #E2E8F0;
    transition:box-shadow .2s, transform .2s;
}
.tl-card:hover { box-shadow:0 6px 20px rgba(14,165,233,.07); transform:translateY(-1px); }
.tl-top { display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:.6rem; margin-bottom:.5rem; }
.tl-role { font-family:'Syne',sans-serif; font-size:.97rem; font-weight:700; color:#0F172A; }
.tl-co   { font-size:.84rem; color:#0284C7; font-weight:500; margin:.15rem 0 .1rem; }
.tl-pl   { font-size:.76rem; color:#94A3B8; }
.tl-bdg  {
    background:#F1F5F9;border:1px solid #E2E8F0;color:#64748B;
    font-size:.7rem;padding:.25rem .72rem;border-radius:100px;
    white-space:nowrap;font-weight:500;flex-shrink:0;
}
.tl-li   { font-size:.84rem; color:#475569; line-height:1.75; padding-left:.9rem; position:relative; }
.tl-li::before { content:'▸'; position:absolute; left:0; color:#0EA5E9; font-size:.62rem; top:.35rem; }

/* ── Edu card ── */
.edu-card {
    background:#FFF;border:1px solid #E2E8F0;border-radius:14px;
    padding:1.4rem 1.5rem;position:relative;overflow:hidden;
    transition:border-color .2s,transform .2s,box-shadow .2s;
    margin-bottom:.2rem;
}
.edu-card::before {
    content:'';position:absolute;top:0;left:0;right:0;height:3px;
    background:linear-gradient(90deg,#0EA5E9,#6366F1);
}
.edu-card:hover { border-color:#BAE6FD; transform:translateY(-2px); box-shadow:0 8px 24px rgba(14,165,233,.08); }
.edu-stars { display:flex;gap:.2rem;margin-bottom:.7rem; }
.edu-s      { color:#F59E0B;font-size:.8rem; }
.edu-s.off  { color:#E2E8F0;font-size:.8rem; }
.edu-deg    { font-family:'Syne',sans-serif;font-weight:700;font-size:.9rem;color:#0F172A;margin-bottom:.4rem;line-height:1.35; }
.edu-inst   { font-size:.82rem;color:#0284C7;font-weight:500;margin-bottom:.2rem; }
.edu-meta   { font-size:.74rem;color:#94A3B8; }

/* ── Skill bar ── */
.sk-grp     { font-family:'Syne',sans-serif;font-size:.77rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#0284C7;margin-bottom:1rem;padding-bottom:.45rem;border-bottom:2px solid #EFF6FF; }
.sk-row     { margin-bottom:.85rem; }
.sk-top     { display:flex;justify-content:space-between;margin-bottom:.3rem; }
.sk-nm      { font-size:.82rem;color:#334155;font-weight:500; }
.sk-pc      { font-size:.76rem;color:#94A3B8; }
.sk-bg      { height:6px;background:#F1F5F9;border-radius:100px;overflow:hidden; }
.sk-fill    { height:100%;border-radius:100px; }

/* ── Lang card ── */
.lg-card {
    background:#FFF;border:1px solid #E2E8F0;border-radius:10px;
    padding:1rem 1.2rem;display:flex;align-items:center;gap:.8rem;
    margin-bottom:.2rem;
}
.lg-flag { font-size:1.5rem; }
.lg-nm   { font-weight:600;font-size:.86rem;color:#1E293B; }
.lg-lv   { font-size:.73rem;color:#94A3B8;margin-top:.08rem; }
.lg-bars { display:flex;gap:3px;margin-left:auto; }
.lbar    { width:10px;height:24px;border-radius:3px;background:#F1F5F9; }
.lbar.on { background:#0EA5E9; }

/* ── Project card ── */
.pj-card {
    background:#FFF;border:1px solid #E2E8F0;border-radius:14px;
    padding:1.6rem;position:relative;
    transition:border-color .2s,transform .2s,box-shadow .2s;
    margin-bottom:.2rem;
}
.pj-card:hover { border-color:#BAE6FD;transform:translateY(-2px);box-shadow:0 10px 32px rgba(14,165,233,.08); }
.pj-pd   { font-size:.69rem;color:#94A3B8;font-weight:500;margin-bottom:.7rem; }
.pj-ico  { font-size:1.7rem;margin-bottom:.75rem; }
.pj-ttl  { font-family:'Syne',sans-serif;font-size:.94rem;font-weight:700;color:#0F172A;margin-bottom:.6rem;line-height:1.3; }
.pj-dsc  { font-size:.81rem;color:#64748B;line-height:1.75;margin-bottom:.85rem; }
.pj-imp  {
    display:inline-flex;align-items:center;gap:.3rem;
    background:#F0FDF4;border:1px solid #BBF7D0;color:#16A34A;
    font-size:.71rem;font-weight:600;padding:.23rem .68rem;border-radius:100px;
    margin-bottom:.75rem;
}
.tag-row { display:flex;flex-wrap:wrap;gap:.3rem; }
.tag     { background:#EEF2FF;border:1px solid #C7D2FE;color:#4F46E5;font-size:.68rem;font-weight:500;padding:.2rem .6rem;border-radius:100px; }

/* ── Contact ── */
.ct-item {
    display:flex;align-items:center;gap:.85rem;
    background:#FFF;border:1px solid #E2E8F0;border-radius:10px;
    padding:.85rem 1.1rem;margin-bottom:.7rem;
}
.ct-ico {
    width:36px;height:36px;border-radius:8px;background:#EFF6FF;
    border:1px solid #DBEAFE;display:flex;align-items:center;justify-content:center;font-size:.9rem;flex-shrink:0;
}
.ct-lbl { font-size:.67rem;color:#94A3B8;text-transform:uppercase;letter-spacing:.07em; }
.ct-val { font-size:.84rem;color:#1E293B;font-weight:500; }
.ct-lnk { font-size:.84rem;color:#0284C7;text-decoration:none!important;font-weight:500; }
.ct-lnk:hover { color:#0EA5E9; }
.msg-box { background:#F8FAFF;border:1px solid #DBEAFE;border-radius:14px;padding:1.5rem; }
.msg-ttl { font-family:'Syne',sans-serif;font-size:.9rem;font-weight:700;color:#0F172A;margin-bottom:.9rem; }

/* ── Footer ── */
.footer {
    background:#FFF;border-top:1px solid #E2E8F0;
    padding:2rem 5rem;text-align:center;
    color:#94A3B8;font-size:.76rem;
}
.footer .fn { font-family:'Syne',sans-serif;font-size:.9rem;font-weight:700;color:#334155;margin-bottom:.35rem; }
.footer a   { color:#0284C7;text-decoration:none!important;margin:0 .7rem; }

/* ── Streamlit overrides ── */
[data-baseweb="tab-list"] {
    background:#F1F5F9!important;border:1px solid #E2E8F0!important;
    border-radius:10px!important;padding:3px!important;gap:0!important;
}
[data-baseweb="tab"] {
    border-radius:7px!important;color:#64748B!important;
    font-family:'DM Sans',sans-serif!important;font-size:.8rem!important;
    font-weight:500!important;letter-spacing:.05em!important;
    padding:.55rem 1.2rem!important;background:transparent!important;
}
[aria-selected="true"] {
    background:#FFF!important;color:#0284C7!important;
    box-shadow:0 1px 4px rgba(0,0,0,.07)!important;
}
button[data-testid="baseButton-secondary"] {
    background:#EFF6FF!important;color:#0284C7!important;
    border:1px solid #DBEAFE!important;border-radius:8px!important;
}
.stTextInput input, .stTextArea textarea {
    background:#FFF!important;border:1px solid #E2E8F0!important;
    color:#1E293B!important;border-radius:8px!important;
    font-family:'DM Sans',sans-serif!important;
}
label { color:#475569!important; }
p { color: #1E293B !important; }
</style>
""", unsafe_allow_html=True)


# ─── HERO ───────────────────────────────────────────────────────────────────
col_txt, col_av = st.columns([3, 1])
with col_txt:
    st.markdown(f"""
    <div class="hero">
      <div class="badge"><span class="dot"></span>Disponible · Open to opportunities</div>
      <div class="h-name">{PROFILE['name']}</div>
      <div class="h-title">{PROFILE['title']}</div>
      <div class="h-quote">« {PROFILE['tagline']} »</div>
      <div class="h-bio">{PROFILE['bio']}</div>
      <div class="cta-row">
        <a href="mailto:{PROFILE['email']}" class="btn-p">✉️ Me contacter</a>
        <a href="{PROFILE['linkedin']}" target="_blank" class="btn-o">🔗 LinkedIn</a>
        <a href="{PROFILE['github']}" target="_blank" class="btn-o">💻 GitHub</a>
      </div>
    </div>
    """, unsafe_allow_html=True)

with col_av:
    st.markdown(f"""
    <div style="background:linear-gradient(150deg,#F0F7FF,#EEF2FF);height:100%;
                display:flex;flex-direction:column;align-items:center;
                justify-content:center;padding:2rem 1rem;border-bottom:1px solid #E2E8F0;">
      <div class="av-ring"><div class="av-inner">AS</div></div>
      <div class="loc-tag">📍 {PROFILE['location']}</div>
    </div>
    """, unsafe_allow_html=True)

# ─── STATS ──────────────────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
for col, n, label in zip(
    [c1, c2, c3, c4],
    ["4+", "4", "10+", "3"],
    ["Années études spécialisées", "Expériences professionnelles", "Outils & technologies", "Pays d'expérience"]
):
    col.markdown(f"""
    <div class="stat-cell">
      <div class="s-n">{n}</div>
      <div class="s-l">{label}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr style='border:none;border-top:1px solid #E2E8F0;margin:0;'>", unsafe_allow_html=True)

# ─── TABS ───────────────────────────────────────────────────────────────────
st.markdown("<div style='padding:1.2rem 5rem 0;background:#F8FAFC;'>", unsafe_allow_html=True)
tab_exp, tab_form, tab_sk, tab_proj, tab_ct = st.tabs([
    "  💼  Expérience  ",
    "  🎓  Formation  ",
    "  ⚡  Compétences  ",
    "  🚀  Projets  ",
    "  📬  Contact  ",
])
st.markdown("</div>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# EXPÉRIENCE  — one st.markdown() per card
# ════════════════════════════════════════════════════════════════════════════
with tab_exp:
    st.markdown("<div style='padding:2.5rem 5rem 0;'>", unsafe_allow_html=True)
    st.markdown('<div class="lbl">Parcours professionnel</div>', unsafe_allow_html=True)
    st.markdown('<div class="hd">Expériences</div>', unsafe_allow_html=True)
    st.markdown(
        "<div class='sub'>Des environnements variés — institutionnels, médicaux, aéronautiques — "
        "qui m'ont forgé une vision à 360° de la donnée.</div>",
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='padding:0 5rem 3rem;'>", unsafe_allow_html=True)
    for exp in EXPERIENCES:
        # Build bullet list separately
        bullets = "".join(f'<div class="tl-li">{p}</div>' for p in exp["points"])
        st.markdown(f"""
        <div class="tl-card" style="border-left-color:{exp['couleur']};">
          <div class="tl-top">
            <div>
              <div class="tl-role">{exp['icone']} {exp['titre']}</div>
              <div class="tl-co">{exp['entreprise']}</div>
              <div class="tl-pl">📍 {exp['lieu']}</div>
            </div>
            <div class="tl-bdg">{exp['periode']}</div>
          </div>
          {bullets}
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# FORMATION  — one st.markdown() per card
# ════════════════════════════════════════════════════════════════════════════
with tab_form:
    st.markdown("<div style='padding:2.5rem 5rem 0;'>", unsafe_allow_html=True)
    st.markdown('<div class="lbl">Parcours académique</div>', unsafe_allow_html=True)
    st.markdown('<div class="hd">Formation</div>', unsafe_allow_html=True)
    st.markdown(
        "<div class='sub'>Un cursus rigoureux en mathématiques, statistiques et informatique "
        "décisionnelle, couronné par un Master II spécialisé.</div>",
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='padding:0 5rem 3rem;'>", unsafe_allow_html=True)
    col_a, col_b = st.columns(2)
    for i, f in enumerate(FORMATIONS):
        stars = "".join(
            f'<span class="edu-s{" off" if s > f["niveau"] else ""}">★</span>'
            for s in range(1, 6)
        )
        card_html = f"""
        <div class="edu-card">
          <div class="edu-stars">{stars}</div>
          <div class="edu-deg">{f['diplome']}</div>
          <div class="edu-inst">🏛️ {f['institution']}</div>
          <div class="edu-meta">📍 {f['lieu']} &nbsp;·&nbsp; 📅 {f['periode']}</div>
        </div>
        """
        if i % 2 == 0:
            col_a.markdown(card_html, unsafe_allow_html=True)
        else:
            col_b.markdown(card_html, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# COMPÉTENCES — one st.markdown() per bar
# ════════════════════════════════════════════════════════════════════════════
with tab_sk:
    st.markdown("<div style='padding:2.5rem 5rem 0;'>", unsafe_allow_html=True)
    st.markdown('<div class="lbl">Stack technique</div>', unsafe_allow_html=True)
    st.markdown('<div class="hd">Compétences</div>', unsafe_allow_html=True)
    st.markdown(
        "<div class='sub'>De la collecte à la visualisation, un stack complet orienté BI et Data.</div>",
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='padding:0 5rem;'>", unsafe_allow_html=True)
    groups = list(COMPETENCES.items())
    col1, col2 = st.columns(2)
    for gi, (grp, items) in enumerate(groups):
        target = col1 if gi % 2 == 0 else col2
        target.markdown(f'<div class="sk-grp">{grp}</div>', unsafe_allow_html=True)
        for nm, pct, col in items:
            target.markdown(f"""
            <div class="sk-row">
              <div class="sk-top"><span class="sk-nm">{nm}</span><span class="sk-pc">{pct}%</span></div>
              <div class="sk-bg">
                <div class="sk-fill" style="width:{pct}%;background:linear-gradient(90deg,{col},{col}99);"></div>
              </div>
            </div>""", unsafe_allow_html=True)
        target.markdown("<br>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Langues
    st.markdown("<div style='padding:0 5rem;'>", unsafe_allow_html=True)
    st.markdown('<div class="lbl" style="margin-top:1rem;">Communication</div>', unsafe_allow_html=True)
    st.markdown('<div class="hd" style="font-size:1.3rem;">Langues</div>', unsafe_allow_html=True)
    lc1, lc2 = st.columns(2)
    for i, (nm, pct, desc, flag) in enumerate(LANGUES):
        filled = round(pct / 20)
        bars = "".join(f'<div class="lbar{"  on" if b <= filled else ""}"></div>' for b in range(1, 6))
        card = f"""
        <div class="lg-card">
          <div class="lg-flag">{flag}</div>
          <div><div class="lg-nm">{nm}</div><div class="lg-lv">{desc}</div></div>
          <div class="lg-bars">{bars}</div>
        </div>"""
        (lc1 if i % 2 == 0 else lc2).markdown(card, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<div style='padding-bottom:3rem;'></div>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# PROJETS — one st.markdown() per card
# ════════════════════════════════════════════════════════════════════════════
with tab_proj:
    st.markdown("<div style='padding:2.5rem 5rem 0;'>", unsafe_allow_html=True)
    st.markdown('<div class="lbl">Réalisations</div>', unsafe_allow_html=True)
    st.markdown('<div class="hd">Projets Data & BI</div>', unsafe_allow_html=True)
    st.markdown(
        "<div class='sub'>Projets concrets alliant rigueur statistique, ingénierie de données "
        "et visualisation pour des prises de décision à fort impact.</div>",
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='padding:0 5rem;'>", unsafe_allow_html=True)
    pc1, pc2 = st.columns(2)
    for i, p in enumerate(PROJETS):
        tags = "".join(f'<span class="tag">{t}</span>' for t in p["tags"])
        card = f"""
        <div class="pj-card">
          <div class="pj-pd">{p['periode']}</div>
          <div class="pj-ico">{p['icone']}</div>
          <div class="pj-ttl">{p['titre']}</div>
          <div class="pj-dsc">{p['desc']}</div>
          <div class="pj-imp">✦ {p['impact']}</div>
          <div class="tag-row">{tags}</div>
        </div>"""
        (pc1 if i % 2 == 0 else pc2).markdown(card, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<div style='padding-bottom:3rem;'></div>", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# CONTACT
# ════════════════════════════════════════════════════════════════════════════
with tab_ct:
    st.markdown("<div style='padding:2.5rem 5rem 0;'>", unsafe_allow_html=True)
    st.markdown('<div class="lbl">Restons en contact</div>', unsafe_allow_html=True)
    st.markdown('<div class="hd">Contact</div>', unsafe_allow_html=True)
    st.markdown(
        "<div class='sub'>Disponible pour des opportunités BI / Data Analyst Junior. "
        "N'hésitez pas à me contacter directement.</div>",
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='padding:0 5rem;'>", unsafe_allow_html=True)
    cc1, cc2 = st.columns([1, 1])
    with cc1:
        for ico, lbl, val, href in [
            ("✉️", "Email professionnel", PROFILE["email"], f"mailto:{PROFILE['email']}"),
            ("📱", "Téléphone / WhatsApp", PROFILE["phone"], f"tel:{PROFILE['phone'].replace(' ','')}"),
            ("🔗", "LinkedIn", "linkedin.com/in/sefdineahmed", PROFILE["linkedin"]),
            ("💻", "GitHub", "github.com/sefdineahmed", PROFILE["github"]),
            ("📍", "Localisation", f"{PROFILE['location']} · Remote OK", None),
        ]:
            val_html = (
                f'<a href="{href}" target="_blank" class="ct-lnk">{val}</a>'
                if href else f'<div class="ct-val">{val}</div>'
            )
            st.markdown(f"""
            <div class="ct-item">
              <div class="ct-ico">{ico}</div>
              <div><div class="ct-lbl">{lbl}</div>{val_html}</div>
            </div>""", unsafe_allow_html=True)

    with cc2:
        st.markdown('<div class="msg-box"><div class="msg-ttl">💬 Envoyez-moi un message</div>', unsafe_allow_html=True)
        nom_v   = st.text_input("Votre nom",   placeholder="Marie Dupont",          key="ct_nom")
        email_v = st.text_input("Votre email", placeholder="marie@entreprise.com",  key="ct_email")
        msg_v   = st.text_area("Votre message",placeholder="Bonjour Ahmed, ...",    height=120, key="ct_msg")
        if st.button("📨 Envoyer le message"):
            if nom_v and email_v and msg_v:
                st.success("✅ Message reçu ! Je vous répondrai dans les 24h.")
            else:
                st.warning("Veuillez remplir tous les champs.")
        st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<div style='padding-bottom:3rem;'></div>", unsafe_allow_html=True)


# ─── FOOTER ─────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="footer">
  <div class="fn">Ahmed Sefdine</div>
  <div>Business Intelligence Analyst Junior · Dakar, Sénégal</div>
  <div style="margin-top:.65rem;">
    <a href="mailto:{PROFILE['email']}">✉️ Email</a>
    <a href="{PROFILE['linkedin']}" target="_blank">🔗 LinkedIn</a>
    <a href="{PROFILE['github']}" target="_blank">💻 GitHub</a>
  </div>
  <div style="margin-top:.7rem;color:#CBD5E1;">© {datetime.now().year} Ahmed Sefdine · Fait avec ❤️ &amp; Streamlit</div>
</div>
""", unsafe_allow_html=True)
