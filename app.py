import streamlit as st
from chatbot import get_career_advice
from roi import calculate_roi
from loan import calculate_loan
from timeline import generate_timeline
from admission import predict_admission
from loan_eligibility import estimate_loan_eligibility
from loan_application import get_loan_offer
from profile import get_default_profile, profile_completion_pct, save_profile, load_profile
from gamification import get_badge, get_next_badge, award_xp, XP_REWARDS
from nudges import get_nudges, get_tips
from notifications import get_smart_notifications
from sop import generate_sop
from scholarships import find_scholarships
from email_nudges import get_email_sequence
from charts import donut_chart, gauge_chart, bar_breakdown
import plotly.graph_objects as go
from streaks import update_streak, streak_bonus_xp, streak_emoji
from referral import generate_referral_code, get_referral_link, get_referral_message

st.set_page_config(page_title="EduPath AI", page_icon="🎓", layout="wide")

st.markdown("""
<style>
    /* ── 70% Neutral base ── */
    .stApp { background-color: #0d1117; color: #e2e8f0; }
    html, body, [data-testid="stAppViewContainer"], [data-testid="stAppViewBlockContainer"], section.main, .main .block-container {
        background-color: #0d1117 !important;
        color: #e2e8f0 !important;
    }
    p, li, span, label { color: #94a3b8 !important; }
    h2, h3 { color: #cbd5e1 !important; font-weight: 700; }
    h1 {
        background: linear-gradient(135deg, #ffffff, #a5b4fc) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
        font-weight: 800 !important;
    }
    h2 { border-bottom: 1px solid rgba(79,70,229,0.25) !important; padding-bottom: 6px !important; }

    /* ── 20% Primary — Cards ── */
    .stMetric, div[data-testid="metric-container"] {
        background: rgba(15, 23, 42, 0.7) !important;
        backdrop-filter: blur(12px) !important;
        -webkit-backdrop-filter: blur(12px) !important;
        border: 1px solid rgba(79, 70, 229, 0.2) !important;
        border-radius: 16px !important;
        padding: 1.2rem !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.4), 0 10px 30px rgba(0,0,0,0.3), 0 0 16px rgba(79,70,229,0.07), inset 0 1px 0 rgba(255,255,255,0.04) !important;
        transition: all 0.3s ease !important;
    }
    .stMetric:hover, div[data-testid="metric-container"]:hover {
        background: rgba(15, 23, 42, 0.9) !important;
        box-shadow: 0 8px 16px rgba(0,0,0,0.5), 0 20px 50px rgba(0,0,0,0.4), 0 0 24px rgba(79,70,229,0.18), inset 0 1px 0 rgba(255,255,255,0.07) !important;
        transform: translateY(-4px) scale(1.02) !important;
        border-color: rgba(99,102,241,0.35) !important;
    }

    /* ── 10% Highlight — metric numbers only ── */
    div[data-testid="metric-container"] div[data-testid="stMetricValue"] > div {
        background: linear-gradient(135deg, #818cf8, #c084fc) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
        font-weight: 800 !important;
        font-size: 1.6rem !important;
    }

    /* ── Alert boxes — neutral ── */
    div[data-testid="stAlert"] {
        background: rgba(15, 23, 42, 0.6) !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(255,255,255,0.06) !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 16px rgba(0,0,0,0.3) !important;
        transition: transform 0.2s ease, box-shadow 0.2s ease !important;
    }
    div[data-testid="stAlert"]:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 24px rgba(0,0,0,0.4) !important;
    }

    /* ── Inputs — neutral glass ── */
    .stTextArea textarea, .stNumberInput input, .stTextInput input {
        background: rgba(15, 23, 42, 0.6) !important;
        border: 1px solid rgba(255,255,255,0.07) !important;
        border-radius: 10px !important;
        color: #e2e8f0 !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.3) !important;
        transition: all 0.3s ease;
    }
    .stTextArea textarea:focus, .stNumberInput input:focus, .stTextInput input:focus {
        border: 1px solid rgba(79,70,229,0.5) !important;
        box-shadow: 0 0 12px rgba(79,70,229,0.18), 0 4px 12px rgba(0,0,0,0.4) !important;
        background: rgba(15,23,42,0.8) !important;
    }

    /* ── Selectbox — neutral ── */
    div[data-baseweb="select"] > div {
        background: rgba(15,23,42,0.6) !important;
        border: 1px solid rgba(255,255,255,0.07) !important;
        border-radius: 10px !important;
        transition: all 0.3s ease !important;
    }
    div[data-baseweb="select"] > div:hover {
        border: 1px solid rgba(79,70,229,0.35) !important;
        box-shadow: 0 0 10px rgba(79,70,229,0.12) !important;
    }

    /* ── 20% Primary — Buttons ── */
    .stButton > button {
        background: linear-gradient(135deg, #4f46e5, #7c3aed) !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 0.5rem 1.5rem !important;
        font-weight: 600 !important;
        border: 1px solid rgba(129,140,248,0.2) !important;
        transition: all 0.25s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
        box-shadow: 0 2px 12px rgba(79,70,229,0.25) !important;
        position: relative !important;
        overflow: hidden !important;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #4338ca, #6d28d9) !important;
        box-shadow: 0 4px 20px rgba(79,70,229,0.45) !important;
        transform: translateY(-3px) scale(1.03) !important;
    }
    .stButton > button:active {
        transform: translateY(0px) scale(0.97) !important;
        box-shadow: 0 0 8px rgba(79,70,229,0.3) !important;
        transition: all 0.1s ease !important;
    }
    .stButton > button::after {
        content: "" !important;
        position: absolute !important;
        width: 100% !important; height: 100% !important;
        top: 0 !important; left: 0 !important;
        background: rgba(255,255,255,0.1) !important;
        border-radius: 10px !important;
        opacity: 0 !important;
        transition: opacity 0.4s ease !important;
    }
    .stButton > button:active::after { opacity: 1 !important; transition: opacity 0s !important; }

    /* ── Sidebar — deep neutral ── */
    [data-testid="stSidebar"] {
        background: rgba(5,8,15,0.97) !important;
        backdrop-filter: blur(20px) !important;
        border-right: 1px solid rgba(255,255,255,0.04) !important;
    }
    [data-testid="stSidebar"] * { color: #94a3b8 !important; }
    [data-testid="stSidebar"] strong, [data-testid="stSidebar"] b { color: #e2e8f0 !important; }
    [data-testid="stSidebar"] .stButton > button {
        background: transparent !important;
        border: 1px solid rgba(255,255,255,0.06) !important;
        box-shadow: none !important;
        color: #94a3b8 !important;
        transition: all 0.2s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
    }
    [data-testid="stSidebar"] .stButton > button:hover {
        background: rgba(79,70,229,0.12) !important;
        border-color: rgba(79,70,229,0.25) !important;
        color: #e2e8f0 !important;
        transform: translateX(4px) !important;
    }
    [data-testid="stSidebar"] .stButton > button:active {
        transform: translateX(2px) scale(0.98) !important;
        transition: all 0.1s ease !important;
    }

    /* ── 10% Highlight — progress bars ── */
    div[data-testid="stProgressBar"] > div > div {
        background: linear-gradient(90deg, #4f46e5, #7c3aed, #c084fc) !important;
        border-radius: 999px !important;
    }

    /* ── Hero — neutral dark ── */
    .hero {
        background: linear-gradient(135deg, #0f172a, #1e1b4b) !important;
        border-radius: 16px; padding: 2rem; margin-bottom: 1.5rem;
        border: 1px solid rgba(79,70,229,0.12) !important;
        box-shadow: 0 8px 32px rgba(0,0,0,0.5), 0 0 30px rgba(79,70,229,0.06), inset 0 1px 0 rgba(255,255,255,0.03);
        animation: fadeSlideIn 0.8s ease forwards;
    }

    /* ── Animations ── */
    @keyframes fadeSlideIn {
        from { opacity: 0; transform: translateY(16px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    .block-container { animation: fadeSlideIn 0.6s ease forwards; }

    /* ── Dividers — subtle neutral ── */
    hr { border: none !important; height: 1px !important; background: rgba(255,255,255,0.05) !important; margin: 1.5rem 0 !important; }

    /* ── Expanders ── */
    div[data-testid="stExpander"] {
        background: rgba(15,23,42,0.5) !important;
        border: 1px solid rgba(255,255,255,0.05) !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3) !important;
    }
    div[data-testid="stVerticalBlock"] > div { transition: all 0.2s ease; }
</style>
""", unsafe_allow_html=True)

