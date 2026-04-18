from dotenv import load_dotenv
load_dotenv()
import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def find_scholarships(profile: dict):
    prompt = f"""
You are a scholarship advisor specializing in helping Indian students find funding for graduate studies abroad.

Student Profile:
- Degree: {profile.get('degree', '')}
- GPA: {profile.get('gpa', '')}
- Target Program: {profile.get('target_program', '')}
- Target Country: {profile.get('target_country', '')}
- Work Experience: {profile.get('work_exp', '0 years')}
- Budget: {profile.get('budget', 'Not specified')}

Find the best scholarships for this student. Respond in this exact markdown format:

---

## 🎓 Scholarship Recommendations

For each scholarship, use this format:

### 1. [Scholarship Name]
- 🏛️ Offered by: [University / Government / Organization]
- 💰 Value: [Amount or % of tuition]
- 📋 Eligibility: [Key requirements]
- 🎯 Match Score: [High / Medium / Low] — [one sentence why it fits this student]
- 🔗 Apply at: [Official website URL]

---

List at least 6 scholarships covering:
- University-specific merit scholarships
- Government scholarships (e.g. Fulbright, Chevening, DAAD, Commonwealth)
- Private/NGO scholarships for Indian students
- Program-specific funding

End with:

## 💡 Application Tips
3 specific tips for this student to maximize their scholarship chances.
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a scholarship advisor for Indian students pursuing graduate studies abroad. Always respond in clean markdown with accurate, specific information."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.6,
        max_tokens=1500,
    )
    return response.choices[0].message.content
