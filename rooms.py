import random
import string
from database import cursor, conn

def generate_room():
    room_id = ''.join(random.choices(string.digits, k=6))
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    cursor.execute("INSERT INTO rooms (room_id, password) VALUES (?, ?)", (room_id, password))
    conn.commit()
    return room_id, password
