import streamlit as st
from graph.build_graph import build_medical_graph

st.set_page_config(page_title="Agentic MedBot", layout="wide")
st.title("🩺 Agentic Medical Chatbot")

if "history" not in st.session_state:
    st.session_state["history"] = []

user_input = st.text_input("Enter your symptoms or medical query:")

if user_input:
    graph = build_medical_graph()
    result = graph.invoke({
        "query": user_input,
        "history": st.session_state["history"]
    })
    
    response = result["response"]
    st.write("### 💬 Response:")
    st.success(response)

    # Save to session state history
    st.session_state["history"].append({
        "query": user_input,
        "response": response
    })

# Show full history
if st.session_state["history"]:
    with st.expander("📜 Chat History"):
        for turn in st.session_state["history"]:
            st.markdown(f"**User:** {turn['query']}")
            st.markdown(f"**Bot:** {turn['response']}")
