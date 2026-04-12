# 🚀 Streamify AI — Production RAG + CAG Music Intelligence System

## 📌 Overview

**Streamify AI** is a production-grade AI system that combines **Retrieval-Augmented Generation (RAG)** and **Cache-Augmented Generation (CAG)** to deliver intelligent, real-time music recommendations.

The system integrates:

* 🎧 Semantic search (vector database)
* ⚡ Real-time data from Spotify API
* 🧠 Large Language Models (LLMs)
* 🚀 High-performance caching (Redis)

This architecture demonstrates how to build scalable, cost-efficient AI systems for real-world applications such as music streaming platforms.

---

## 🧠 Architecture

```text
User Query
   ↓
FastAPI (Async Backend)
   ↓
Redis Cache (CAG)  ← reduces cost & latency
   ↓
Vector DB (FAISS) ← semantic retrieval
   ↓
Spotify API       ← real-time enrichment
   ↓
Prompt Builder
   ↓
LLM (OpenAI)
   ↓
Final Answer
```

---

## ⚙️ Tech Stack

| Layer          | Technology           |
| -------------- | -------------------- |
| API            | FastAPI              |
| LLM            | OpenAI (gpt-4o-mini) |
| Embeddings     | SentenceTransformers |
| Vector DB      | FAISS                |
| Cache (CAG)    | Redis                |
| External Data  | Spotify Web API      |
| Async Requests | httpx                |

---

## 🔥 Features

* ✅ Hybrid RAG (Vector DB + External API)
* ✅ CAG (Redis-based caching layer)
* ✅ Async architecture (FastAPI + httpx)
* ✅ Modular & scalable design
* ✅ Real-time music recommendations
* ✅ Cost optimization via caching

---

## 📂 Project Structure

```text
streamify_ai_pro/
│
├── app.py                # FastAPI entrypoint
├── config.py            # Environment variables
├── requirements.txt
│
├── data/
│   └── songs.txt        # Initial dataset
│
├── rag/
│   ├── embedder.py      # Embedding model
│   ├── retriever.py     # FAISS retrieval
│   ├── spotify_api.py   # External API integration
│   ├── cache.py         # Redis caching (CAG)
│   ├── generator.py     # LLM interaction
│   └── pipeline.py      # RAG orchestration
```

---

## 🚀 Getting Started

### 1. Clone repository

```bash
git clone https://github.com/your-username/streamify-ai.git
cd streamify-ai
```

---

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup environment variables

#### 🔑 OpenAI

```bash
set OPENAI_API_KEY=your_openai_key
```

---

#### 🎵 Spotify API (Free)

Create app:

👉 https://developer.spotify.com/dashboard

Then:

```bash
set SPOTIFY_CLIENT_ID=your_client_id
set SPOTIFY_CLIENT_SECRET=your_client_secret
```

---

### 5. Run Redis (CAG)

```bash
docker run -p 6379:6379 redis
```

---

### 6. Start API

```bash
uvicorn app:app --reload
```

---

### 7. Test the API

Open:

👉 http://127.0.0.1:8000/docs

Example request:

```json
{
  "text": "chill music for night"
}
```

---

## 🧪 Example Output

```json
{
  "source": "generated",
  "answer": "You should try Drake and The Weeknd for a chill night vibe...",
  "retrieved": [...],
  "spotify": [...]
}
```

---

## ⚡ Performance Optimization (CAG)

The system uses Redis to cache responses:

* First request → LLM generates response
* Second identical request → served instantly from cache

```text
Result:
✔ Lower latency
✔ Reduced API cost
✔ Better scalability
```

---

## 🧠 Key Concepts Demonstrated

* Retrieval-Augmented Generation (RAG)
* Cache-Augmented Generation (CAG)
* Semantic search with embeddings
* Hybrid data pipelines (internal + external)
* Async API design
* AI system architecture (not just models)

---

## 📈 Future Improvements

* 🔹 User personalization (user embeddings)
* 🔹 Ranking models (learning-to-rank)
* 🔹 Streaming pipelines (Kafka)
* 🔹 Feature store integration (Databricks-style)
* 🔹 Multi-modal recommendations (audio + metadata)

---

## 💡 Use Cases

* Music recommendation systems
* AI assistants for streaming platforms
* Personalized content delivery
* Real-time AI enrichment systems

---

## 🧑‍💻 Author

Younes Mellouki — DATA Engineer
Specialized in:

* Machine Learning
* NLP & LLM Systems
* Data Engineering
* AI System Design

---

## ⭐ Final Note

This project demonstrates how to move from **ML models → real AI systems** by combining:

```text
Retrieval + Generation + Caching + APIs
```

👉 A key skill for modern AI Engineers.
