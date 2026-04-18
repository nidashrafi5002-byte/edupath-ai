def get_nudges(profile, xp, tools_used):
    nudges = []

    if not profile.get("completed"):
        nudges.append(("⚠️", "Complete your profile to unlock personalized recommendations."))

    if "ROI Calculator" not in tools_used:
        nudges.append(("📈", "Have you checked if your target course is worth the investment? Try the ROI Calculator."))

    if "Admission Predictor" not in tools_used:
        nudges.append(("🎯", "Know your admission chances before applying — try the Admission Predictor."))

    if "AI Timeline Generator" not in tools_used:
        nudges.append(("📅", "Build your month-by-month study abroad plan with the Timeline Generator."))

    if "Loan Eligibility" not in tools_used:
        nudges.append(("💳", "Check how much education loan you qualify for — it takes 2 minutes."))

    if "Loan Application" not in tools_used and xp >= 100:
        nudges.append(("🏦", "You've explored enough — ready to apply for an education loan? Start your application."))

    if xp >= 200:
        nudges.append(("🏆", "You're a power user! Share EduPath AI with a friend and earn bonus XP."))

    return nudges[:3]  # show max 3 nudges at a time


def get_tips(target_country):
    tips = {
        "USA": [
            "🗓️ GRE scores are valid for 5 years — plan your test early.",
            "📄 Most US universities require 3 LORs. Start asking professors now.",
            "💰 Apply for FAFSA or university scholarships alongside your loan.",
        ],
        "UK": [
            "📅 UCAS deadlines are strict — mark them on your calendar.",
            "🏦 UK student visa requires proof of funds — plan your finances early.",
            "📝 Personal Statement is critical for UK admissions — draft it 3 months early.",
        ],
        "Canada": [
            "🍁 Apply for a study permit as soon as you get your offer letter.",
            "💼 Canada allows 20hrs/week work during studies — factor this into your budget.",
            "🎓 Many Canadian universities offer entrance scholarships — check eligibility.",
        ],
        "Germany": [
            "🆓 Most public German universities have no tuition fees.",
            "🗣️ Learn basic German — it helps with daily life even in English programs.",
            "📋 APS certificate is mandatory for Indian students applying to Germany.",
        ],
        "Australia": [
            "🌏 Apply for an Australian Student Visa (subclass 500) early.",
            "💵 Show proof of AUD 21,041/year for living expenses in your visa application.",
            "🏥 OSHC (health cover) is mandatory — factor it into your budget.",
        ],
    }
    return tips.get(target_country, [
        "📚 Research your target universities thoroughly before applying.",
        "💰 Start financial planning at least 12 months before your intake.",
        "📝 Prepare your SOP early — it takes multiple revisions.",
    ])
