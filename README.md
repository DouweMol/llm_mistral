# Python Practice

This project uses the `llama-cpp-python` library with a local Mistral model for LLM tasks.

## Project Structure

- `.venv/` — Local virtual environment (excluded from Git)  
- `.vscode/` — Local VS Code settings (excluded from Git)  
- `models/mistral` — Subfolder with the model: mistral-7b-instruct-v0.2.Q4_K_M.gguf
- `scripts/` — Python script 
- `.gitignore` — Specifies files that need to be excluded from Git


## Setup

1. Create and activate a virtual environment:

python3 -m venv .venv
source .venv/bin/activate (Linux)

2. Install dependencies

pip install -r requirements.txt

3. Make sure the model is located at models/mistral/mistral-7b-instruct-v0.2.Q4_K_M.gguf

4. Run script

python scripts/main.py



