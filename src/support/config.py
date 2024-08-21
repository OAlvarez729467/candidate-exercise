import os
from dotenv import load_dotenv

# Loads environment variables from .env
load_dotenv()

API_BASE_URL = os.getenv('API_BASE_URL', 'http://127.0.0.1:5000')
# API_TOKEN = os.getenv('API_TOKEN', 'default-token')