# ── Init session state ────────────────────────────────────
if "profile" not in st.session_state:
    st.session_state.profile = load_profile()
if "xp" not in st.session_state:
    st.session_state.xp = 0
if "tools_used" not in st.session_state:
    st.session_state.tools_used = set()
if "streak" not in st.session_state:
    st.session_state.streak = {"last_visit": None, "count": 0, "longest": 0}
if "referral_bonus_claimed" not in st.session_state:
    st.session_state.referral_bonus_claimed = False

# Update streak on every session load
updated = update_streak(st.session_state.streak)
if updated["count"] != st.session_state.streak.get("count") or updated["last_visit"] != st.session_state.streak.get("last_visit"):
    bonus = streak_bonus_xp(updated["count"])
    if bonus:
        st.session_state.xp += bonus
    st.session_state.streak = updated

# ── Smart Notifications (shown on every page) ─────────────
def show_notifications():
    loan_result = st.session_state.get("last_loan_result")
    notifs = get_smart_notifications(
        st.session_state.profile,
        st.session_state.xp,
        st.session_state.tools_used,
        loan_result
    )
    if notifs:
        for ntype, msg in notifs:
            if ntype == "warning":   st.warning(msg)
            elif ntype == "error":   st.error(msg)
            elif ntype == "success": st.success(msg)
            else:                    st.info(msg)

TOOLS_WITH_HISTORY = ["💬 Career Navigator", "🎯 Admission Predictor", "📅 AI Timeline Generator"]
for tool in TOOLS_WITH_HISTORY:
    if f"convs_{tool}" not in st.session_state:
        st.session_state[f"convs_{tool}"] = []
    if f"active_{tool}" not in st.session_state:
        st.session_state[f"active_{tool}"] = None

def award(tool):
    if tool not in st.session_state.tools_used:
        st.session_state.xp += award_xp(tool)
        st.session_state.tools_used.add(tool)

# ── Sidebar ───────────────────────────────────────────────
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/graduation-cap.png", width=60)
    st.title("EduPath AI")
    st.caption("Your AI-powered study abroad companion")
    st.divider()

    # XP & Badge
    badge = get_badge(st.session_state.xp)
    next_badge = get_next_badge(st.session_state.xp)
    streak = st.session_state.streak
    st.markdown(f"**{badge['name']}** — {st.session_state.xp} XP")
    st.markdown(f"{streak_emoji(streak['count'])} **{streak['count']}-day streak** | Best: {streak['longest']}")
    if next_badge:
        progress_val = min(st.session_state.xp, next_badge["min_xp"])
        st.progress(int((progress_val / next_badge["min_xp"]) * 100),
                    text=f"Next: {next_badge['name']} at {next_badge['min_xp']} XP")
    st.divider()

    menu = st.selectbox("Navigate", [
        "🏠 Home",
        "👤 My Profile",
        "💬 Career Navigator",
        "🎯 Admission Predictor",
        "📈 ROI Calculator",
        "📅 AI Timeline Generator",
        "🏦 Loan EMI Calculator",
        "💳 Loan Eligibility",
        "📋 Loan Application",
        "🎓 SOP Generator",
        "🏆 Scholarship Finder",
        "📧 Email Nudge Simulator",
        "🎁 Rewards & Referral",
    ])

    if menu in TOOLS_WITH_HISTORY:
        st.divider()
        key = f"convs_{menu}"
        active_key = f"active_{menu}"
        col1, col2 = st.columns(2)
        with col1:
            if st.button("➕ New Chat", use_container_width=True):
                st.session_state[active_key] = None
                st.rerun()
        with col2:
            if st.button("🗑️ Clear All", use_container_width=True):
                st.session_state[key] = []
                st.session_state[active_key] = None
                st.rerun()
        if st.session_state[key]:
            st.markdown("**History**")
            for i, conv in enumerate(reversed(st.session_state[key])):
                idx = len(st.session_state[key]) - 1 - i
                if st.button(f"💬 {conv['title']}", key=f"{menu}_conv_{idx}", use_container_width=True):
                    st.session_state[active_key] = idx
                    st.rerun()

    st.divider()
    st.caption("Built for Indian students planning higher education.")


