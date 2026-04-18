from dotenv import load_dotenv
load_dotenv()
import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_sop(profile: dict, extra: str = ""):
    prompt = f"""
You are an expert academic writer specializing in Statements of Purpose (SOP) for graduate school admissions.

Write a compelling, personalized SOP for the following student:

- Name: {profile.get('name', 'the applicant')}
- Degree: {profile.get('degree', '')}
- GPA: {profile.get('gpa', '')}
- Target Program: {profile.get('target_program', '')}
- Target Country: {profile.get('target_country', '')}
- Work Experience: {profile.get('work_exp', '0 years')}
- GRE Score: {profile.get('gre_score', 'Not taken')}
- IELTS/TOEFL: {profile.get('english_score', 'Not taken')}
- Additional context: {extra if extra else 'None'}

Write a full SOP (500–700 words) with these sections:

1. Opening Hook — a compelling first paragraph that grabs attention
2. Academic Background — GPA, relevant coursework, academic achievements
3. Professional Experience — internships, projects, work experience
4. Why This Program — specific reasons for choosing this program and country
5. Career Goals — short-term and long-term goals after graduation
6. Closing — confident, memorable conclusion

Guidelines:
- Write in first person
- Be specific, not generic
- Sound human and authentic, not robotic
- Avoid clichés like "since childhood I was fascinated..."
- Tailor every paragraph to the student's actual profile
"""
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are an expert SOP writer for graduate school admissions. Write compelling, authentic, personalized statements."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8,
        max_tokens=1500,
    )
    return response.choices[0].message.content
