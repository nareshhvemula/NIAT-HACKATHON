import streamlit as st
import streamlit.components.v1 as components
from groq import Groq

# 1. Page Configuration & Cyberpunk Theme Injection
st.set_page_config(
    page_title="NEO-REPO AUDITOR 3D", 
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Futuristic Neon CSS Styling & Swipe Card Animations
st.markdown("""
    <style>
    /* Neon Glow & Tech Themes */
    .stApp {
        background-color: #0d0e15;
        color: #e2e8f0;
    }
    
    /* Futuristic Code Audit Action Card with Swipe Hover Effect */
    div.stButton > button {
        background: linear-gradient(90deg, #8b5cf6, #ec4899);
        color: white !important;
        border: none;
        padding: 12px 24px;
        font-weight: bold;
        border-radius: 8px;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: all 0.4s ease;
        box-shadow: 0 0 15px rgba(139, 92, 246, 0.4);
        position: relative;
        overflow: hidden;
    }
    
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 0 25px rgba(236, 72, 153, 0.7);
        background: linear-gradient(90deg, #ec4899, #8b5cf6);
    }
    
    /* Tech Container Panel Styling */
    .tech-card {
        background: rgba(30, 41, 59, 0.5);
        border: 1px solid rgba(139, 92, 246, 0.2);
        padding: 20px;
        border-radius: 12px;
        backdrop-filter: blur(10px);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Interactive Three.js 3D Particle Nexus Header
three_js_canvas = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://cloudflare.com"></script>
    <style>
        body { margin: 0; overflow: hidden; background-color: #0d0e15; }
        canvas { display: block; width: 100vw; height: 160px; }
    </style>
</head>
<body>
    <div id="canvas-container"></div>
    <script>
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / 160, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
        renderer.setSize(window.innerWidth, 160);
        document.getElementById('canvas-container').appendChild(renderer.domElement);

        const geometry = new THREE.BufferGeometry();
        const vertices = [];
        for (let i = 0; i < 400; i++) {
            vertices.push(Math.random() * 40 - 20); // X
            vertices.push(Math.random() * 10 - 5);   // Y
            vertices.push(Math.random() * 20 - 10);  // Z
        }
        geometry.setAttribute('position', new THREE.Float32BufferAttribute(vertices, 3));
        
        const material = new THREE.PointsMaterial({ color: 0x8b5cf6, size: 0.15, transparent: true, opacity: 0.8 });
        const particles = new THREE.Points(geometry, material);
        scene.add(particles);
        camera.position.z = 8;

        let clock = 0;
        function animate() {
            requestAnimationFrame(animate);
            clock += 0.01;
            particles.rotation.y = clock * 0.1;
            particles.rotation.x = Math.sin(clock * 0.2) * 0.1;
            renderer.render(scene, camera);
        }
        animate();

        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / 160;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, 160);
        });
    </script>
</body>
</html>
"""

# Render the 3D visual component at the header banner spot
components.html(three_js_canvas, height=160, scrolling=False)

st.title("⚡ NEO-REPO AUDITOR 3D")
st.caption("Quantum Static Multi-Agent Verification Platform")
st.markdown("---")

# 3. Sidebar Configuration Console
st.sidebar.header("🌌 Core Matrix")
api_key = st.sidebar.text_input("Access Authorization Key:", type="password", help="Groq API Token")

with st.sidebar.expander("🔮 Model Architectures", expanded=True):
    model_choice = st.selectbox(
        "Select LLM Node Engine:", 
        ["openai/gpt-oss-120b", "llama-3.3-70b-versatile", "llama3-70b-8192", "mixtral-8x8b-32768"]
    )
    temperature = st.slider("Quantum Randomness Variance:", 0.0, 1.0, 0.2)

# 4. Source Matrix Workspace Panel
st.subheader("📥 Data Buffer Upload Matrix")
input_mode = st.radio("Choose Input Matrix Format:", ["Raw Text Stream Injection", "Direct Core Local File Transmission"], horizontal=True)

code_input = ""
if input_mode == "Raw Text Stream Injection":
    code_input = st.text_area(
        "Paste target source string block inside this terminal frame:", 
        height=250, 
        placeholder="// Insert code architecture array vectors...",
        key="custom_code_area"
    )
else:
    uploaded_file = st.file_uploader("Inject code segment manifest directly:", type=["py", "js", "ts", "go"])
    if uploaded_file:
        code_input = uploaded_file.read().decode("utf-8")
        st.success(f"File verification vector complete: {uploaded_file.name}")

st.markdown("---")

# 5. Core Trigger Action Loop
if st.button("🚀 INITIATE QUANTUM ARCHITECTURE AUDIT"):
    if not api_key:
        st.warning("🔒 Authorization Key vector missing. Please configure your token frame.")
    elif not code_input.strip():
        st.error("❌ Data stream buffer empty. Please feed valid script instructions.")
    else:
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        status_text.text("⚡ Synthesizing local environment instances...")
        progress_bar.progress(30)
        
        try:
            client = Groq(api_key=api_key)
            
            system_prompt = (
                "You are an expert senior software engineer and security auditor. "
                "Analyze the provided code carefully. Provide feedback divided into three strict sections: "
                "1. BUGS & LOGIC ERRORS, 2. SECURITY FLAWS, 3. OPTIMIZATION SUGGESTIONS. "
                "Be direct, highly precise, and provide corrected code blocks where applicable."
            )
            
            status_text.text("🪐 Launching deep semantic inference engines via Groq matrix...")
            progress_bar.progress(70)
            
            response = client.chat.completions.create(
                model=model_choice,
                temperature=temperature,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"Review this code:\n\n```\n{code_input}\n```"}
                ]
            )
            
            # FIXED: Added [0] index accessor block here
            report_out = response.choices[0].message.content
            
            progress_bar.progress(100)
            status_text.text("✅ Security verification sequence operational!")
            
            # 6. Tabbed Workspace Output Matrix
            st.subheader("📊 Generated Metrics Framework")
            res_tab1, res_tab2 = st.tabs(["⚡ Core Structural Analysis Ledger", "💾 Compile System Blueprint (.md)"])
            
            with res_tab1:
                st.markdown(f'<div class="tech-card">{report_out}</div>', unsafe_allow_html=True)
                
            with res_tab2:
                st.download_button(
                    label="💾 TRANSMIT LOCAL ANALYSIS BUILD",
                    data=report_out,
                    file_name="quantum_audit_manifest.md",
                    mime="text/markdown"
                )
                
        except Exception as e:
            st.error(f"💥 Kernel panic exception standard return: {e}")
