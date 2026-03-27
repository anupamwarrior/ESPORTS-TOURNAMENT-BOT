maps_cycle = ["Erangel", "Miramar", "Sanhok"]
current_index = 0

def next_map():
    global current_index
    map_name = maps_cycle[current_index]
    current_index = (current_index + 1) % len(maps_cycle)
    return map_name
