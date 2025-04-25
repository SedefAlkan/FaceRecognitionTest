
from dotenv import load_dotenv
import os
load_dotenv()


from opencv.fr import FR

# Get credentials from .env
BACKEND_URL = os.getenv("BACKEND_URL")
DEVELOPER_KEY = os.getenv("DEVELOPER_KEY")


sdk = FR(BACKEND_URL, DEVELOPER_KEY)