# ── Helper: chat UI ───────────────────────────────────────
def render_chat_ui(tool_key, placeholder, ai_fn):
    key = f"convs_{tool_key}"
    active_key = f"active_{tool_key}"
    active = st.session_state[active_key]

    if active is not None:
        current_msgs = st.session_state[key][active]["messages"]
        st.caption(f"📂 {st.session_state[key][active]['title']}")
    else:
        current_msgs = []
        st.caption("New conversation — type below to get started.")

    for msg in current_msgs:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input(placeholder)
    if user_input:
        if st.session_state[active_key] is None:
            title = user_input[:45] + ("..." if len(user_input) > 45 else "")
            st.session_state[key].append({"title": title, "messages": []})
            st.session_state[active_key] = len(st.session_state[key]) - 1

        idx = st.session_state[active_key]
        msgs = st.session_state[key][idx]["messages"]
        msgs.append({"role": "user", "content": user_input})

        with st.chat_message("user"):
            st.markdown(user_input)
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = ai_fn(user_input, msgs)
            st.markdown(response)

        msgs.append({"role": "assistant", "content": response})
        award(tool_key)
        st.rerun()


# ── Home ──────────────────────────────────────────────────
if menu == "🏠 Home":
    p = st.session_state.profile
    name = p.get("name") or "Student"
    show_notifications()

    st.markdown(f"""
    <div class='hero'>
        <h1>👋 Welcome, {name}</h1>
        <p style='font-size:1.1rem; color:#a5b4fc;'>Helping students make smart career and financial decisions using AI</p>
    </div>
    """, unsafe_allow_html=True)

    # Profile completion bar
    pct = profile_completion_pct(p)
    st.write("**Profile Completion**")
    st.progress(pct, text=f"{pct}% complete — finish your profile to unlock personalized advice")

    # Smart nudges
    nudges = get_nudges(p, st.session_state.xp, st.session_state.tools_used)
    if nudges:
        st.divider()
        st.markdown("### 💡 Recommended Next Steps")
        for icon, msg in nudges:
            st.info(f"{icon} {msg}")

    # Country tips
    country = p.get("target_country", "")
    if country:
        st.divider()
        st.markdown(f"### 🌍 Tips for Studying in {country}")
        for tip in get_tips(country):
            st.success(tip)

    st.divider()
    st.markdown("### 🛠️ All Tools")

    st.markdown("""
    <style>
    .cards-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1.5rem;
        margin-top: 1rem;
    }
    .flip-card {
        background: transparent;
        width: 100%;
        height: 180px;
        perspective: 1000px;
        cursor: pointer;
    }
    .flip-card-inner {
        position: relative;
        width: 100%;
        height: 100%;
        transition: transform 0.7s cubic-bezier(0.4, 0.2, 0.2, 1);
        transform-style: preserve-3d;
    }
    .flip-card:hover .flip-card-inner { transform: rotateY(180deg); }
    .flip-card-front, .flip-card-back {
        position: absolute;
        width: 100%; height: 100%;
        border-radius: 16px;
        backface-visibility: hidden;
        -webkit-backface-visibility: hidden;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 1.5rem;
        box-sizing: border-box;
    }
    .flip-card-front {
        background: rgba(15, 23, 42, 0.85);
        border: 1px solid rgba(79, 70, 229, 0.25);
        box-shadow: 0 4px 24px rgba(0,0,0,0.4), 0 0 16px rgba(79,70,229,0.08);
    }
    .flip-card-back {
        background: linear-gradient(135deg, #1e1b4b, #312e81);
        border: 1px solid rgba(129, 140, 248, 0.35);
        box-shadow: 0 4px 24px rgba(79,70,229,0.25);
        transform: rotateY(180deg);
        text-align: center;
    }
    .flip-card-front .icon { font-size: 2.4rem; margin-bottom: 0.6rem; }
    .flip-card-front .title { color: #e2e8f0; font-size: 1rem; font-weight: 700; text-align: center; }
    .flip-card-back .back-title { color: #a5b4fc; font-size: 0.78rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 0.5rem; }
    .flip-card-back .back-desc { color: #e2e8f0; font-size: 0.9rem; line-height: 1.5; }
    .flip-card-back .hint { margin-top: 0.8rem; color: #818cf8; font-size: 0.76rem; }
    </style>

    <div class="cards-grid">
        <div class="flip-card"><div class="flip-card-inner">
            <div class="flip-card-front"><div class="icon">💬</div><div class="title">Career Navigator</div></div>
            <div class="flip-card-back"><div class="back-title">AI Chat</div><div class="back-desc">AI-powered career advice tailored to your skills, interests, and goals.</div><div class="hint">→ Navigate via sidebar</div></div>
        </div></div>
        <div class="flip-card"><div class="flip-card-inner">
            <div class="flip-card-front"><div class="icon">🎯</div><div class="title">Admission Predictor</div></div>
            <div class="flip-card-back"><div class="back-title">AI Prediction</div><div class="back-desc">Know your admission chances at top universities before you apply.</div><div class="hint">→ Navigate via sidebar</div></div>
        </div></div>
        <div class="flip-card"><div class="flip-card-inner">
            <div class="flip-card-front"><div class="icon">📈</div><div class="title">ROI Calculator</div></div>
            <div class="flip-card-back"><div class="back-title">Financial Tool</div><div class="back-desc">Calculate if your dream course is worth the investment with salary projections.</div><div class="hint">→ Navigate via sidebar</div></div>
        </div></div>
        <div class="flip-card"><div class="flip-card-inner">
            <div class="flip-card-front"><div class="icon">📅</div><div class="title">Timeline Generator</div></div>
            <div class="flip-card-back"><div class="back-title">AI Planner</div><div class="back-desc">Month-by-month action plan covering exams, SOP, visa steps and deadlines.</div><div class="hint">→ Navigate via sidebar</div></div>
        </div></div>
        <div class="flip-card"><div class="flip-card-inner">
            <div class="flip-card-front"><div class="icon">🏦</div><div class="title">Loan EMI Calculator</div></div>
            <div class="flip-card-back"><div class="back-title">Financial Tool</div><div class="back-desc">Full repayment breakdown with principal vs interest split and affordability check.</div><div class="hint">→ Navigate via sidebar</div></div>
        </div></div>
        <div class="flip-card"><div class="flip-card-inner">
            <div class="flip-card-front"><div class="icon">💳</div><div class="title">Loan Eligibility</div></div>
            <div class="flip-card-back"><div class="back-title">Loan Tool</div><div class="back-desc">Check how much education loan you qualify for based on your financial profile.</div><div class="hint">→ Navigate via sidebar</div></div>
        </div></div>
    </div>
    """, unsafe_allow_html=True)

