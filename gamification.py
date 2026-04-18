XP_REWARDS = {
    "profile_complete": 50,
    "Career Navigator": 20,
    "Admission Predictor": 30,
    "ROI Calculator": 20,
    "AI Timeline Generator": 30,
    "Loan EMI Calculator": 15,
    "Loan Eligibility": 25,
    "Loan Application": 50,
    "SOP Generator": 40,
    "Scholarship Finder": 30,
}

BADGES = [
    {"name": "🌱 Explorer",     "min_xp": 0,   "desc": "Just getting started"},
    {"name": "📚 Learner",      "min_xp": 50,  "desc": "Completed your profile"},
    {"name": "🔍 Researcher",   "min_xp": 100, "desc": "Used 3+ tools"},
    {"name": "🎯 Strategist",   "min_xp": 175, "desc": "Predicted admission chances"},
    {"name": "💡 Planner",      "min_xp": 250, "desc": "Generated your timeline"},
    {"name": "🏆 EduPath Pro",  "min_xp": 400, "desc": "Completed the full journey"},
]

def get_badge(xp):
    badge = BADGES[0]
    for b in BADGES:
        if xp >= b["min_xp"]:
            badge = b
    return badge

def get_next_badge(xp):
    for b in BADGES:
        if xp < b["min_xp"]:
            return b
    return None

def award_xp(tool_name):
    return XP_REWARDS.get(tool_name, 10)
