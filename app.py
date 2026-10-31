import streamlit as st
import streamlit.components.v1 as components
import requests
from groq import Groq

# ==========================================
# 1. PAGE CONFIGURATION & CYBERPUNK THEME
# ==========================================
st.set_page_config(
    page_title="NEO REPO AUDITOR 3D",
    page_icon="🎛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Deep Space Cyberpunk Matrix Injections
st.markdown("""
    <style>
    .stApp {
        background-color: #060713;
        color: #00ffcc;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Glowing Neon Glassmorphism Input Cards */
    div.stTextArea textarea {
        background-color: #0b0d1f !important;
        color: #39ff14 !important;
        border: 1px solid #00ffcc !important;
        box-shadow: 0 0 10px rgba(0, 255, 204, 0.2);
    }

    /* Swipe-Animated Execution Button */
    div.stButton > button {
        background: linear-gradient(135deg, #00ffcc #39ff14);
        color: #060713 !important;
        border: none;
        border-radius: 4px;
        padding: 14px 28px;
        font-weight: bold;
        letter-spacing: 2px;
        box-shadow: 0 0 15px rgba(0, 255, 204, 0.4);
        transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
    }
    
    div.stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 0 30px rgba(57, 255, 20, 0.8);
        color: #ffffff !important;
    }
    
    section[data-testid="stSidebar"] {
        background-color: #090a16;
        border-right: 1px solid #00ffcc;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. SIDEBAR UTILITIES & LLM SCHEDULER
# ==========================================
st.sidebar.title("🛸 CYBER PIPELINE")
st.sidebar.markdown("---")

api_key = st.sidebar.text_input("Groq Security Gateway Key", type="password", placeholder="gsk_...")
llm_engine = st.sidebar.selectbox(
    "LLM Architecture Node", 
    ["Local Gemma3 (Ollama Offline)", "openai/gpt-oss-120b", "llama3-8b-8192", "mixtral-8x7b-32768"]
)

st.sidebar.markdown("---")
st.sidebar.caption("System Framework: Node fully linked to local hardware topology.")

# ==========================================
# 3. INTERACTIVE 3D THREE.JS CANVAS INJECTION
# ==========================================
st.title("🛡️ NEO REPO AUDITOR 3D")
st.subheader("Autonomous Three.js / Cryptographic Code Scan Matrix")

# 3D Node Grid Canvas Injection mirroring CyberGuard 3D architecture layout
three_js_cyber_matrix = """
<div id="three-canvas-container" style="width: 100%; height: 300px; background: #03040a; border-radius: 8px; border: 1px solid #00ffcc; position: relative; overflow: hidden;">
    <div id="matrix-webgl" style="width: 100%; height: 100%;"></div>
    <div style="position: absolute; top: 15px; left: 15px; font-family: monospace; color: #39ff14; font-size: 11px; text-shadow: 0 0 5px #39ff14;">
        ⚡ GRAPHICS CORE: RTX 3050 TARGET ACTIVE // FRAME RATE: 60FPS STABLE //
    </div>
</div>

<script src="https://cloudflare.com"></script>
<script>
    // Initializing Three.js 3D Particle Cloud Net Matrix
    const container = document.getElementById('matrix-webgl');
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(60, container.clientWidth / 300, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
    
    renderer.setSize(container.clientWidth, 300);
    container.appendChild(renderer.domElement);
    
    // Generating Network Nodes (Particle Matrix)
    const particleCount = 250;
    const geometry = new THREE.BufferGeometry();
    const positions = new Float32Array(particleCount * 3);
    
    for(let i=0; i<particleCount*3; i+=3) {
        positions[i] = (Math.random() - 0.5) * 40;     // X axis range
        positions[i+1] = (Math.random() - 0.5) * 15;   // Y axis range
        positions[i+2] = (Math.random() - 0.5) * 20;   // Z axis range
    }
    
    geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    
    const material = new THREE.PointsMaterial({
        color: 0x00ffcc,
        size: 0.18,
        transparent: true,
        opacity: 0.85
    });
    
    const pointCloud = new THREE.Points(geometry, material);
    scene.add(pointCloud);
    camera.position.z = 18;

    // Animation Loop handling live orbital rotational tracking
    function animate() {
        requestAnimationFrame(animate);
        pointCloud.rotation.y += 0.002;
        pointCloud.rotation.x += 0.001;
        renderer.render(scene, camera);
    }
    
    // Dynamic aspect resizing boundary
    window.addEventListener('resize', () => {
        camera.aspect = container.clientWidth / 300;
        camera.updateProjectionMatrix();
        renderer.setSize(container.clientWidth, 300);
    });
    
    animate();
</script>
"""
components.html(three_js_cyber_matrix, height=315)

# ==========================================
# 4. SPLIT GRID CONTROLLER INTERFACE
# ==========================================
left_node, right_node = st.columns(2)

with left_node:
    st.markdown("### 📥 Code Segment Target Node")
    code_segment = st.text_area(
        "Deploy source snippet string context for execution checks:", 
        height=320, 
        placeholder="def shield_matrix():\n    pass"
    )
    execute_sequence = st.button("RUN COMPLIANCE PROTOCOL")

with right_node:
    st.markdown("### 📊 Compliance Threat Report Vector")
    
    if execute_sequence:
        if not code_segment.strip():
            st.error("❌ Action terminated: Code target node data missing.")
        else:
            with st.spinner("Analyzing parameters across cryptographic validation layers..."):
                
                # PIPELINE NODE 1: LOCAL OFFLINE LLM EXECUTION LAYER
                if llm_engine == "Local Gemma3 (Ollama Offline)":
                    try:
                        res = requests.post(
                            "http://localhost:11434/api/generate",
                            json={
                                "model": "gemma3:1b",
                                "prompt": f"Audit this code snippet for security threats, runtime bugs, and anti-patterns. Provide output inside a clean structured markdown table report:\n\n{code_segment}",
                                "stream": False
                            },
                            timeout=30
                        )
                        if res.status_code == 200:
                            st.success("🤖 Core Analysis Complete: Processed locally inside isolated GPU cluster.")
                            st.markdown(res.json().get("response"))
                        else:
                            st.error(f"Engine failure code: {res.status_code}")
                    except Exception as e:
                        st.error(f"Local link failed. Confirm background daemon runtime status. Context: {e}")
                
                # PIPELINE NODE 2: EXTERNAL CLOUD NETWORK CONNECTOR
                else:
                    if not api_key:
                        st.warning("🔒 Target selected requires a valid Groq Cloud Security Gateway validation string key.")
                    else:
                        try:
                            mapped_id = "llama3-8b-8192" if "llama3" in llm_engine else "mixtral-8x7b-32768"
                            client = Groq(api_key=api_key)
                            completion = client.chat.completions.create(
                                model=mapped_id,
                                messages=[{"role": "user", "content": f"Audit this code for vulnerabilities:\n\n{code_segment}"}],
                                temperature=0.2
                            )
                            st.success(f"⚡ Cloud Query Resolved via: {mapped_id}")
                            st.markdown(completion.choices.message.content)
                        except Exception as e:
                            st.error(f"Gateway execution failure: {e}")
    else:
        st.info("System idling in standby. Input raw package configuration array segments to trigger compilation analytics.")
