import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")

ADMIN_IDS = [int(admin_id) for admin_id in os.getenv("ADMINS").split(',')]
DB_URI = os.getenv("DB_URI")
