import random
from solarsystem import Planet, SolarSystem 
import math

solar_system = SolarSystem(width=1400, height=900) 
solar_system_instance = SolarSystem(width=1400, height=900) 

def move_meteor(meteor):
    """Moves a meteor randomly, with optional constraints.

    Args:
        meteor: A dictionary representing the meteor object. 
                Expects keys like 'x', 'y', 'velocity_x', 'velocity_y' 

    """
    # Basic random movement
    meteor['x'] += random.uniform(-meteor['velocity_x'], meteor['velocity_x'])
    meteor['y'] += random.uniform(-meteor['velocity_y'], meteor['velocity_y'])

    # Optional: Screen boundaries
    if meteor['x'] < 0 or meteor['x'] > solar_system:
        meteor['velocity_x'] *= -1  # Bounce off left/right edges
    if meteor['y'] < 0 or meteor['y'] > solar_system:
        meteor['velocity_y'] *= -1  # Bounce off top/bottom edges

    # Optional: Simulate gravity well of a planet
    for planet in Planet: 
        dx = planet['x'] - meteor['x']
        dy = planet['y'] - meteor['y']
        distance = (dx**2 + dy**2) ** 0.5  
        if distance < planet['gravity_radius']:
            gravity_force = planet['mass'] / distance**2  
            angle = math.atan2(dy, dx)
            meteor['velocity_x'] += gravity_force * math.cos(angle)
            meteor['velocity_y'] += gravity_force * math.sin(angle) 

