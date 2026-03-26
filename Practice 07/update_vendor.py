from db import get_connection

def update_name(new_name, con_id):
    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute(
                "UPDATE contacts SET name = %s WHERE id = %s;",
                (new_name, con_id)
            )

            print("Name is updated")


def update_phone(new_phone, con_id):
    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute(
                "UPDATE contacts SET phone = %s WHERE id = %s;",
                (new_phone, con_id)
            )

            print("Phone is updated")


id = input("ID: ")

choice = input("1 - by name, 2 - by phone: ")

if choice == "1":
    name = input("Name: ")
    update_name(name,id)

elif choice == "2":
    phone = input("Phone: ")
    update_phone(phone,id)