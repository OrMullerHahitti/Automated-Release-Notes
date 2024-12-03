# backend/app/utils/config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

LLM_API_URL = os.getenv("LLM_API_URL", "https://api.example.com/generate")
LLM_API_KEY = os.getenv("LLM_API_KEY")
