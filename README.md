# 🧠 Agentic MedBot

**Agentic MedBot** is a Retrieval-Augmented Generation (RAG)-based medical chatbot powered by Large Language Models (LLMs). It simulates doctor-patient conversations using a dataset of 100k dialogues, leveraging agent-based architecture to enable modular reasoning and context-aware responses — all without the need for fine-tuning.

---

## 📌 Features

- 🧩 **Agent-based architecture** for modular task delegation.
- 🔎 **Dense retrieval** using FAISS and OpenAI embeddings.
- 🧠 **RAG-based response generation** with GPT-4 or Claude.
- 🧪 Optional **response validation** for medical safety.
- 📦 Easily extensible with new tools, agents, or graphs.

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/agentic-medbot.git
cd agentic-medbot
```

### 2. Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_openai_api_key
MODEL_PROVIDER=openai  # or anthropic
```

### 5. Build the vector index

```bash
python vector_store/build_index.py
```

### 6. Run the bot

```bash
python main.py
```

---

## 🧠 How It Works

1. **User submits a query** (e.g., "What causes chest pain?")
2. **Vector retrieval agent** finds relevant medical conversations.
3. **RAG generation agent** combines user input + context to generate an answer.
4. **Validation agent** (optional) checks for safety and hallucinations.
5. **Formatter agent** prepares the response for display or API delivery.

---

## ⚙️ Tech Stack

- Python 3.10+
- FAISS for similarity search
- OpenAI / Anthropic APIs
- dotenv for configuration
- jsonlines for data handling
- LangChain or LlamaIndex (optional)

---

## 📄 Dataset Format

The dataset is a `.jsonl` file containing 100,000 instruction-formatted entries like:

```json
{
  "instruction": "What are the symptoms of anemia?",
  "response": "Symptoms of anemia include fatigue, weakness, pale skin..."
}
```

You can replace this file with any similar medical conversation dataset.

---

## ⚠️ Disclaimer

> This is a **research and educational project**. It is **not a substitute for professional medical advice, diagnosis, or treatment**. Always consult a licensed healthcare provider for medical concerns.

---

## 🔮 Future Plans

- Add multi-turn conversation memory
- Integrate external sources like PubMed
- Deploy with FastAPI + Streamlit/Gradio frontend
- Add LLM-based re-ranker or confidence scorer
- Dockerize for easy deployment

---

## 🤝 Contributing

1. Fork the repo
2. Create a new branch
3. Make your changes
4. Submit a pull request

Issues and suggestions are welcome!

---
## 📫 Contact

Feel free to reach out via GitHub Issues or email: `baibhav06june@gmail.com`
