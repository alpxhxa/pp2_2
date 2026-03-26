from db import get_connection

def delete_name(name):
    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute("DELETE FROM contacts WHERE name = %s;",(name,))
            print("Name Deleted")

def delete_phone(phone):
    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute("DELETE FROM contacts WHERE phone = %s;",(phone,))
            print("Phone Deleted")


choice = input("1 - name, 2 - phone: ")

if choice == "1":
    name = input("Name: ")
    delete_name(name)

elif choice == "2":
    phone = input("Phone: ")
    delete_phone(phone)