import turtle
import math

class SolarSystemBody(turtle.Turtle):
    """
    Class representing a celestial body in the solar system.
    """

    min_display_size = 20
    display_log_base = 1.1

    def __init__(self, solar_system, mass, position=(0, 0), velocity=(0, 0)):
        """
        Initialize a SolarSystemBody object.
        
        Parameters:
            solar_system (SolarSystem): The solar system to which the body belongs.
            mass (float): The mass of the celestial body.
            position (tuple): The initial position of the body (default is (0, 0)).
            velocity (tuple): The initial velocity of the body (default is (0, 0)).
        """
        super().__init__()
        self.mass = mass
        self.setposition(position)
        self.velocity = velocity
        self.display_size = max(math.log(self.mass, self.display_log_base), self.min_display_size)
        self.penup()
        self.hideturtle()
        solar_system.add_body(self)

    def draw(self):
        """
        Draw the celestial body.
        """
        self.clear()
        self.dot(self.display_size)

    def move(self):
        """
        Move the celestial body according to its velocity.
        """
        self.setx(self.xcor() + self.velocity[0])
        self.sety(self.ycor() + self.velocity[1])


class Sun1(SolarSystemBody):
    """
    Class representing the first sun in the solar system.
    """

    def __init__(self, solar_system, mass, position=(0, 0), velocity=(0, 0)):
        """
        Initialize a Sun1 object.
        
        Parameters:
            solar_system (SolarSystem): The solar system to which the sun belongs.
            mass (float): The mass of the sun.
            position (tuple): The initial position of the sun (default is (0, 0)).
            velocity (tuple): The initial velocity of the sun (default is (0, 0)).
        """
        super().__init__(solar_system, mass, position, velocity)
        self.color("yellow")


class Sun2(SolarSystemBody):
    def __init__(self, solar_system, mass, position=(0, 0), velocity=(0, 0)):
        """
        Initialize a Sun2 object.
        
        Parameters:
            solar_system (SolarSystem): The solar system to which the sun belongs.
            mass (float): The mass of the sun.
            position (tuple): The initial position of the sun (default is (0, 0)).
            velocity (tuple): The initial velocity of the sun (default is (0, 0)).
        """
        super().__init__(solar_system, mass, position, velocity)
        self.color("red")
