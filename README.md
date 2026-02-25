# Thoughtful AI Support Agent 🤖

A simple conversational AI agent that answers questions about Thoughtful AI using predefined responses and fuzzy matching.

## 🚀 Features
- Conversational UI using Streamlit
- Fuzzy matching to find the most relevant answer
- Graceful fallback for unknown queries
- Clean and simple user experience

## 🛠 Tech Stack
- Python
- Streamlit

## 📦 Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/thoughtful-ai-support-agent.git  
cd thoughtful-ai-support-agent  

Install dependencies:

pip install -r requirements.txt  

Run the app:

streamlit run app.py  

## 💬 Example Questions
- What does the eligibility verification agent (EVA) do?
- What does the claims processing agent (CAM) do?
- Tell me about Thoughtful AI's agents

## 🧠 Approach
The agent uses fuzzy string matching (`difflib`) to map user queries to the closest predefined question and returns the corresponding answer. If no close match is found, it provides a fallback response.

## ⚠️ Limitations
- Uses hardcoded dataset (no real-time learning)
- Limited to predefined knowledge base

## 📌 Future Improvements
- Add LLM fallback for unknown queries
- Improve semantic search using embeddings
- Add chat history UI