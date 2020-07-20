import sqlite3
import datetime
from dotenv import load_dotenv
load_dotenv()
# logDate = datetime.datetime.fromtimestamp(1595123722.000700)

# create a default path to connect to and create (if necessary) a database
# called 'processed_messages.db' in the same directory as this script
DEFAULT_PATH = os.getenv('PROCESSED_MESSAGES_DB')
def db_connect(db_path=DEFAULT_PATH):
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except Error as e:
        print(e)
    return conn

def init_db():
    db = db_connect()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

def create_table(conn,):
c = conn.cursor()

# # c.execute("""CREATE TABLE messages (
# #             timestamp text,
# #             id integer
# #             )""")
#
# c.execute("INSERT INTO messages VALUES ('19/07/2020 14:0:11', 1594579781000500)")
# conn.commit()

c.execute("SELECT * FROM messages WHERE id=1594579781000500")
print(c.fetchall())
conn.commit()

conn.close()
