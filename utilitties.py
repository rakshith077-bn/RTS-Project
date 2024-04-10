import math

def calculate_priority(body, all_bodies):
    min_distance = min(body.distance(other) for other in all_bodies if other != body)
    return 1 / min_distance if min_distance != 0 else math.inf
