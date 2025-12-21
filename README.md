# 🧠 AI Log Intelligence & Incident Root Cause Analyzer

A **developer-first AI tool** that scans repositories, ingests logs and errors, and provides **AI-powered root cause explanations** using a **RAG (Retrieval-Augmented Generation) pipeline**.

This project is designed to work as a **CLI + API**, not a frontend UI — making it ideal for **local debugging, CI/CD pipelines, and production environments**.

---

## 🚀 What Problem Does This Solve?

Developers often struggle with:

* Large volumes of logs
* Distributed services
* Repeated production incidents
* Hard-to-trace root causes

This tool:

* Automatically scans a repository for error signals
* Builds a searchable AI memory of logs
* Answers *why something failed* using context-aware retrieval
* Works locally, offline, and without sending code to external services

---

## 🧩 Key Features

* 🔍 **Repo-aware scanning** – Automatically scans any repo for logs & errors
* 🧠 **RAG-based intelligence** – Uses embeddings + FAISS + LLM reasoning
* 🧪 **No training required** – Pure retrieval, no model fine-tuning
* 🧰 **CLI-first design** – Built for developers & automation
* 🔐 **Local-first & private** – Uses local LLMs (Ollama)
* ♻️ **Persistent memory** – Logs survive restarts
* 🏗️ **Production-ready architecture** – API, monitoring-ready, dockerizable

---

## 🏗️ Architecture Overview

```text
┌──────────────────────┐
│  Developer / CI/CD   │
│  (CLI Tool)          │
└─────────┬────────────┘
          │
          ▼
┌──────────────────────┐
│ FastAPI Backend      │
│  /ingest /query      │
└─────────┬────────────┘
          │
          ▼
┌──────────────────────┐
│ RAG Service          │
│  Retrieval + Reason  │
└─────────┬────────────┘
          │
          ▼
┌──────────────────────┐
│ FAISS Vector Store   │
│  Persistent Memory   │
└─────────┬────────────┘
          │
          ▼
┌──────────────────────┐
│ Ollama (LLM)         │
│  Root Cause Explain  │
└──────────────────────┘
```

---

## 📦 Tech Stack

* **Python 3.10+**
* **FastAPI** – Backend API
* **Typer** – CLI interface
* **FAISS** – Vector database
* **SentenceTransformers** – Embeddings
* **Ollama (Mistral / LLaMA)** – Local LLM
* **Rich** – CLI output formatting

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repo

```bash
git clone https://github.com/<your-username>/ai-log-intelligence.git
cd ai-log-intelligence
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Start Ollama (local LLM)

```bash
ollama serve
ollama pull mistral
```

---

## ▶️ Running the Backend API

```bash
python -m uvicorn backend.api.main:app --reload
```

API will be available at:

```
http://127.0.0.1:8000
```

Swagger Docs:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Using the CLI (Primary Interface)

### 🔍 Scan a repository and ingest logs

```bash
python -m cli.main scan .
```

What this does:

* Walks the repository
* Detects error lines (`ERROR`, `WARN`, `Exception`, etc.)
* Ingests them into the AI memory

---

### ❓ Ask AI about the issue

```bash
python -m cli.main query "Why did the payment service fail?"
```

Example output:

```text
🔍 Retrieved Logs
- services/payment/db.py: ERROR DB_TIMEOUT
- services/payment/cache.py: ERROR CACHE_MISS

🧠 AI Explanation
The payment service failed due to database timeouts, likely caused by slow
responses or connection pool exhaustion.
```

---

### 📄 Ingest a single log file

```bash
python -m cli.main ingest app.log
```

---

## 🔑 How Other Developers Can Use This

### Local debugging

```bash
ai-log scan .
ai-log query "Why is my app crashing?"
```

### CI/CD pipeline

```yaml
- name: AI Log Analysis
  run: |
    python -m cli.main scan .
    python -m cli.main query "Any critical failures?"
```

### Production incident analysis

* Periodically ingest logs
* Query during outages
* Get instant root cause summaries

---

## 🧠 What This Tool Does NOT Do (Yet)

* ❌ Auto-fix code
* ❌ Create PRs
* ❌ Replace debuggers

But the architecture **supports future upgrades**:

* Code-aware RAG
* Stack trace parsing
* Line-level diagnosis
* Automated remediation

---

## 🛣️ Roadmap

* [ ] Structured log enrichment (file, service, line)
* [ ] Dockerized deployment
* [ ] Prometheus + Grafana monitoring
* [ ] pip-installable CLI (`ai-log`)
* [ ] CI/CD templates
* [ ] Multi-language stack trace parsing

---

## 🎯 Who Is This For?

* Backend engineers
* SREs / DevOps
* Platform teams
* ML / GenAI engineers
* Anyone debugging complex systems

---

## 🏆 Why This Project Matters

This is **not a toy chatbot**.

It demonstrates:

* Real-world RAG architecture
* Production-minded GenAI engineering
* Developer-first tooling
* Local-first, privacy-respecting AI

---

## 📜 License

MIT License

