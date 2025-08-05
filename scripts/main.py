# Author: Douwe
# Date: 2025-08-05
# -*- coding: utf-8 -*-

"""
Description: lokale llama_cpp wrapper voor het uitvoeren van LLM-taken.
Deze code maakt gebruik van de llama_cpp bibliotheek om een lokaal LLM-model te laden en te gebruiken voor tekstgeneratie.
Het model moet lokaal beschikbaar zijn in het opgegeven pad.
Laadt het Mistral 7B Instruct model en voert een simpele prompt uit.
"""

from pathlib import Path
from llama_cpp import Llama

# Dynamisch pad naar het model (relatief t.o.v. dit script)
script_dir = Path(__file__).resolve().parent
model_path = script_dir.parent / "models" / "mistral" / "mistral-7b-instruct-v0.2.Q4_K_M.gguf"

# Initialiseer de Llama-wrapper met het model
llm = Llama(model_path=str(model_path), n_ctx=2048, n_threads=8)

# Geef een prompt
prompt = "Wat is de hoofdstad van Nederland?"

# Genereer een antwoord
output = llm(prompt, max_tokens=128, stop=["</s>"])

# Print het antwoord (de gegenereerde tekst)
print("Antwoord:", output['choices'][0]['text'].strip())

