import os
import psycopg
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

def get_connection():
    conn_string = os.getenv("DATABASE_URL")
    return psycopg.connect(conn_string)