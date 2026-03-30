# 🔧 F5 AI Troubleshooter (Ollama)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![AI](https://img.shields.io/badge/AI-Ollama-green)
![Status](https://img.shields.io/badge/Status-Active-success)

> AI-powered troubleshooting assistant for F5 / Network Engineers
> Built using Python, Streamlit, and local LLM (Ollama)

---

## 🎥 Demo

![Demo](images/demo.gif)

---

## 🚀 Overview

F5 AI Troubleshooter is a smart tool designed to help engineers quickly diagnose and resolve common network issues such as:

* VIP down
* SSL handshake failures
* Application timeouts

It provides:

* Root cause analysis
* Step-by-step troubleshooting
* Fix recommendations
* Suggested F5 commands

---

## 🔥 Highlights

* Built real-world F5 troubleshooting assistant
* Integrated local LLM (Ollama) for offline AI
* Implemented dual-mode (Basic + AI) architecture
* Designed clean UI using Streamlit
* Added automation simulation for commands

---

## ✨ Features

* 🤖 AI-powered analysis using Ollama (local LLM)
* ⚡ Dual mode: Basic + AI
* 📂 Upload log files (.txt)
* 💻 Suggested F5 commands
* 🛠 Automation simulation
* 🎨 Simple and interactive UI

---

## 🧠 How It Works

```
User Input (UI)
      ↓
Analysis Engine (AI / Basic Logic)
      ↓
Processing
      ↓
Output (Root Cause + Fix + Commands)
```

---

## 🤖 AI Integration

* Uses Ollama local LLM for inference
* Sends prompt via REST API (`localhost:11434`)
* Processes response and displays structured output
* Falls back to basic logic if AI is unavailable

---

## 📁 Project Structure

```
ui-olam.py        # Main application
requirements.txt
README.md
images/           # Screenshots / demo
```

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Ollama (Local LLM)
* Requests

---

## ▶️ Getting Started

### 1️⃣ Install dependencies

```bash
pip install streamlit requests
```

---

### 2️⃣ Start Ollama

```bash
ollama run llama3
  OR
ollama run phi3
```

---

### 3️⃣ Run the application

```bash
streamlit run ui-olam.py
```

---

## 🧪 Example Input

```
VIP 10.10.10.1 is down and all pool members are unavailable
```

---

## 💼 Use Case

This tool helps:

* Network Engineers
* F5 Administrators
* Support Teams

Quickly diagnose and troubleshoot real-world issues using AI.

---

## 🔮 Future Enhancements

* 🔗 Real F5 device integration (SSH / API)
* 💬 Chat-based interface
* 📊 Dashboard with analytics
* ☁️ Cloud deployment

---

## 🙌 Key Learnings

* AI + Networking integration
* Prompt engineering
* UI development with Streamlit
* Automation mindset

---

## ⭐ Support

If you found this useful, consider giving a ⭐ on GitHub!
