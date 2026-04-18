from dotenv import load_dotenv
load_dotenv()
import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def predict_admission(profile: dict):
    prompt = f"""
You are an expert graduate admissions consultant with deep knowledge of US, UK, Canada, and European universities.

A student has shared their profile:
- Degree: {profile['degree']}
- GPA / Percentage: {profile['gpa']}
- Target Program: {profile['program']}
- Target Country: {profile['country']}
- GRE Score: {profile.get('gre', 'Not taken')}
- IELTS/TOEFL Score: {profile.get('english', 'Not taken')}
- Work Experience: {profile.get('work_exp', '0')} years
- Research / Publications: {profile.get('research', 'None')}
- Extracurriculars / Projects: {profile.get('extras', 'None')}

Respond in this exact markdown format:

---

## 🎯 Admission Probability Report

### Overall Admission Chance
Give a percentage score (e.g. 72%) and a one-line verdict (Strong / Moderate / Reach).

### 📊 Profile Strength Breakdown
Rate each factor out of 10 and give a one-line comment:
- Academic Score: X/10
- Test Scores: X/10
- Work Experience: X/10
- Research & Projects: X/10
- Overall Profile: X/10

### 🏫 University Recommendations
Suggest 3 tiers with 2 universities each:

**Safe (80%+ chance):**
- University 1 — reason
- University 2 — reason

**Target (50–80% chance):**
- University 1 — reason
- University 2 — reason

**Reach (Below 50%):**
- University 1 — reason
- University 2 — reason

### 🔧 How to Improve Your Profile
List 3 specific, actionable things this student can do to increase their chances.

### 💰 Estimated Cost & Loan Requirement
- Estimated total cost for the program (tuition + living): ₹X – ₹Y lakhs
- Suggested education loan range: ₹X – ₹Y lakhs

---

Be realistic, specific, and encouraging.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are an expert graduate admissions consultant. Always respond in clean markdown with realistic assessments."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.6,
        max_tokens=1500,
    )
    return response.choices[0].message.content
