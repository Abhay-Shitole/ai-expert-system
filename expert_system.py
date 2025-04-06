import streamlit as st
import time

st.set_page_config(page_title="AI Expert System", layout="centered")

st.markdown("<h1 style='text-align: center; color: #4A90E2;'>🤖 AI Expert System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter a symptom to see possible causes and suggested actions.</p>", unsafe_allow_html=True)

# Knowledge base
expert_knowledge = {
    "fever": {
        "causes": ["Viral Infection", "Bacterial Infection", "Flu"],
        "actions": ["Take rest", "Stay hydrated", "Consult a doctor if persistent"]
    },
    "headache": {
        "causes": ["Stress", "Migraine", "Lack of sleep"],
        "actions": ["Take a painkiller", "Rest in a dark room", "Reduce screen time"]
    },
    "cough": {
        "causes": ["Cold", "Allergy", "Respiratory Infection"],
        "actions": ["Drink warm fluids", "Use cough syrup", "Consult a doctor"]
    },
    "stomach pain": {
        "causes": ["Indigestion", "Food Poisoning", "Gastritis"],
        "actions": ["Avoid spicy food", "Drink ORS", "Visit a physician"]
    },
    "sore throat": {
        "causes": ["Viral infection", "Cold", "Tonsillitis"],
        "actions": ["Gargle with salt water", "Drink warm tea", "Consult a doctor"]
    },
    "fatigue": {
        "causes": ["Anemia", "Lack of sleep", "Poor diet"],
        "actions": ["Get enough sleep", "Eat a balanced diet", "Exercise regularly"]
    },
    "nausea": {
        "causes": ["Food poisoning", "Motion sickness", "Pregnancy"],
        "actions": ["Avoid strong smells", "Stay hydrated", "Take prescribed medication"]
    }
}

# Get known symptoms
all_symptoms = list(expert_knowledge.keys())

# Text input
user_input = st.text_input("Type your symptom (e.g., fever, headache)", "").strip().lower()

if user_input:
    # Exact match found
    if user_input in expert_knowledge:
        with st.spinner("Analyzing symptom..."):
            time.sleep(3)  # Simulate processing time

        data = expert_knowledge[user_input]
        st.success(f"Results for symptom: **{user_input.capitalize()}**")

        with st.container():
            st.markdown("### 🔍 Possible Causes")
            for cause in data["causes"]:
                st.markdown(f"- {cause}")

            st.markdown("### 💡 Suggested Actions")
            for action in data["actions"]:
                st.markdown(f"- {action}")
    else:
        # Find close matches
        matches = [s for s in all_symptoms if user_input in s]
        if matches:
            st.warning("Symptom not found exactly. Did you mean:")
            for match in matches:
                st.markdown(f"- **{match.capitalize()}**")
        else:
            st.error("❌ Sorry, we couldn't find any matching symptom. Please check your input or try a different one.")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 12px;'>Developed for AI Expert System Project</p>", unsafe_allow_html=True)
