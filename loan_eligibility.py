def estimate_loan_eligibility(annual_income, co_applicant_income, existing_emi, credit_score, loan_amount, course_duration_years):
    """
    Rule-based loan eligibility estimator for education loans (NBFC/bank style).
    """
    total_income = annual_income + co_applicant_income
    monthly_income = total_income / 12
    foir_limit = 0.50  # Fixed Obligation to Income Ratio max 50%
    max_emi_allowed = (monthly_income * foir_limit) - existing_emi

    # Interest rate based on credit score
    if credit_score >= 750:
        interest_rate = 9.5
        credit_label = "Excellent"
    elif credit_score >= 700:
        interest_rate = 11.0
        credit_label = "Good"
    elif credit_score >= 650:
        interest_rate = 13.0
        credit_label = "Fair"
    else:
        interest_rate = 15.5
        credit_label = "Poor"

    # Max loan based on repayment capacity (repayment = course + 1 year grace)
    repayment_months = (course_duration_years + 1) * 12
    r = interest_rate / (12 * 100)
    if r > 0 and max_emi_allowed > 0:
        max_loan_by_income = max_emi_allowed * ((1 + r)**repayment_months - 1) / (r * (1 + r)**repayment_months)
    else:
        max_loan_by_income = 0

    eligible = max_loan_by_income >= loan_amount
    coverage = min((max_loan_by_income / loan_amount) * 100, 100) if loan_amount > 0 else 0

    return {
        "eligible": eligible,
        "max_loan": round(max_loan_by_income, 2),
        "interest_rate": interest_rate,
        "credit_label": credit_label,
        "max_emi_allowed": round(max_emi_allowed, 2),
        "coverage_pct": round(coverage, 1),
        "repayment_months": repayment_months,
    }
