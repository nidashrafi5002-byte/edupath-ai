from dotenv import load_dotenv
load_dotenv()
import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_loan_offer(profile, loan_amount, credit_label, interest_rate):
    """Generate a personalized dynamic loan offer based on student profile."""
    prompt = f"""
You are a loan officer at an education-focused NBFC in India.

A student has the following profile:
- Name: {profile.get('name', 'Student')}
- Degree: {profile.get('degree', 'Not specified')}
- Target Program: {profile.get('target_program', 'Not specified')}
- Target Country: {profile.get('target_country', 'Not specified')}
- GPA: {profile.get('gpa', 'Not specified')}
- Work Experience: {profile.get('work_exp', '0 years')}
- Loan Amount Requested: ₹{loan_amount:,.0f}
- Credit Rating: {credit_label}
- Offered Interest Rate: {interest_rate}%

Generate a personalized loan offer letter in markdown with:

## 🏦 Your Personalized Loan Offer

### Offer Summary
- Loan Amount Approved: (based on profile, be specific)
- Interest Rate: {interest_rate}% per annum
- Repayment Period: (suggest based on course + 1 year grace)
- Processing Fee: (typical NBFC range 0.5–1%)
- Collateral Required: (Yes/No based on amount)

### Why You Qualify
2–3 sentences explaining why this student is a good candidate.

### Repayment Plan Options
Give 2 options (e.g. 5-year and 7-year) with estimated EMI for each.

### 📋 Next Steps
3 clear steps to proceed with the application.

### ⚠️ Important Conditions
2–3 standard loan conditions.

Keep it professional, warm, and encouraging.
    """
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a professional loan officer at an education NBFC. Respond in clean markdown."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=1000,
    )
    return response.choices[0].message.content
