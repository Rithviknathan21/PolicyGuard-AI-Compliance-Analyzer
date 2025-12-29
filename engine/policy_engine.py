
def detect_violations(actions, policies):
    violations = []

    for act in actions:
        for pol in policies:
            condition = pol["condition"]
            matched = True

            for key, value in condition.items():
                if key.endswith("_gt"):
                    real_key = key.replace("_gt", "")
                    if act.get(real_key, 0) <= value:
                        matched = False
                else:
                    if act.get(key) != value:
                        matched = False

            if matched:
                violations.append({
                    "user_id": act["user_id"],
                    "policy_id": pol["policy_id"],
                    "policy_name": pol["name"],
                    "risk": pol["risk"],
                    "description": pol["description"],
                    "timestamp": act["timestamp"]
                })

    return violations
