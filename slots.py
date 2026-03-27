from database import cursor

MAX_SLOTS = 25

def assign_slots():
    cursor.execute("SELECT name FROM teams")
    teams = [t[0] for t in cursor.fetchall()]
    return {team: i+1 for i, team in enumerate(teams[:MAX_SLOTS])}
