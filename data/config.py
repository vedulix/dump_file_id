import os

from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

API_ID = str(os.getenv("API_ID"))
API_HASH = str(os.getenv("API_HASH"))
