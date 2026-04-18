from datetime import date, timedelta

def update_streak(streak_data: dict) -> dict:
    """
    streak_data: { "last_visit": "YYYY-MM-DD", "count": int, "longest": int }
    Returns updated streak_data.
    """
    today = date.today()
    last = streak_data.get("last_visit")
    count = streak_data.get("count", 0)
    longest = streak_data.get("longest", 0)

    if last is None:
        count = 1
    else:
        last_date = date.fromisoformat(last)
        if last_date == today:
            pass  # already visited today, no change
        elif last_date == today - timedelta(days=1):
            count += 1  # consecutive day
        else:
            count = 1  # streak broken

    longest = max(longest, count)
    return {"last_visit": today.isoformat(), "count": count, "longest": longest}


def streak_bonus_xp(count: int) -> int:
    """Award bonus XP for streak milestones."""
    if count == 7:
        return 50
    elif count == 3:
        return 20
    elif count % 10 == 0:
        return 100
    return 0


def streak_emoji(count: int) -> str:
    if count >= 30: return "🔥🔥🔥"
    if count >= 14: return "🔥🔥"
    if count >= 7:  return "🔥"
    if count >= 3:  return "⚡"
    return "✨"
