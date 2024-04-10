# simplesolarsystem.py
from solarsystem import SolarSystem, Sun1, Planet  
from celestialbody import CelestialBodyTask 
from utilitties import calculate_priority
from visualization import plot_metrics
import time
import tracemalloc
import csv

tracemalloc.start()

solar_system = SolarSystem(width=1400, height=900)

sun = Sun1(solar_system, mass=40_000) # Can Increase the speed

planets = (
    Planet(
        solar_system,
        mass=1,
        position=(-350, 0),
        velocity=(0, 5),
    ),
    Planet(
        solar_system,
        mass=2,
        position=(-270, 0),
        velocity=(0, 7),
    ),
)

current_time = time.time()  # Define the current time

tasks = [CelestialBodyTask(planet, 1 / planet.mass, current_time) for planet in planets]

task_execution_times = []  # List to store task execution times
task_deadline_miss_rate = []  # List to store task deadline miss rates
real_time_compliance = []

for _ in range(1000):  # Change NUM_ITERATIONS to the desired number of iterations
    snapshot1 = tracemalloc.take_snapshot()
    top_stats = snapshot1.statistics('lineno')

    print("[ Top 10 ]")
    for stat in top_stats[:10]:
        print(f"{stat}\n")

    solar_system.calculate_all_body_interactions()
    solar_system.update_all()

    execution_times, deadline_miss_rates, compliance_rates = solar_system.right_monotonic_schedule(tasks)

    # Append metrics to lists
    task_execution_times.extend(execution_times)
    task_deadline_miss_rate.append(deadline_miss_rates)
    real_time_compliance.append(compliance_rates)

# Visualize the collected metrics
plot_metrics(task_execution_times, task_deadline_miss_rate, real_time_compliance)

# Write metrics to CSV file
csv_filename = 'metrics.csv'  # Set the filename
try:
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Task Execution Time', 'Deadline Miss Rate', 'Real-time Compliance'])
        for execution_time, deadline_rate, compliance_rate in zip(task_execution_times, task_deadline_miss_rate, real_time_compliance):
            writer.writerow([execution_time, deadline_rate, compliance_rate])
    print(f"Metrics successfully written to {csv_filename}")
except Exception as e:
    print(f"Error writing metrics to {csv_filename}: {e}")
