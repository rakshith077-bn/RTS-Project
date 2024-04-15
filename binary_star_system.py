import tracemalloc 
import csv 
import random
import turtle
from solarsystem import SolarSystem  
from solarsystem import Planet
from celestialbody import Sun1, Sun2 

solar_system = SolarSystem(width=1400, height=900) 

# Define the suns and planets
suns = (
    Sun1(solar_system, mass=10_000, position=(-200, 0), velocity=(0, 3.5)),
    Sun2(solar_system, mass=10_000, position=(200, 0), velocity=(0, -3.5)),
)

planets = (
    Planet(solar_system, mass=2, position=(50, 0), velocity=(0, 11)), 
    Planet(solar_system, mass=2, position=(-350, 0), velocity=(0, -10)), 
    Planet(solar_system, mass=2, position=(0, 200), velocity=(-2, -7)), 
)

tracemalloc.start()
old_limit = tracemalloc.get_traceback_limit()

meteor_turtles = []

def create_meteor_turtle(x, y):
    # Create a new turtle object
    meteor_turtle = turtle.Turtle()
    meteor_turtle.speed(0)  # Set the drawing speed to maximum
    meteor_turtle.shape("circle")  # Set the shape of the turtle to a circle
    meteor_turtle.color("gray")  # Set the color of the turtle to gray
    meteor_turtle.penup()  # Lift the pen up to prevent drawing lines
    meteor_turtle.goto(x, y)  # Move the turtle to the specified position
    meteor_turtles.append(meteor_turtle)  # Append the turtle to the list

def move_meteor(meteor):
    # Update meteor position to move in a straight line
    meteor['x'] += meteor['velocity_x']
    meteor['y'] += meteor['velocity_y']
    print(f"\n Meteor moved to ({meteor['x']}, {meteor['y']}) \n")

meteors = []

def tdm_schedule(meteors, time_slot):
    for meteor in meteors:
        # Check if the meteor's time slot matches the current time
        if meteor['time_slot'] == time_slot:
            # Move the meteor
            move_meteor(meteor)
            print(f"Moving meteor at position ({meteor['x']}, {meteor['y']})")

# Add meteors from the left side
for _ in range(4):
    meteors.append({'x': random.randint(-1000, -800), 'y': random.randint(-500, 500), 'velocity_x': random.uniform(5, 10), 'velocity_y': 0})

# Add meteors from the top and bottom
for _ in range(4):
    x = random.randint(-800, 800)
    y = random.choice([-500, 500])
    meteors.append({'x': x, 'y': y, 'velocity_x': random.uniform(-10, 10), 'velocity_y': random.uniform(5, 10) if y == -500 else random.uniform(-10, -5)})

# Add meteors from the right side
for _ in range(4):
    meteors.append({'x': random.randint(800, 1000), 'y': random.randint(-500, 500), 'velocity_x': random.uniform(-10, -5), 'velocity_y': 0})

for meteor in meteors:
    create_meteor_turtle(meteor['x'], meteor['y'])

# Assign time slots to meteors
num_time_slots = 10
time_slot_duration = 10
for i, meteor in enumerate(meteors):
    meteor['time_slot'] = i % num_time_slots

with open('snapshot_binary.csv', 'a', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Snapshot", "Size", "Count", "Average Count"])

    snapshot_count = 0

    while True:
        snapshot_binary1 = tracemalloc.take_snapshot()
        
        solar_system.calculate_all_body_interactions()
        solar_system.update_all()

        snapshot_binary2 = tracemalloc.take_snapshot()

        top_stats = snapshot_binary2.compare_to(snapshot_binary1, 'lineno')

        print(" \nTop Stats \n")
        for stat in top_stats[:5]:
            size_change = stat.size
            count_change = stat.count
            average_change = stat.size / stat.count if stat.count != 0 else 0

            print(f"Size: {size_change}, Count: {count_change}, Average Change: {average_change}\n")

            snapshot_count += 1

            formatted_stat = f"{snapshot_count}, {size_change}, {count_change}, {average_change:.2f}"
            csv_writer.writerow([formatted_stat])
            
        # Schedule meteors using TDM algorithm
        num_time_slots = 10
        for time_slot in range(num_time_slots):
            tdm_schedule(meteors, time_slot)

        # Move and draw meteors
        for meteor, meteor_turtle in zip(meteors, meteor_turtles):
            move_meteor(meteor)
            meteor_turtle.goto(meteor['x'], meteor['y'])
            meteor_turtle.dot(0.5)  # Draw meteor as a small dot
        
        turtle.update()