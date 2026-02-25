import json
import streamlit as st
from difflib import get_close_matches

# Load data
with open("data.json") as f:
    data = json.load(f)

questions = [q["question"] for q in data["questions"]]

def find_best_match(user_input):
    matches = get_close_matches(user_input, questions, n=1, cutoff=0.5)
    return matches[0] if matches else None

def get_answer(question):
    for q in data["questions"]:
        if q["question"] == question:
            return q["answer"]
    return None

# UI
st.title("🤖 Thoughtful AI Support Agent")

user_input = st.text_input("Ask a question:")

if user_input:
    match = find_best_match(user_input)
    
    if match:
        answer = get_answer(match)
        st.success(answer)
    else:
        st.warning("I'm not sure about that. Try asking something else!")