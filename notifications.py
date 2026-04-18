from datetime import date

# Key deadlines by country and intake
DEADLINES = {
    "USA": {
        "Fall 2025": [
            ("GRE Registration Deadline", date(2025, 4, 30)),
            ("Early Application Deadline", date(2025, 9, 15)),
            ("Regular Application Deadline", date(2026, 1, 15)),
        ],
        "Fall 2026": [
            ("GRE Registration Deadline", date(2025, 10, 31)),
            ("Early Application Deadline", date(2025, 10, 15)),
            ("Regular Application Deadline", date(2026, 1, 15)),
        ],
        "Spring 2026": [
            ("Application Deadline", date(2025, 9, 1)),
            ("Document Submission", date(2025, 9, 15)),
        ],
    },
    "UK": {
        "Fall 2025": [
            ("UCAS Application Deadline", date(2025, 1, 29)),
            ("Visa Application Opens", date(2025, 3, 1)),
        ],
        "Fall 2026": [
            ("UCAS Application Deadline", date(2026, 1, 28)),
            ("IELTS Booking Deadline", date(2025, 10, 1)),
        ],
    },
    "Canada": {
        "Fall 2026": [
            ("Application Deadline", date(2026, 2, 1)),
            ("Study Permit Application", date(2026, 3, 15)),
        ],
        "Spring 2026": [
            ("Application Deadline", date(2025, 10, 1)),
        ],
    },
    "Germany": {
        "Fall 2026": [
            ("APS Certificate Deadline", date(2025, 12, 1)),
            ("Uni-Assist Application", date(2026, 1, 15)),
        ],
    },
    "Australia": {
        "Fall 2026": [
            ("Application Deadline", date(2026, 1, 31)),
            ("Student Visa Application", date(2026, 3, 1)),
        ],
    },
}


def get_smart_notifications(profile: dict, xp: int, tools_used: set, loan_result=None) -> list:
    """
    Returns list of (type, message) tuples.
    type: "warning" | "info" | "success" | "error"
    """
    notifications = []
    today = date.today()

    country = profile.get("target_country", "")
    intake = profile.get("timeline", "")
    name = profile.get("name", "")

    # ── Deadline notifications ──
    if country and intake and country in DEADLINES and intake in DEADLINES.get(country, {}):
        for label, deadline in DEADLINES[country][intake]:
            days_left = (deadline - today).days
            if 0 < days_left <= 30:
                notifications.append(("error" if days_left <= 7 else "warning",
                                       f"⏰ {country} — {label} in {days_left} days! ({deadline.strftime('%d %b %Y')})"))
            elif days_left <= 0 and days_left >= -3:
                notifications.append(("error", f"🚨 {label} deadline was {abs(days_left)} day(s) ago. Check if late applications are accepted."))

    # ── Loan upgrade notification ──
    if loan_result:
        if loan_result.get("credit_label") in ["Good", "Excellent"] and loan_result.get("coverage_pct", 0) >= 90:
            notifications.append(("success", "💳 You qualify for a competitive loan rate. Head to Loan Application to lock in your offer."))
        if loan_result.get("interest_rate", 15) <= 10:
            notifications.append(("success", f"🎉 You qualify for a low {loan_result['interest_rate']}% interest rate — better than most students!"))

    # ── Profile nudges ──
    if not profile.get("gre_score") and country == "USA":
        notifications.append(("info", "📝 GRE score not added. US universities require it — add it to your profile for accurate predictions."))

    if not profile.get("english_score") and country in ["UK", "Canada", "Australia"]:
        notifications.append(("info", f"🗣️ IELTS/TOEFL score missing. {country} universities require English proficiency proof."))

    # ── XP milestone ──
    if xp >= 100 and "Loan Application" not in tools_used:
        notifications.append(("info", "🏦 You've explored the platform well. Ready to take the next step? Apply for your education loan."))

    if xp >= 200:
        notifications.append(("success", "🏆 You're a power user! Share EduPath AI with friends and earn +100 XP."))

    # ── Streak reminder ──
    return notifications[:3]  # max 3 at a time
