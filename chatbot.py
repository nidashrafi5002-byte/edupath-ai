from dotenv import load_dotenv
load_dotenv()
import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_career_advice(user_input, history=None):
    messages = [
        {
            "role": "system",
            "content": "You are an expert career counselor specializing in guiding Indian students toward fulfilling, high-growth careers and study abroad opportunities. Always respond in clean, well-structured markdown. Be specific, practical, and personalized."
        }
    ]

    # Inject prior conversation for context
    if history:
        for msg in history[:-1]:  # exclude the latest user message, added below
            messages.append({"role": msg["role"], "content": msg["content"]})

    messages.append({"role": "user", "content": f"""
You are an expert career counselor specializing in guiding students toward fulfilling, high-growth careers.

A student has shared the following:
\"\"\"{user_input}\"\"\"

Carefully analyze their interests, strengths, and goals. Then respond using this exact markdown structure:

---

## 🎯 Career Recommendations

Recommend exactly 3 career paths that are a strong match. For each one:

**1. [Career Title]**
- What you'll do: One sentence describing the role.
- Why it fits you: One sentence connecting it to the student's input.
- Average salary: Provide a realistic range (e.g. ₹6–12 LPA or $60k–$90k).
- Growth outlook: One word rating — Excellent / Good / Moderate.

---

## 📚 Learning Roadmap

List 5 specific courses, certifications, or skills the student should pursue, in priority order:
1. [Skill/Course] — [Platform] — [Estimated duration]
2. ...

---

## 💡 Your Strengths & Fit

In 3–4 sentences, explain what stands out about this student's profile and why these careers are a natural fit. Be specific, not generic.

---

## 🚀 Action Plan for This Week

Give 3 concrete, immediately actionable steps the student can take right now. Be specific.

---

Tone: Encouraging, honest, and professional. Tailor everything to what the student actually said.
    """})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.7,
        max_tokens=1024,
    )

    return response.choices[0].message.content
