import sqlite3

# create a table within the database (if it doesn't exist)
def create_table():
    conn = sqlite3.connect('contact_page_messages.db')  # create a db connection
    c = conn.cursor()  # create a cursor

    c.execute("""CREATE TABLE form_response (
        date_sent text, 
        name text, 
        email text, 
        company text,
        user_msg text
        )""")

create_table()