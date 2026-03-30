import streamlit as st
import requests

# -------------------------------
# BASIC ANALYSIS (Fallback)
# -------------------------------
def basic_analysis(log):

    if "vip" in log.lower():
        return {
            "analysis": """Root Cause:
All pool members down or VIP disabled

Troubleshooting:
1. Check virtual server status
2. Verify pool members
3. Check health monitor

Fix:
Enable VIP or fix backend servers
""",
            "command": "tmsh show ltm pool"
        }

    elif "ssl" in log.lower():
        return {
            "analysis": """Root Cause:
SSL certificate issue

Troubleshooting:
1. Check SSL profile
2. Verify certificate expiry
3. Check cipher settings

Fix:
Update certificate
""",
            "command": "tmsh list ltm profile client-ssl"
        }

    elif "timeout" in log.lower():
        return {
            "analysis": """Root Cause:
Backend server not responding

Troubleshooting:
1. Check pool members
2. Ping backend servers
3. Check firewall rules

Fix:
Restart backend or fix network issue
""",
            "command": "tmsh show ltm pool"
        }

    else:
        return {
            "analysis": "Basic analysis: Unable to detect issue.",
            "command": "Check logs manually"
        }


# -------------------------------
# AI ANALYSIS (Ollama)
# -------------------------------
def ai_analysis(log):

    prompt = f"""
    You are a senior F5 L3 network engineer.

    Analyze this issue:

    {log}

    Provide structured output:

    Root Cause:
    ...

    Troubleshooting:
    1.
    2.
    3.

    Fix:
    ...

    Suggested Command:
    ...
    """

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )

        data = response.json()

        if "response" in data:
            return data["response"]
        else:
            return "⚠️ No response from Ollama"

    except Exception as e:
        return f"⚠️ AI Error: {str(e)}"


# -------------------------------
# UI
# -------------------------------
st.set_page_config(page_title="F5 Troubleshooter", layout="centered")

st.title("🔧 F5 AI Troubleshooter (Basic + Ollama)")

st.info("Supports Basic Logic + AI (Ollama) + File Upload + Command Suggestion")

# Mode Selection
mode = st.radio(
    "Select Mode",
    ["Basic", "AI (Ollama)"]
)

# File Upload
uploaded_file = st.file_uploader("Upload log file (.txt)")

# Input Handling
if uploaded_file is not None:
    log = uploaded_file.read().decode("utf-8")
else:
    log = st.text_area("Enter your issue or log:")

# Button
if st.button("Analyze"):

    if not log:
        st.warning("Please enter or upload a log")
    else:
        with st.spinner("Analyzing..."):

            if mode == "Basic":
                result = basic_analysis(log)

                st.subheader("📊 Analysis Result")
                st.write(result["analysis"])

                st.subheader("💻 Suggested Command")
                st.code(result["command"])

                if st.button("Run Fix (Simulation)"):
                    st.success("Executing command...")
                    st.write("Output: Simulated response")

            else:
                result = ai_analysis(log)

                st.subheader("🤖 AI Analysis")
                st.write(result)
