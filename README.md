# NIAT Hackathon — Local AI Stack

An open-source local AI assistant engine built during the NIAT Hacktoberfest Hackathon framework. This project leverages an isolated backend environment to pipeline queries into a locally hosted micro-LLM model for privacy-focused, zero-latency inferences.

## 🚀 Technical Architecture
- **Language Environment:** Python 3.14 (Stable layout configuration)
- **Model Engine Runtime:** Ollama Server API Core Engine
- **Active Model Weights:** `gemma3:1b` (Lightweight edge-optimized parameters running on dedicated GPU hardware)
- **Backend Application Context:** FastAPI & Uvicorn Framework Pipelines

## 🛠️ Local Environment Workspace Setup

Ensure your local Ollama daemon runtime environment is running in the background, then set up the sandbox folder directory:

```bash
# Navigate to your hackathon directory
cd "NIAT Hackathon"

# Initialize and activate the stable isolated environment profile
py -3.14 -m venv .venv314
.venv314\Scripts\Activate.ps1

# Install runtime package dependencies
python -m pip install fastapi uvicorn chromadb requests transformers
```

## 🤖 Verification Tests
Run the pipeline connection layer utility script to confirm API communication status:
```bash
python test_ai.py
```