# ── My Profile ────────────────────────────────────────────
elif menu == "👤 My Profile":
    st.subheader("👤 My Profile")
    st.write("Complete your profile to get personalized advice across all tools.")

    p = st.session_state.profile
    pct = profile_completion_pct(p)
    st.progress(pct, text=f"{pct}% complete")
    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        p["name"] = st.text_input("Full Name", value=p.get("name", ""), placeholder="e.g. Rahul Sharma")
        p["degree"] = st.selectbox("Current Degree", ["", "B.Tech / B.E.", "B.Sc", "BCA", "BBA / B.Com", "Other"],
                                   index=["", "B.Tech / B.E.", "B.Sc", "BCA", "BBA / B.Com", "Other"].index(p.get("degree", "")))
        p["gpa"] = st.text_input("GPA / Percentage", value=p.get("gpa", ""), placeholder="e.g. 8.2 CGPA or 78%")
        p["work_exp"] = st.selectbox("Work Experience", ["0 years", "1 year", "2 years", "3+ years"],
                                     index=["0 years", "1 year", "2 years", "3+ years"].index(p.get("work_exp", "0 years")))
    with col2:
        p["target_program"] = st.text_input("Target Program", value=p.get("target_program", ""), placeholder="e.g. MS in Data Science")
        p["target_country"] = st.selectbox("Target Country", ["", "USA", "UK", "Canada", "Germany", "Australia", "Other"],
                                           index=["", "USA", "UK", "Canada", "Germany", "Australia", "Other"].index(p.get("target_country", "")))
        p["budget"] = st.text_input("Total Budget (₹)", value=p.get("budget", ""), placeholder="e.g. ₹40,00,000")
        p["timeline"] = st.selectbox("Target Intake", ["", "Fall 2025", "Spring 2026", "Fall 2026", "Spring 2027"],
                                     index=["", "Fall 2025", "Spring 2026", "Fall 2026", "Spring 2027"].index(p.get("timeline", "")))

    p["english_score"] = st.text_input("IELTS / TOEFL Score (optional)", value=p.get("english_score", ""), placeholder="e.g. IELTS 7.0")
    p["gre_score"] = st.text_input("GRE Score (optional)", value=p.get("gre_score", ""), placeholder="e.g. 320")

    if st.button("Save Profile", type="primary"):
        st.session_state.profile = p
        save_profile(p)
        new_pct = profile_completion_pct(p)
        if new_pct == 100 and not p.get("completed"):
            st.session_state.profile["completed"] = True
            award("profile_complete")
            st.balloons()
            st.success("🎉 Profile complete! You earned 50 XP.")
        else:
            st.success(f"Profile saved. {new_pct}% complete.")
        st.rerun()

    # Show country tips if target country is set
    if p.get("target_country"):
        st.divider()
        st.markdown(f"### 🌍 Tips for {p['target_country']}")
        for tip in get_tips(p["target_country"]):
            st.success(tip)

# ── Career Navigator ──────────────────────────────────────
elif menu == "💬 Career Navigator":
    st.subheader("💬 AI Career Navigator")
    show_notifications()
    render_chat_ui("💬 Career Navigator", "Ask about careers, universities, courses...", get_career_advice)

# ── Admission Predictor ───────────────────────────────────
elif menu == "🎯 Admission Predictor":
    st.subheader("🎯 Admission Probability Predictor")
    show_notifications()
    p = st.session_state.profile

    col1, col2 = st.columns(2)
    with col1:
        degree = st.selectbox("Degree", ["B.Tech / B.E.", "B.Sc", "BCA", "BBA / B.Com", "Other"],
                              index=["B.Tech / B.E.", "B.Sc", "BCA", "BBA / B.Com", "Other"].index(p.get("degree") or "B.Tech / B.E.") if p.get("degree") else 0)
        gpa = st.text_input("GPA / Percentage", value=p.get("gpa", ""), placeholder="e.g. 8.2 CGPA")
        program = st.text_input("Target Program", value=p.get("target_program", ""), placeholder="e.g. MS in Computer Science")
        country = st.selectbox("Target Country", ["USA", "UK", "Canada", "Germany", "Australia", "Other"],
                               index=["USA", "UK", "Canada", "Germany", "Australia", "Other"].index(p.get("target_country") or "USA") if p.get("target_country") in ["USA", "UK", "Canada", "Germany", "Australia", "Other"] else 0)
    with col2:
        gre = st.text_input("GRE Score (optional)", value=p.get("gre_score", ""), placeholder="e.g. 320")
        english = st.text_input("IELTS / TOEFL (optional)", value=p.get("english_score", ""), placeholder="e.g. IELTS 7.0")
        work_exp = st.selectbox("Work Experience", ["0 years", "1 year", "2 years", "3+ years"],
                                index=["0 years", "1 year", "2 years", "3+ years"].index(p.get("work_exp", "0 years")))
        research = st.text_input("Research / Publications (optional)", placeholder="e.g. 1 paper published")

    extras = st.text_area("Projects / Extracurriculars (optional)", placeholder="e.g. Built 3 ML projects, hackathon winner")

    if st.button("Predict My Chances", type="primary"):
        if gpa and program:
            profile_data = {"degree": degree, "gpa": gpa, "program": program, "country": country,
                            "gre": gre, "english": english, "work_exp": work_exp,
                            "research": research, "extras": extras}
            with st.spinner("Evaluating your profile..."):
                result = predict_admission(profile_data)

            key = "convs_🎯 Admission Predictor"
            active_key = "active_🎯 Admission Predictor"
            title = f"{program[:30]} — {country}"
            st.session_state[key].append({"title": title, "messages": [
                {"role": "user", "content": f"{gpa} GPA | {program} | {country}"},
                {"role": "assistant", "content": result}
            ]})
            st.session_state[active_key] = len(st.session_state[key]) - 1
            award("Admission Predictor")
            st.divider()
            st.markdown(result)
        else:
            st.warning("Please fill in at least your GPA and target program.")

    # Load from history
    key = "convs_🎯 Admission Predictor"
    active_key = "active_🎯 Admission Predictor"
    active = st.session_state[active_key]
    if active is not None and st.session_state[key]:
        conv = st.session_state[key][active]
        if conv["messages"]:
            st.divider()
            st.caption(f"📂 Viewing saved: {conv['title']}")
            st.markdown(conv["messages"][-1]["content"])

