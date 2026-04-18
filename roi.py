def calculate_roi(cost, salary, duration_years=1, current_salary=0):
    net_gain = (salary - current_salary) * duration_years - cost
    roi = (net_gain / cost) * 100 if cost > 0 else 0
    payback_months = (cost / (salary / 12)) if salary > 0 else None
    return {
        "roi": round(roi, 2),
        "net_gain": round(net_gain, 2),
        "payback_months": round(payback_months, 1) if payback_months else None,
        "monthly_gain": round((salary - current_salary) / 12, 2),
        "salary_growth": round(((salary - current_salary) / current_salary) * 100, 1) if current_salary > 0 else None,
    }
