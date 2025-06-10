import os
from openai import OpenAI
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()

# Initialize Groq-compatible OpenAI client
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = "llama3-8b-8192"  # Groq-supported model

def generate_response(user_query: str, retrieved_cases: List[Dict], history: List[Dict] = None) -> str:
    # Format past conversation into history section
    history_prompt = ""
    if history:
        summarized_history = "\n".join([
            f"User: {h['query']}\nAssistant: {h['response']}"
            for h in history[-3:]  # Only include last 3 exchanges for brevity
        ])
        history_prompt = f"Conversation History:\n{summarized_history}\n\n"

    # Filter top 2 relevant cases (can be adjusted based on similarity threshold)
    filtered_cases = retrieved_cases[:2]
    context = "\n\n".join(
        [f"Q: {case.get('input', '')}\nA: {case.get('output', '')}" for case in filtered_cases]
    )

    # Full prompt for the LLM
    prompt = f"""{history_prompt}Retrieved Medical Cases:\n{context}

Patient's Current Question:
{user_query}

Answer:"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a concise, helpful medical assistant trained on patient-doctor conversations. "
                    "Use retrieved medical cases and user history to generate thoughtful replies. "
                    "Never make a diagnosis. Always include a brief disclaimer at the top of your reply."
                )
            },
            {"role": "user", "content": prompt}
        ],
        temperature=0.4
    )

    return response.choices[0].message.content


# For testing this script directly
if __name__ == "__main__":
    from agents.vector_retrieval import retrieve_similar_cases

    query = "I feel dizzy and nauseous when I stand up"
    history = [
        {"query": "I had a mild headache last night", "response": "It could be due to dehydration or stress."}
    ]
    retrieved, _ = retrieve_similar_cases(query)
    print("🔍 Retrieved Cases Preview:\n", retrieved)
    answer = generate_response(query, retrieved, history)
    print("\nGenerated Answer:\n", answer)
