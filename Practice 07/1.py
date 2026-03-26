from db import get_connection

def delete_data():

    with get_connection() as conn:
        with conn.cursor() as cur:

            cur.execute("DELETE FROM contacts WHERE name = %s",(name,))
            cur.commit()