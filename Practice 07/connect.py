import os
import psycopg
from dotenv import load_dotenv

# загружаем .env
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

# берем строку подключения
conn_string = os.getenv("DATABASE_URL")

try:
    with psycopg.connect(conn_string) as conn:
        print("Подключение успешно!")

        with conn.cursor() as cur:
            cur.execute("SELECT 1;")
            result = cur.fetchone()
            print(result)

except Exception as e:
    print("Ошибка подключения:")
    print(e)

print("ENV PATH:", env_path)
print("VALUE:", os.getenv("DATABASE_URL"))