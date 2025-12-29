
import json
import sys
import streamlit as st

BASE_DIR = "."

sys.path.append(f"{BASE_DIR}/engine")

from policy_engine import detect_violations
from risk_engine import risk_score
from explanation_engine import explain_violation

st.set_page_config(page_title="PolicyGuard", layout="wide")

st.title("🛡️ PolicyGuard – AI Policy Violation & Risk Analyzer")
st.caption("Enterprise Governance & Compliance Intelligence System")

# Load data
with open("policies/policy_rules.json") as f:
    policies = json.load(f)["policies"]

with open("data/simulated_actions.json") as f:
    actions = json.load(f)["actions"]

# Run analysis
violations = detect_violations(actions, policies)

final_report = []
for v in violations:
    v["risk_score"] = risk_score(v["risk"])
    v["explanation"] = explain_violation(v)
    final_report.append(v)

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Policies", len(policies))
col2.metric("Total Actions", len(actions))
col3.metric("Violations Detected", len(final_report))

st.divider()

st.subheader("🚨 Detected Policy Violations")

if final_report:
    for v in final_report:
        with st.expander(f"{v['policy_id']} | {v['policy_name']} | Risk: {v['risk']}"):
            st.write("👤 **User:**", v["user_id"])
            st.write("🕒 **Timestamp:**", v["timestamp"])
            st.write("⚠️ **Risk Score:**", v["risk_score"])
            st.write("🧠 **Explanation:**")
            st.info(v["explanation"])
else:
    st.success("No policy violations detected.")
