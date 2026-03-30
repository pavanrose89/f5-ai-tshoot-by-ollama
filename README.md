# 🔧 F5 AI Troubleshooter (Ollama)

> AI-powered troubleshooting tool for F5 / Network Engineers  
> Built using Python, Streamlit, and local LLM (Ollama)

---

## 🚀 Overview

F5 AI Troubleshooter helps engineers quickly analyze network issues such as:

- VIP down  
- SSL errors  
- Timeout issues  

It provides:
- Root cause analysis  
- Troubleshooting steps  
- Fix recommendations  
- Suggested F5 commands  

---

## ✨ Features

- 🤖 AI-powered analysis using Ollama (local LLM)  
- ⚡ Dual mode: Basic + AI  
- 📂 Upload log files (.txt)  
- 💻 Suggested F5 commands  
- 🛠 Automation simulation  
- 🎨 Simple and clean UI  

---

## 🧠 How It Works

User Input (UI)
↓
Analysis Engine (AI / Basic Logic)
↓
Processing
↓
Output (Root Cause + Fix + Commands)

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Ollama (Local LLM)  
- Requests  

---

## ▶️ Getting Started

### 1️⃣ Install dependencies

```bash
pip install streamlit requests

## 2️⃣ Start Ollama

bash
ollama run llama3
   OR
ollama run phi3

## 3️⃣ Run the application
bash

streamlit run ui-olam.py

🧪 Example Input

VIP 10.10.10.1 is down and all pool members are unavailable

💼 Use Case

This tool helps:

Network Engineers

F5 Administrators

Support Teams

Quickly diagnose and troubleshoot real-world issues.

🔮 Future Enhancements

🔗 Real F5 device integration (SSH / API)

💬 Chat-based interface

📊 Dashboard with analytics

☁️ Cloud deployment

🙌 Key Learnings

AI + Networking integration

Prompt engineering

UI development with Streamlit

Automation mindset

⭐ Support
If you find this project useful, consider giving it a ⭐ on GitHub!
