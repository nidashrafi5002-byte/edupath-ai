from datetime import date, timedelta

def get_email_sequence(profile: dict, xp: int, tools_used: set) -> list:
    """
    Returns a simulated email sequence the platform would send
    based on the student's journey stage.
    Each email: {day, subject, preview, body, stage, sent}
    """
    name = profile.get("name") or "Student"
    program = profile.get("target_program") or "your target program"
    country = profile.get("target_country") or "your target country"
    today = date.today()

    emails = []

    # Day 0 — Welcome
    emails.append({
        "day": 0,
        "date": today.strftime("%d %b %Y"),
        "subject": f"Welcome to EduPath AI, {name}! 🎓",
        "preview": "Your AI-powered study abroad journey starts now.",
        "body": f"""Hi {name},

Welcome to EduPath AI — your personal AI companion for the study abroad journey.

Here's what you can do right now:
✅ Complete your profile to unlock personalized advice
🎯 Check your admission chances with our AI Predictor
📈 Calculate the ROI of your target program
📅 Generate your month-by-month application timeline

You've already earned your first badge: 🌱 Explorer

Let's get started → [Open EduPath AI]

Team EduPath AI""",
        "stage": "Onboarding",
        "sent": True
    })

    # Day 2 — Profile nudge
    if not profile.get("completed"):
        emails.append({
            "day": 2,
            "date": (today + timedelta(days=2)).strftime("%d %b %Y"),
            "subject": f"{name}, your profile is incomplete ⚠️",
            "preview": "Complete your profile to get personalized university recommendations.",
            "body": f"""Hi {name},

We noticed your profile is still incomplete. Students with complete profiles get:

📊 More accurate admission predictions
🎓 Better-matched scholarship recommendations
📅 Personalized timelines with real deadlines

It takes less than 2 minutes → [Complete Profile]

Team EduPath AI""",
            "stage": "Activation",
            "sent": True
        })

    # Day 5 — ROI nudge
    if "ROI Calculator" not in tools_used:
        emails.append({
            "day": 5,
            "date": (today + timedelta(days=5)).strftime("%d %b %Y"),
            "subject": f"Is {program} worth the investment?",
            "preview": "Calculate your expected ROI before committing to a program.",
            "body": f"""Hi {name},

Studying {program} in {country} is a big financial decision.

Our ROI Calculator shows you:
💰 Expected salary after graduation
📈 Net gain over 3–5 years
⏱️ How long to pay back your investment

Students who calculate ROI before applying make 40% better financial decisions.

Calculate your ROI now → [Open ROI Calculator]

Team EduPath AI""",
            "stage": "Engagement",
            "sent": False
        })

    # Day 10 — Admission predictor
    if "Admission Predictor" not in tools_used:
        emails.append({
            "day": 10,
            "date": (today + timedelta(days=10)).strftime("%d %b %Y"),
            "subject": f"What are your chances at top {country} universities?",
            "preview": "Find out before you apply — our AI gives you a realistic assessment.",
            "body": f"""Hi {name},

Before spending hours on applications, know your chances.

Our Admission Predictor analyzes:
🎓 Your GPA and test scores
🏫 Target program and country
💼 Work experience and projects

And gives you:
✅ Admission probability %
🏛️ Safe, Target, and Reach universities
🔧 Specific tips to improve your profile

Check your chances → [Open Admission Predictor]

Team EduPath AI""",
            "stage": "Engagement",
            "sent": False
        })

    # Day 15 — Scholarship finder
    emails.append({
        "day": 15,
        "date": (today + timedelta(days=15)).strftime("%d %b %Y"),
        "subject": f"You may qualify for scholarships worth ₹10L+",
        "preview": "Our AI found scholarships that match your profile.",
        "body": f"""Hi {name},

Good news — based on your profile, you may qualify for several scholarships.

Our Scholarship Finder found matches including:
🏆 Merit-based university scholarships
🌍 Government scholarships (Fulbright, Chevening, DAAD)
💡 Program-specific funding for {program}

Reducing your loan requirement by even ₹5–10L makes a huge difference.

Find your scholarships → [Open Scholarship Finder]

Team EduPath AI""",
        "stage": "Nurture",
        "sent": False
    })

    # Day 21 — Loan awareness
    if "Loan Eligibility" not in tools_used:
        emails.append({
            "day": 21,
            "date": (today + timedelta(days=21)).strftime("%d %b %Y"),
            "subject": "Planning your education loan? Start early.",
            "preview": "Check your eligibility and lock in the best interest rate.",
            "body": f"""Hi {name},

Education loans for studying in {country} can take 4–6 weeks to process.

Start early and:
✅ Check how much you qualify for
💳 Get a personalized loan offer
📋 Know exactly which documents you need

Students who apply early get better rates and fewer rejections.

Check loan eligibility → [Open Loan Eligibility]

Team EduPath AI""",
            "stage": "Conversion",
            "sent": False
        })

    # Day 30 — Loan application CTA
    if xp >= 100:
        emails.append({
            "day": 30,
            "date": (today + timedelta(days=30)).strftime("%d %b %Y"),
            "subject": f"Ready to apply for your education loan, {name}?",
            "preview": "You've done the research. Now take the final step.",
            "body": f"""Hi {name},

You've explored EduPath AI thoroughly — you're clearly serious about your goals.

Now it's time to take the final step: apply for your education loan.

Your profile shows you're a strong candidate. Our AI will:
📋 Pre-fill your application from your profile
💰 Generate a personalized loan offer
📄 Give you a complete document checklist

Apply in under 10 minutes → [Start Loan Application]

Team EduPath AI""",
            "stage": "Conversion",
            "sent": False
        })

    return emails
