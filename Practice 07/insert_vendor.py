from db import get_connection

def insert_data(name,phone):
    
    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s);",
                (name, phone)
            )

            print("Data Added")


if __name__ == "__main__":

    name = input("Name: ")
    phone = input("Phone: ")
    insert_data(name,phone)