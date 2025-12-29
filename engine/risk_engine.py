
def risk_score(level):
    mapping = {
        "LOW": 30,
        "MEDIUM": 60,
        "HIGH": 90
    }
    return mapping.get(level, 0)
