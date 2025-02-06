import os

API_ID    = os.environ.get("API_ID", "18116881")
API_HASH  = os.environ.get("API_HASH", "cca3bacf40fb3ebcb4f075b2e46ff1bd")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7958229600:AAHqpzrkOdzCNn-0QF5JOsi6bLvuxn9ETBM") 
WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
