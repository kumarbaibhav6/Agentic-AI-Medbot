from agents.vector_retrieval import retrieve_similar_cases
from agents.rag_generator import generate_response
from .wiki_fetcher import fetch_wikipedia_summary

def input_parser(state: dict) -> dict:
    return {"query": state["query"], "history": state.get("history", [])}

def vector_retrieval(state: dict) -> dict:
    retrieved = retrieve_similar_cases(state["query"])
    return {**state, "retrieved_cases": retrieved}

def rag_response(state):
    query = state["query"]
    history = state.get("history", [])
    
    retrieved_cases, _ = retrieve_similar_cases(query)  # ✅ unpack tuple

    response = generate_response(query, retrieved_cases, history=history)

    return {
        "response": response,
        "history": history + [{"query": query, "response": response}],
    }


def wiki_fallback(state: dict) -> dict:
    fallback = fetch_wikipedia_summary(state["query"])
    return {**state, "response": fallback or "Sorry, I couldn't find information on that. Please consult a doctor."}
