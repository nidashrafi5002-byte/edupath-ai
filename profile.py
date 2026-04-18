import json
import os

PROFILE_FILE = "user_profile.json"

def get_default_profile():
    return {
        "name": "",
        "degree": "",
        "gpa": "",
        "target_program": "",
        "target_country": "",
        "budget": "",
        "timeline": "",
        "english_score": "",
        "gre_score": "",
        "work_exp": "0 years",
        "completed": False,
    }

def profile_completion_pct(profile):
    fields = ["name", "degree", "gpa", "target_program", "target_country", "budget", "timeline"]
    filled = sum(1 for f in fields if profile.get(f, "").strip())
    return int((filled / len(fields)) * 100)

def save_profile(profile: dict):
    with open(PROFILE_FILE, "w") as f:
        json.dump(profile, f)

def load_profile() -> dict:
    if os.path.exists(PROFILE_FILE):
        with open(PROFILE_FILE, "r") as f:
            return json.load(f)
    return get_default_profile()
