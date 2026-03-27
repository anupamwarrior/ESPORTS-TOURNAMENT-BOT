import sqlite3

conn = sqlite3.connect("scrims.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS teams (id INTEGER PRIMARY KEY, name TEXT, player1 TEXT, player2 TEXT, player3 TEXT, player4 TEXT, points INTEGER DEFAULT 0)")
cursor.execute("CREATE TABLE IF NOT EXISTS matches (id INTEGER PRIMARY KEY, team TEXT, kills INTEGER, placement INTEGER, total_points INTEGER)")
cursor.execute("CREATE TABLE IF NOT EXISTS rooms (id INTEGER PRIMARY KEY, room_id TEXT, password TEXT)")

conn.commit()