# ── ROI Calculator ────────────────────────────────────────
elif menu == "📈 ROI Calculator":
    st.subheader("📈 Course ROI Calculator")
    col1, col2 = st.columns(2)
    with col1:
        cost = st.number_input("Course Cost (₹)", min_value=0.0, step=1000.0)
        st.caption("e.g. ₹50,000 for an online bootcamp")
    with col2:
        salary = st.number_input("Expected Salary After Course (₹/year)", min_value=0.0, step=10000.0)
        st.caption("e.g. ₹600,000 for a fresher role")
    col3, col4 = st.columns(2)
    with col3:
        current_salary = st.number_input("Current Salary (₹/year)", min_value=0.0, step=10000.0)
        st.caption("Enter 0 if you're a fresher")
    with col4:
        duration_years = st.slider("Career Duration to Measure (years)", min_value=1, max_value=10, value=3)

    if st.button("Calculate ROI", type="primary"):
        if cost > 0 and salary > 0:
            result = calculate_roi(cost, salary, duration_years, current_salary)
            award("ROI Calculator")
            st.divider()
            col1, col2, col3 = st.columns(3)
            col1.metric("ROI", f"{result['roi']}%")
            col2.metric("Net Gain", f"₹{result['net_gain']:,.0f}")
            col3.metric("Monthly Salary Boost", f"₹{result['monthly_gain']:,.0f}")
            col4, col5 = st.columns(2)
            if result["payback_months"]: col4.metric("Payback Period", f"{result['payback_months']} months")
            if result["salary_growth"]: col5.metric("Salary Growth", f"{result['salary_growth']}%")
            st.divider()
            roi = result["roi"]
            col_g, col_s = st.columns([1, 2])
            with col_g:
                st.plotly_chart(gauge_chart(min(max(roi, 0), 100), "ROI Score"), use_container_width=True)
            with col_s:
                if roi >= 500: st.success("Exceptional ROI. This course is a no-brainer investment.")
                elif roi >= 100: st.success("Strong ROI. The course pays for itself well.")
                elif roi >= 0: st.info("Moderate return. Consider the long-term career benefits too.")
                else: st.error("Negative ROI. You may want to reconsider this course.")
                st.metric("Actual ROI", f"{roi}%")
        else:
            st.warning("Please enter a valid course cost and expected salary.")

# ── Timeline Generator ────────────────────────────────────
elif menu == "📅 AI Timeline Generator":
    st.subheader("📅 AI Timeline Generator")
    show_notifications()
    p = st.session_state.profile

    goal = st.text_input("What is your goal?",
                         value=f"Study {p.get('target_program','')} in {p.get('target_country','')}".strip(" in") if p.get("target_program") else "",
                         placeholder="e.g. Study MS in Computer Science in the USA")
    col1, col2 = st.columns(2)
    with col1:
        start_month = st.selectbox("Starting Month", ["January","February","March","April","May","June",
                                                       "July","August","September","October","November","December"])
    with col2:
        duration_months = st.slider("Plan Duration (months)", min_value=3, max_value=18, value=12)
    extras = st.text_area("Additional context (optional)",
                          value=f"GRE: {p.get('gre_score','')} | IELTS: {p.get('english_score','')} | Budget: {p.get('budget','')} | Intake: {p.get('timeline','')}".strip(" | ") if p.get("gre_score") or p.get("budget") else "",
                          placeholder="e.g. GRE 320, targeting Fall 2026, budget ₹30L")

    if st.button("Generate Timeline", type="primary"):
        if goal.strip():
            with st.spinner("Building your personalized timeline..."):
                timeline = generate_timeline(goal, start_month, duration_months, extras)

            key = "convs_📅 AI Timeline Generator"
            active_key = "active_📅 AI Timeline Generator"
            st.session_state[key].append({"title": goal[:45], "messages": [
                {"role": "user", "content": f"Goal: {goal} | Start: {start_month} | {duration_months}mo"},
                {"role": "assistant", "content": timeline}
            ]})
            st.session_state[active_key] = len(st.session_state[key]) - 1
            award("AI Timeline Generator")
            st.divider()
            st.markdown(timeline)
        else:
            st.warning("Please enter your goal first.")

    key = "convs_📅 AI Timeline Generator"
    active_key = "active_📅 AI Timeline Generator"
    active = st.session_state[active_key]
    if active is not None and st.session_state[key] and not goal.strip():
        conv = st.session_state[key][active]
        if conv["messages"]:
            st.divider()
            st.caption(f"📂 Viewing: {conv['title']}")
            st.markdown(conv["messages"][-1]["content"])

