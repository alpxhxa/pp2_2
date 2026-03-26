import csv
from db import get_connection

def import_csv(filename):
    with get_connection() as conn:
        with conn.cursor() as cur:
            with open(filename,"r") as file:

                reader = csv.DictReader(file)

                for row in reader:

                    cur.execute("INSERT INTO contacts(name,phone) VALUES (%s,%s);", (row["name"], row["phone"]))

    
    print("Data Added")

if __name__ == "__main__":

    import_csv("data.csv")

