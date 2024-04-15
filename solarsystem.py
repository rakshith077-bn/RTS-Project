import turtle
import math
import time
import random
from itertools import cycle
from heapq import heappush, heappop
from celestialbody import SolarSystemBody
from body_calculations import calculate_all_body_interactions

class Planet(SolarSystemBody):
    colours = cycle(["teal", "magenta", "blue", "red", "green", "yellow"])

    def __init__(self, solar_system, mass, position=(0, 0), velocity=(0, 0), distance_to_sun=0):
        super().__init__(solar_system, mass, position, velocity)
        self.color(next(Planet.colours))
        self.orbit_trail = []

        self.eccentricity = None
        self.semi_major_axis = None
        self.orbit_period = None

        self.solar_system = solar_system

    def move(self):
        super().move()
        self.orbit_trail.append((self.xcor(), self.ycor()))
        self.orbit_trail = self.orbit_trail[-100:]


    def draw(self):
        super().draw()
        self.penup()
        if len(self.orbit_trail) > 1:
            for i in range(len(self.orbit_trail) - 1):
                start = self.orbit_trail[i]
                end = self.orbit_trail[i + 1]
                self.goto(start)
                self.pendown()
                self.goto(end)
                self.penup()

        x, y = self.position()

class SolarSystem:
    def __init__(self, width, height):
        """
        Initialize a SolarSystem object.

        Parameters:
            width (int): The width of the solar system window.
            height (int): The height of the solar system window.
        """
        self.solar_system = turtle.Screen()
        self.solar_system.tracer(0)
        self.solar_system.setup(width, height)
        self.solar_system.bgcolor("black")
        self.bodies = []


    def add_body(self, body):
        """
        Add a celestial body to the solar system.

        Parameters:
            body (SolarSystemBody): The celestial body to add to the solar system.
        """
        self.bodies.append(body)

    def remove_body(self, body):
        """
        Remove a celestial body from the solar system.

        Parameters:
            body (SolarSystemBody): The celestial body to remove from the solar system.
        """
        body.clear()
        self.bodies.remove(body)

    def update_all(self):
        """
        Update the positions of all celestial bodies in the solar system and update the screen.
        """
        for body in self.bodies:
            body.move()
            body.draw()
        self.solar_system.update()

    def calculate_all_body_interactions(self):
       
        bodies_copy = self.bodies.copy()
        for idx, first in enumerate(bodies_copy):
            for second in bodies_copy[idx + 1:]:
                self.accelerate_due_to_gravity(first, second)

    def accelerate_due_to_gravity(self, first, second):
        """
        Calculate the acceleration of two celestial bodies due to gravity and update their velocities.

        Parameters:
            first (SolarSystemBody): The first celestial body.
            second (SolarSystemBody): The second celestial body.
        """
        start_time = time.time()
        force = first.mass * second.mass / first.distance(second) ** 2
        angle = first.towards(second)
        reverse = 1
        for body in first, second:
            acceleration = force / body.mass
            acc_x = acceleration * math.cos(math.radians(angle))
            acc_y = acceleration * math.sin(math.radians(angle))
            body.velocity = (
                body.velocity[0] + (reverse * acc_x),
                body.velocity[1] + (reverse * acc_y),
            )
            reverse = -1
        end_time = time.time()
        force_calc = end_time - start_time
        print(f"Force Calc: {force_calc:.7f} s")

    def check_collision(self, first, second):
        """
        Check if two celestial bodies have collided and remove them from the solar system if they are planets.

        Parameters:
            first (SolarSystemBody): The first celestial body.
            second (SolarSystemBody): The second celestial body.
        """
        start_time = time.time()
        if isinstance(first, Planet) and isinstance(second, Planet):
            return
        if first.distance(second) < first.display_size / 2 + second.display_size / 2:
            for body in first, second:
                if isinstance(body, Planet):
                    self.remove_body(body)
        end_time = time.time()
        check_collision = end_time - start_time
        print(f"Collision Calc: {check_collision:.7f} s")


    def right_monotonic_schedule(self, tasks):
        """
        Implement the Right Monotonic Scheduling algorithm to schedule aperiodic tasks.

        Parameters:
            tasks (list): A list of CelestialBodyTask objects representing aperiodic tasks.

        Returns:
            tuple: A tuple containing task execution times, deadline miss rate, and real-time compliance rate.
        """
        current_time = time.time()
        heap = []
        for task in tasks:
            deadline = current_time + 1 / task.priority
            heappush(heap, calculate_all_body_interactions(task.body, task.priority, deadline))
        
        task_execution_times = []  # Store task execution times
        missed_deadlines = 0  # Count missed deadlines
        completed_tasks = 0  # Count completed tasks
        total_tasks = len(tasks)  # Total number of tasks

        while heap:    
            task = heappop(heap)
            if task.deadline <= current_time:
                print("Task missed deadline.")
                missed_deadlines += 1
                continue
            
            start_time = time.time()
            task.body.move()
            task.body.draw()
            end_time = time.time()
            task_execution_time = end_time - start_time
            task_execution_times.append(task_execution_time)

            priority = calculate_all_body_interactions(task.body, self.bodies)
            new_deadline = current_time + 1 / priority
            heappush(heap, calculate_all_body_interactions(task.body, priority, new_deadline))
            current_time = time.time()

            completed_tasks += 1

        real_time_compliance = (completed_tasks / total_tasks) * 100
        avg_task_execution_time = sum(task_execution_times) / len(task_execution_times)
        task_deadline_miss_rate = (missed_deadlines / total_tasks) * 100

        return avg_task_execution_time, task_deadline_miss_rate, real_time_compliance