# ── Loan EMI Calculator ───────────────────────────────────
elif menu == "🏦 Loan EMI Calculator":
    st.subheader("🏦 Student Loan EMI Calculator")
    col1, col2, col3 = st.columns(3)
    with col1:
        P = st.number_input("Loan Amount (₹)", min_value=0.0, step=10000.0)
        st.caption("e.g. ₹1,500,000")
    with col2:
        R = st.number_input("Interest Rate (% per year)", min_value=0.0, step=0.1)
        st.caption("e.g. 10.5% for education loans")
    with col3:
        N = st.number_input("Duration (months)", min_value=1.0, step=1.0)
        st.caption("e.g. 84 months = 7 years")

    if st.button("Calculate EMI", type="primary"):
        if P > 0 and R > 0 and N > 0:
            result = calculate_loan(P, R, N)
            award("Loan EMI Calculator")
            st.divider()
            col1, col2, col3 = st.columns(3)
            col1.metric("Monthly EMI", f"₹{result['emi']:,.2f}")
            col2.metric("Total Payment", f"₹{result['total_payment']:,.2f}")
            col3.metric("Total Interest", f"₹{result['total_interest']:,.2f}")
            col4, col5 = st.columns(2)
            col4.metric("Principal Amount", f"₹{result['principal']:,.2f}")
            col5.metric("Loan Duration", f"{int(N)} months ({round(N/12, 1)} years)")
            st.divider()
            st.write("📊 Payment Breakdown")
            st.plotly_chart(bar_breakdown(
                ["Principal", "Interest"],
                [result['principal_ratio'], result['interest_ratio']],
                ["#4f46e5", "#7c3aed"]
            ), use_container_width=True)
            st.divider()
            monthly_income_needed = result['emi'] * 3
            st.info(f"💡 To comfortably afford this EMI, you'd need a monthly income of at least ₹{monthly_income_needed:,.0f} (EMI ≤ 33% of income rule).")
            if result['interest_ratio'] > 40: st.warning("High interest burden. Consider a shorter duration or larger down payment.")
            else: st.success("Reasonable interest-to-principal ratio. This looks manageable.")
        else:
            st.warning("Please fill in all fields with valid values.")

# ── Loan Eligibility ──────────────────────────────────────
elif menu == "💳 Loan Eligibility":
    st.subheader("💳 Education Loan Eligibility Estimator")
    show_notifications()
    col1, col2 = st.columns(2)
    with col1:
        annual_income = st.number_input("Your Annual Income (₹)", min_value=0.0, step=50000.0)
        st.caption("Enter 0 if you're a student with no income")
        co_income = st.number_input("Co-applicant Annual Income (₹)", min_value=0.0, step=50000.0)
        st.caption("Parent / guardian income")
        existing_emi = st.number_input("Existing Monthly EMI Obligations (₹)", min_value=0.0, step=1000.0)
        st.caption("Any current loan EMIs being paid")
    with col2:
        credit_score = st.slider("Credit Score (Co-applicant)", min_value=300, max_value=900, value=720)
        st.caption("750+ = Excellent, 700–749 = Good, 650–699 = Fair, <650 = Poor")
        loan_amount = st.number_input("Loan Amount Required (₹)", min_value=0.0, step=100000.0)
        st.caption("e.g. ₹2,000,000 for MS abroad")
        course_duration = st.selectbox("Course Duration", ["1 year", "2 years", "3 years", "4 years"])

    if st.button("Check Eligibility", type="primary"):
        if loan_amount > 0 and (annual_income + co_income) > 0:
            duration_years = int(course_duration.split()[0])
            result = estimate_loan_eligibility(annual_income, co_income, existing_emi,
                                               credit_score, loan_amount, duration_years)
            award("Loan Eligibility")
            st.session_state["last_loan_result"] = result
            st.session_state["last_loan_amount"] = loan_amount
            st.divider()
            col1, col2, col3 = st.columns(3)
            col1.metric("Max Eligible Loan", f"₹{result['max_loan']:,.0f}")
            col2.metric("Interest Rate", f"{result['interest_rate']}%")
            col3.metric("Credit Rating", result['credit_label'])
            col4, col5 = st.columns(2)
            col4.metric("Max Affordable EMI", f"₹{result['max_emi_allowed']:,.0f}")
            col5.metric("Repayment Period", f"{result['repayment_months']} months")
            st.divider()
            col_d, col_info = st.columns([1, 2])
            with col_d:
                st.plotly_chart(donut_chart(result['coverage_pct'], "Loan Coverage"), use_container_width=True)
            with col_info:
                if result['eligible']:
                    st.success(f"✅ You are eligible for the full loan amount of ₹{loan_amount:,.0f}.")
                    st.info("👉 Head to **Loan Application** in the sidebar to get your personalized offer and apply.")
                else:
                    shortfall = loan_amount - result['max_loan']
                    st.error(f"⚠️ You qualify for ₹{result['max_loan']:,.0f} but need ₹{loan_amount:,.0f}. Shortfall: ₹{shortfall:,.0f}.")
                    st.info("💡 Tips: Add a co-applicant with higher income, reduce existing EMIs, or improve credit score.")
            st.divider()
            st.markdown("### 📋 Document Checklist")
            st.markdown("""
- ✅ Admission letter from university
- ✅ Fee structure / cost of attendance document
- ✅ KYC documents (Aadhaar, PAN) — student & co-applicant
- ✅ Last 3 years ITR — co-applicant
- ✅ Last 6 months bank statements — co-applicant
- ✅ Academic marksheets (10th, 12th, graduation)
- ✅ Collateral documents (if loan > ₹7.5L)
- ✅ Passport copy (for abroad studies)
            """)
        else:
            st.warning("Please enter the loan amount and at least one income source.")

