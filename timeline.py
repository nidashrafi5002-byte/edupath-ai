from dotenv import load_dotenv
load_dotenv()
import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_timeline(goal, start_month, duration_months, extras):
    prompt = f"""
You are an expert academic and visa planning advisor for students.

A student has the following goal:
Goal: {goal}
Starting Month: {start_month}
Duration: {duration_months} months
Additional context: {extras if extras else "None"}

Create a detailed month-by-month action plan in this exact markdown format:

---

## 📅 Your Personalized Timeline

For each month, use this structure:

### Month 1 – [Month Name]: [Theme/Focus]
- ✅ Task 1
- ✅ Task 2
- ✅ Task 3

Continue for all {duration_months} months. Cover relevant steps from these categories based on the goal:
- 📝 Exams (GRE, IELTS, TOEFL, GMAT, etc.)
- 📄 SOP / LOR / Resume preparation
- 🏫 University research & shortlisting
- 📬 Applications & deadlines
- 💰 Scholarships & financial planning
- 🛂 Visa application steps
- ✈️ Pre-departure checklist

---

## ⚠️ Key Deadlines to Watch
List 3-5 critical deadlines or milestones the student must not miss.

---

## 💡 Pro Tips
Give 3 practical tips specific to this student's goal and timeline.

---

Be specific, realistic, and actionable. Tailor tasks to the goal provided.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an expert student advisor specializing in academic timelines, exam prep, visa planning, and study abroad guidance. Always respond in clean markdown."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_tokens=2048,
    )

    return response.choices[0].message.content
