# Local LLM Project

This project uses the **llama-cpp-python** library with a local **Mistral** model for LLM tasks.  
It can be run either **locally with Python** or inside a **Docker container**.

---

## Project Structure


- `.venv/` — Local virtual environment (excluded from Git)  
- `.vscode/` — Local VS Code settings (excluded from Git)  
- `models/mistral` — Subfolder with the model: mistral-7b-instruct-v0.2.Q4_K_M.gguf
- `scripts/` — Python script 
- `.gitignore` — Specifies files that need to be excluded from Git
- `Dockerfile` # Docker build file
- `docker-compose.yml` # Docker Compose setup
- `.dockerignore` # Excludes files from Docker build context


## Setup (Local)

1. Create and activate a virtual environment
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # Linux / Mac
   .venv\Scripts\activate      # Windows

2. Install dependencies
pip install -r requirements.txt

3. Make sure the model is located at models/mistral/mistral-7b-instruct-v0.2.Q4_K_M.gguf

4. Run script
python scripts/main.py

## Setup (Docker - CPU)

1. Build the container: 
docker compose build

2. Start the service:
docker compose up

3. Run the script inside the container:
docker compose run --rm app python scripts/main.py

## Setup (Docker - GPU with CUDA)
If you have an NVIDIA GPU and want to accelerate inference:

1. Install NVIDIA Container Toolkit
Follow the instructions here:
https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html

2. Update docker-compose.yml
Add the following under your service (e.g., app):
    deploy:
    resources:
        reservations:
        devices:
            - driver: nvidia
            count: all
            capabilities: [gpu]

3. Rebuild and run with GPU support:
    docker compose build
    docker compose up
    
    or run directly with:
    docker compose run --rm --gpus all app python scripts/main.py


## Notes
The models/ directory is mounted into the container, so you don’t need to copy the model inside the image.
For CPU-only use, the default Docker setup works out of the box.
For GPU acceleration, ensure you have the NVIDIA drivers and Container Toolkit installed.



