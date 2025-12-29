
def explain_violation(v):
    return (
        f"User {v['user_id']} violated policy {v['policy_id']} "
        f"({v['policy_name']}) because: {v['description']}."
    )