# ── Loan Application ──────────────────────────────────────
elif menu == "📋 Loan Application":
    st.subheader("📋 AI-Assisted Loan Application")
    st.write("Complete your loan application step by step. Your profile is pre-filled where available.")
    p = st.session_state.profile

    st.divider()
    st.markdown("### Step 1 — Personal Details")
    col1, col2 = st.columns(2)
    with col1:
        app_name = st.text_input("Full Name", value=p.get("name", ""), placeholder="As per Aadhaar")
        app_dob = st.text_input("Date of Birth", placeholder="DD/MM/YYYY")
        app_phone = st.text_input("Mobile Number", placeholder="10-digit number")
    with col2:
        app_email = st.text_input("Email Address", placeholder="your@email.com")
        app_city = st.text_input("City", placeholder="e.g. Mumbai")
        app_pan = st.text_input("PAN Number", placeholder="e.g. ABCDE1234F")

    st.divider()
    st.markdown("### Step 2 — Academic & Course Details")
    col1, col2 = st.columns(2)
    with col1:
        app_degree = st.text_input("Completed Degree", value=p.get("degree", ""), placeholder="e.g. B.Tech Computer Science")
        app_gpa = st.text_input("GPA / Percentage", value=p.get("gpa", ""), placeholder="e.g. 8.2 CGPA")
        app_university = st.text_input("Admitted University", placeholder="e.g. University of Texas at Austin")
    with col2:
        app_program = st.text_input("Program", value=p.get("target_program", ""), placeholder="e.g. MS in Data Science")
        app_country = st.text_input("Country", value=p.get("target_country", ""), placeholder="e.g. USA")
        app_intake = st.text_input("Intake", value=p.get("timeline", ""), placeholder="e.g. Fall 2026")

    st.divider()
    st.markdown("### Step 3 — Financial Details")
    col1, col2 = st.columns(2)
    with col1:
        app_loan = st.number_input("Loan Amount Required (₹)", min_value=0.0, step=100000.0)
        st.caption("e.g. ₹2,000,000")
        app_co_name = st.text_input("Co-applicant Name", placeholder="Parent / Guardian name")
        app_co_income = st.number_input("Co-applicant Annual Income (₹)", min_value=0.0, step=50000.0)
    with col2:
        app_course_cost = st.text_input("Total Course Cost", value=p.get("budget", ""), placeholder="e.g. ₹35,00,000")
        app_co_relation = st.selectbox("Co-applicant Relation", ["Father", "Mother", "Spouse", "Sibling", "Other"])
        app_collateral = st.selectbox("Collateral Available?", ["Yes — Property", "Yes — FD/Insurance", "No"])

    st.divider()
    st.markdown("### Step 4 — Declaration")
    consent = st.checkbox("I confirm that all information provided is accurate and I consent to a credit check.")

    if st.button("Submit Application & Get Loan Offer", type="primary"):
        if not consent:
            st.warning("Please accept the declaration to proceed.")
        elif not app_name or not app_loan or not app_program:
            st.warning("Please fill in Name, Loan Amount, and Program at minimum.")
        else:
            last_result = st.session_state.get("last_loan_result")
            interest_rate = last_result["interest_rate"] if last_result else 11.0
            credit_label = last_result["credit_label"] if last_result else "Good"

            with st.spinner("Processing your application and generating your offer..."):
                offer = get_loan_offer(p, app_loan, credit_label, interest_rate)

            award("Loan Application")
            st.balloons()
            st.divider()
            st.success("✅ Application submitted successfully! Here is your personalized loan offer:")
            st.markdown(offer)
            st.divider()
            st.markdown("### 📋 Document Checklist — Upload Ready")
            st.markdown("""
- ☐ Admission letter from university
- ☐ Fee structure document
- ☐ Aadhaar & PAN — student & co-applicant
- ☐ Last 3 years ITR — co-applicant
- ☐ Last 6 months bank statements
- ☐ Academic marksheets (10th, 12th, graduation)
- ☐ Collateral documents (if applicable)
- ☐ Passport copy
            """)

# ── Rewards & Referral ────────────────────────────────────
elif menu == "🎁 Rewards & Referral":
    st.subheader("🎁 Rewards & Referral")
    p = st.session_state.profile
    streak = st.session_state.streak

    # ── Streak Card ──
    st.markdown("### 🔥 Your Streak")
    col1, col2, col3 = st.columns(3)
    col1.metric("Current Streak", f"{streak_emoji(streak['count'])} {streak['count']} days")
    col2.metric("Longest Streak", f"{streak['longest']} days")
    col3.metric("Total XP", f"{st.session_state.xp} XP")

    st.info("💡 Visit EduPath AI every day to keep your streak alive and earn bonus XP — 3 days = +20 XP, 7 days = +50 XP, every 10 days = +100 XP!")

    st.divider()

    # ── Badge Progress ──
    st.markdown("### 🏆 Badge Journey")
    from gamification import BADGES
    badge_cols = st.columns(len(BADGES))
    for i, b in enumerate(BADGES):
        with badge_cols[i]:
            earned = st.session_state.xp >= b["min_xp"]
            st.markdown(f"{'✅' if earned else '🔒'} **{b['name']}**")
            st.caption(f"{b['desc']}\n{b['min_xp']} XP")

    st.divider()

    # ── XP Breakdown ──
    st.markdown("### 📊 How to Earn XP")
    xp_data = {
        "Complete Profile": 50,
        "Use Career Navigator": 20,
        "Use Admission Predictor": 30,
        "Use ROI Calculator": 20,
        "Generate Timeline": 30,
        "Check Loan EMI": 15,
        "Check Loan Eligibility": 25,
        "Submit Loan Application": 50,
        "3-Day Streak Bonus": 20,
        "7-Day Streak Bonus": 50,
    }
    for action, xp in xp_data.items():
        col1, col2 = st.columns([4, 1])
        col1.write(action)
        col2.write(f"**+{xp} XP**")

    st.divider()

    # ── Referral ──
    st.markdown("### 👥 Refer a Friend — Earn 100 XP")
    st.write("Share EduPath AI with a friend. When they use the platform, you both earn bonus XP.")

    name = p.get("name", "")
    if name.strip():
        code = generate_referral_code(name)
        link = get_referral_link(code)
        message = get_referral_message(name, code, link)

        col1, col2 = st.columns(2)
        col1.text_input("Your Referral Code", value=code, disabled=True)
        col2.text_input("Your Referral Link", value=link, disabled=True)

        st.text_area("Share this message", value=message, height=150)

        if st.button("📋 Copy Message (then paste anywhere)", type="primary"):
            st.success("Message ready — copy it from the box above and share on WhatsApp, Instagram, or email!")

        st.divider()
        st.markdown("**Claim a referral bonus** — enter a friend's referral code:")
        ref_input = st.text_input("Enter referral code", placeholder="e.g. EDU-RAHU-A1B2C")
        if st.button("Claim +100 XP Bonus"):
            if st.session_state.referral_bonus_claimed:
                st.warning("You've already claimed a referral bonus.")
            elif ref_input.strip().upper() == code:
                st.error("You can't use your own referral code.")
            elif ref_input.strip().startswith("EDU-"):
                st.session_state.xp += 100
                st.session_state.referral_bonus_claimed = True
                st.balloons()
                st.success("🎉 +100 XP added! Welcome to EduPath AI.")
                st.rerun()
            else:
                st.error("Invalid referral code. Check with your friend.")
    else:
        st.warning("Set your name in My Profile first to generate your referral code.")

