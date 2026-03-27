def calculate_points(kills, placement):
    placement_points = {1: 15, 2: 12, 3: 10, 4: 8, 5: 6, 6: 4, 7: 2, 8: 1}
    return kills + placement_points.get(placement, 0)
