import streamlit as st
import streamlit.components.v1 as components
from groq import Groq
import requests
import json

# ==========================================
# 1. PAGE CONFIGURATION & CYBERPUNK THEME
# ==========================================
st.set_page_config(
    page_title="NEO REPO AUDITOR 3D",
    page_icon="🎛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Futuristic Neon CSS Styling & Swipe Card Animations
st.markdown("""
    <style>
    /* Neon Glow & Tech Themes */
    .stApp {
        background-color: #0d0e15;
        color: #e2c2f0;
    }
    
    /* Futuristic Code Audit Action Card with Swipe Hover Effect */
    div.stButton > button {
        background: linear-gradient(90deg, #8u5cf6, #ec4899);
        color: white !important;
        border: none;
        border-radius: 8px;
        padding: 12px 24px;
        font-weight: bold;
        box-shadow: 0 0 15px rgba(236, 72, 153, 0.4);
        transition: all 0.3s ease;
    }
    
    div.stButton > button:hover {
        transform: translateY(-2px) scale(1.02);
        box-shadow: 0 0 25px rgba(139, 92, 246, 0.8);
        background: linear-gradient(90deg, #ec4899, #8u5cf6);
    }
    
    /* Custom Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #12131e;
        border-right: 2px solid #1f2937;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. SIDEBAR UTILITIES & COMPONENT SELECTION
# ==========================================
st.sidebar.title("🎛️ CORE ENGINE STATUS")
st.sidebar.markdown("---")

# API Keys & Engine Selections
api_key = st.sidebar.text_input("Groq Cloud Key", type="password", placeholder="gsk_...")
llm_engine = st.sidebar.selectbox(
    "LLM Node Engine", 
    ["openai/gpt-oss-120b", "llama3-8b-8192", "mixtral-8x7b-32768", "Local Gemma3 (Ollama Offline)"]
)

st.sidebar.markdown("---")
st.sidebar.info("Status: System fully primed inside isolated container environment.")

# ==========================================
# 3. INTERACTIVE 3D CANVAS INJECTION
# ==========================================
st.title("⚡ NEO REPO AUDITOR 3D")
st.subheader("Autonomous Local AI Code Audit & Compliance Matrix")

three_js_canvas = """
<div id="canvas-container" style="width: 100%; height: 200px; background: radial-gradient(circle, #1a1c2e 0%, #0d0e15 100%); border-radius: 12px; border: 1px solid #374151; display: flex; align-items: center; justify-content: center;">
    <div style="text-align: center; color: #a78bfa; font-family: monospace;">
        <div style="font-size: 24px; font-weight: bold; margin-bottom: 8px; animation: pulse 2s infinite;">[ 3D CYBER NET MATRIX ACTIVE ]</div>
        <div style="font-size: 12px; color: #9ca3af;">Pipeline Nodes Interlinked. GPU Core Processing Standby.</div>
    </div>
</div>
<style>
@keyframes pulse {
    0% { opacity: 0.4; text-shadow: 0 0 5px #8b5cf6; }
    50% { opacity: 1; text-shadow: 0 0 20px #ec4899; }
    100% { opacity: 0.4; text-shadow: 0 0 5px #8b5cf6; }
}
</style>
"""
components.html(three_js_canvas, height=220)

# ==========================================
# 4. WORKSPACE LAYOUT & INPUT FIELDS
# ==========================================
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 📥 Source Repository Node Input")
    code_input = st.text_area(
        "Paste the raw source code segment here for real-time risk mitigation analysis:", 
        height=350, 
        placeholder="def analyze_security(repo):\n    pass"
    )
    
    audit_triggered = st.button("EXECUTE AUDIT SEQUENCE")

# ==========================================
# 5. CORE EXECUTION ENGINE PIPELINE
# ==========================================
with col2:
    st.markdown("### 📊 Compliance Matrix Output")
    
    if audit_triggered:
        if not code_input.strip():
            st.error("⚠️ Input node empty. Please populate the source code segment.")
        else:
            with st.spinner("Analyzing repository parameters across threat vector models..."):
                
                # OPTION A: LOCAL OFFLINE PROCESSING TRAIN
                if llm_engine == "Local Gemma3 (Ollama Offline)":
                    ollama_url = "http://localhost:11434/api/generate"
                    payload = {
                        "model": "gemma3:1b",
                        "prompt": f"Perform a comprehensive code review and vulnerability audit on this code snippet. Detail any potential performance bugs or security holes:\n\n```python\n{code_input}\n```",
                        "stream": False
                    }
                    
                    try:
                        res = requests.post(ollama_url, json=payload, timeout=30)
                        if res.status_code == 200:
                            ai_output = res.json().get("response")
                            st.success("✅ Analysis completed locally via GPU hardware acceleration.")
                            st.markdown(ai_output)
                        else:
                            st.error(f"❌ Ollama Local Daemon returned status code: {res.status_code}")
                    except Exception as e:
                        st.error(f"❌ Connection to local engine failed. Make sure Ollama is open. Error context: {e}")
                
                # OPTION B: CLOUD-BASED GROQ API PROCESSING ENGINE
                else:
                    if not api_key:
                        st.warning("⚠️ Cloud engine selected but Groq API key is missing from the sidebar Node.")
                    else:
                        try:
                            # Map UI engine selection to valid Groq Model ID
                            model_id = "llama3-8b-8192" if "llama3" in llm_engine else "mixtral-8x7b-32768"
                            if "gpt-oss-120b" in llm_engine:
                                model_id = "llama3-8b-8192" # Fallback mapping if custom engine tag isn't live on Groq host
                            
                            client = Groq(api_key=api_key)
                            completion = client.chat.completions.create(
                                model=model_id,
                                messages=[
                                    {
                                        "role": "user",
                                        "content": f"Perform a comprehensive code review and vulnerability audit on this code snippet. Detail any potential performance bugs or security holes:\n\n{code_input}"
                                    }
                                ],
                                temperature=0.3,
                                max_tokens=2048
                            )
                            
                            st.success(f"⚡ Analysis complete via Cloud Network Node: {model_id}")
                            st.markdown(completion.choices[0].message.content)
                        except Exception as e:
                            st.error(f"❌ Cloud execution aborted by host gateway error: {e}")
    else:
        st.info("System awaiting launch pulse. Input repository source parameters in the adjacent workspace node and trigger execution.")
