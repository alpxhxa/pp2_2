from db import get_connection

def select_data():

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute("SELECT * FROM contacts;")
            rows = cur.fetchall()

            for row in rows:
                print(row, end = " ")

def search_by_name(name):

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute("SELECT * FROM contacts WHERE name ILIKE %s;",
                (f"%{name}%",)
            )
            print(cur.fetchall())


def search_by_phone_prefix(prefix):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM contacts WHERE phone LIKE %s;",
                (f"{prefix}%",)
            )
            print(cur.fetchall(), end = " ")



choice = input("1 - все, 2 - поиск по имени, 3 - по телефону: ")

if choice == "1":
    select_data()

elif choice == "2":
    name = input("Введите имя: ")
    search_by_name(name)

elif choice == "3":
    prefix = input("Введите начало номера: ")
    search_by_phone_prefix(prefix)