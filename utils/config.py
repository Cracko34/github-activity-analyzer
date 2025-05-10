import os
from dotenv import load_dotenv

load_dotenv()  # Carga desde .env

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    raise RuntimeError("Define GITHUB_TOKEN en tu .env")