# ── SOP Generator ─────────────────────────────────────────
elif menu == "🎓 SOP Generator":
    st.subheader("🎓 AI Statement of Purpose Generator")
    show_notifications()
    p = st.session_state.profile
    st.write("Generate a personalized SOP draft based on your profile. Edit and refine it as needed.")

    col1, col2 = st.columns(2)
    with col1:
        st.text_input("Name", value=p.get("name",""), disabled=True)
        st.text_input("Degree", value=p.get("degree",""), disabled=True)
        st.text_input("GPA", value=p.get("gpa",""), disabled=True)
        st.text_input("Work Experience", value=p.get("work_exp",""), disabled=True)
    with col2:
        st.text_input("Target Program", value=p.get("target_program",""), disabled=True)
        st.text_input("Target Country", value=p.get("target_country",""), disabled=True)
        st.text_input("GRE Score", value=p.get("gre_score",""), disabled=True)
        st.text_input("IELTS/TOEFL", value=p.get("english_score",""), disabled=True)

    extra = st.text_area("Additional context for your SOP (optional)",
                         placeholder="e.g. I interned at TCS for 6 months, built an ML project on crop prediction, passionate about NLP research...")

    if not p.get("target_program"):
        st.warning("Please complete your profile first (at minimum: Target Program and Country).")
    else:
        if st.button("✍️ Generate My SOP", type="primary"):
            with st.spinner("Writing your personalized SOP..."):
                sop = generate_sop(p, extra)
            award("SOP Generator")
            st.divider()
            st.markdown("### 📄 Your SOP Draft")
            st.markdown(sop)
            st.divider()
            st.info("💡 This is an AI-generated draft. Review, personalize, and refine it before submitting to universities.")

# ── Scholarship Finder ────────────────────────────────────
elif menu == "🏆 Scholarship Finder":
    st.subheader("🏆 AI Scholarship Finder")
    show_notifications()
    p = st.session_state.profile
    st.write("Discover scholarships that match your profile and reduce your loan requirement.")

    col1, col2 = st.columns(2)
    with col1:
        st.text_input("Degree", value=p.get("degree",""), disabled=True)
        st.text_input("GPA", value=p.get("gpa",""), disabled=True)
        st.text_input("Target Program", value=p.get("target_program",""), disabled=True)
    with col2:
        st.text_input("Target Country", value=p.get("target_country",""), disabled=True)
        st.text_input("Work Experience", value=p.get("work_exp",""), disabled=True)
        st.text_input("Budget", value=p.get("budget",""), disabled=True)

    if not p.get("target_program"):
        st.warning("Please complete your profile first to get relevant scholarship matches.")
    else:
        if st.button("🔍 Find My Scholarships", type="primary"):
            with st.spinner("Searching for scholarships that match your profile..."):
                result = find_scholarships(p)
            award("Scholarship Finder")
            st.divider()
            st.markdown(result)

# ── Email Nudge Simulator ─────────────────────────────────
elif menu == "📧 Email Nudge Simulator":
    st.subheader("📧 AI Email Nudge Simulator")
    st.write("See exactly what emails EduPath AI would send you throughout your journey — powered by AI-driven lifecycle marketing.")

    p = st.session_state.profile
    emails = get_email_sequence(p, st.session_state.xp, st.session_state.tools_used)

    st.divider()
    st.markdown(f"**{len(emails)} emails in your personalized sequence** based on your current journey stage.")

    STAGE_COLORS = {
        "Onboarding": "🟢",
        "Activation": "🔵",
        "Engagement": "🟡",
        "Nurture": "🟠",
        "Conversion": "🔴",
    }

    for i, email in enumerate(emails):
        stage_icon = STAGE_COLORS.get(email["stage"], "⚪")
        sent_label = "✅ Sent" if email["sent"] else "⏳ Scheduled"
        with st.expander(f"{stage_icon} Day {email['day']} — {email['subject']}  |  {sent_label}  |  {email['date']}"):
            col1, col2 = st.columns([1, 3])
            with col1:
                st.metric("Stage", email["stage"])
                st.metric("Day", f"Day {email['day']}")
                st.metric("Status", "Sent" if email["sent"] else "Scheduled")
            with col2:
                st.markdown(f"**Subject:** {email['subject']}")
                st.markdown(f"**Preview:** *{email['preview']}*")
                st.divider()
                st.code(email["body"], language=None)

    st.divider()
    st.markdown("### 📊 Sequence Overview")
    stages = [e["stage"] for e in emails]
    for stage, icon in STAGE_COLORS.items():
        count = stages.count(stage)
        if count:
            st.write(f"{icon} **{stage}** — {count} email{'s' if count > 1 else ''}")

    st.info("💡 This simulates EduPath AI's zero-human-intervention growth loop — students are automatically nurtured from signup to loan application using AI-triggered emails.")
