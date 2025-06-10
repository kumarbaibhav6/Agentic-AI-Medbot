from langgraph.graph import StateGraph # type: ignore
from typing import TypedDict, List
from graph.nodes import input_parser, vector_retrieval, rag_response, wiki_fallback

class MedState(TypedDict):
    query: str
    history: List[dict]
    retrieved_cases: List[dict]
    response: str

def build_medical_graph():
    graph = StateGraph(MedState)

    # Add processing nodes
    graph.add_node("input_parser", input_parser)
    graph.add_node("vector_retrieval", vector_retrieval)
    graph.add_node("rag_response", rag_response)
    graph.add_node("wiki_fallback", wiki_fallback)
    graph.add_node("done", lambda x: x)  # Dummy terminal node

    # Set entry and end points
    graph.set_entry_point("input_parser")
    graph.set_finish_point("done")

    # Define edges
    graph.add_edge("input_parser", "vector_retrieval")
    graph.add_edge("vector_retrieval", "rag_response")

    # Branching logic: use fallback if no RAG response found
    def response_router(state):
        if state.get("response"):
            return "done"
        else:
            return "wiki_fallback"

    graph.add_conditional_edges("rag_response", response_router)
    graph.add_edge("wiki_fallback", "done")

    return graph.compile()

