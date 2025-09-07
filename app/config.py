import os
from dotenv import load_dotenv

load_dotenv()

APP_TITLE = os.getenv("APP_TITLE", "Gestion d'une bibliothèque")
WINDOW_SIZE = os.getenv("WINDOW_SIZE", "925x500+300+200")
DB_PATH = os.getenv("DB_PATH", "data/mydb.db")
