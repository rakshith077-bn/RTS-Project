import tracemalloc 
import csv 
from solarsystem import Planet, SolarSystem  
from celestialbody import Sun1, Sun2 

solar_system = SolarSystem(width=1400, height=900) 
solar_system_instance = SolarSystem(width=1400, height=900)  


suns = (
    Sun1(solar_system, mass=10_000, position=(-200, 0), velocity=(0, 3.5)),
    Sun2(solar_system, mass=10_000, position=(200, 0), velocity=(0, -3.5)),
)

planets = (
    Planet(solar_system, mass=20, position=(50, 0), velocity=(0, 11)), 
    Planet(solar_system, mass=3, position=(-350, 0), velocity=(0, -10)), 
    Planet(solar_system, mass=1, position=(0, 200), velocity=(-2, -7)), 
)

tracemalloc.start()
old_limit = tracemalloc.get_traceback_limit()

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

        print(" Top Stats ")
        for stat in top_stats[:5]:
            size_change = stat.size
            count_change = stat.count
            average_change = stat.size / stat.count if stat.count != 0 else 0

            print(f"Size: {size_change}, Count: {count_change}, Average Change: {average_change}\n")

            snapshot_count += 1

            formatted_stat = f"{snapshot_count}, {size_change}, {count_change}, {average_change:.2f}"
            csv_writer.writerow([formatted_stat])
