def calculate_loan(P, R, N):
    r = R / (12 * 100)
    emi = (P * r * (1 + r)**N) / ((1 + r)**N - 1)
    total_payment = emi * N
    total_interest = total_payment - P
    interest_ratio = (total_interest / total_payment) * 100

    return {
        "emi": round(emi, 2),
        "total_payment": round(total_payment, 2),
        "total_interest": round(total_interest, 2),
        "principal": round(P, 2),
        "interest_ratio": round(interest_ratio, 1),
        "principal_ratio": round(100 - interest_ratio, 1),
    }
