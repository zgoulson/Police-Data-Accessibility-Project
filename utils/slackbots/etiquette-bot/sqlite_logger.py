import sqlite3
import datetime

logDate = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
print(logDate)
conn = sqlite3.connect('message.db')

c = conn.cursor()

# c.execute("""CREATE TABLE messages (
#             timestamp text,
#             id integer
#             )""")

c.execute("INSERT INTO messages VALUES ('19/07/2020 14:0:11', 1594579781000500)")

conn.commit()

c.execute("SELECT * FROM messages WHERE id=1594579781000500")

print(c.fetchall())

conn.commit()

conn.close()
