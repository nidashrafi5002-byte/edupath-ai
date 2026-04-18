import hashlib

def generate_referral_code(name: str) -> str:
    """Generate a unique referral code from the user's name."""
    raw = (name or "student").strip().lower().replace(" ", "")
    hash_part = hashlib.md5(raw.encode()).hexdigest()[:5].upper()
    return f"EDU-{raw[:4].upper()}-{hash_part}"


def get_referral_link(code: str) -> str:
    return f"https://edupathAI.streamlit.app/?ref={code}"


def get_referral_message(name: str, code: str, link: str) -> str:
    return f"""Hey! I've been using EduPath AI to plan my study abroad journey — it helped me with career advice, admission predictions, and even my education loan.

Check it out: {link}

Use my referral code **{code}** when you sign up and we both earn bonus XP! 🎓"""
