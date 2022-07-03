import random
from game.casting.actor import Actor


from game.shared.color import Color
from game.shared.point import Point


class Gem(Actor):
    """A rock that is in the game. 
    
    The responsibility of Actor is to keep track of its appearance, position and velocity in 2d 
    space.

    Attributes:
        Everything from Actor.
    """

    def __init__(self): #, cols, rows, cell_size, font_size):
        """Constructs a new Actor."""
        self.set_text("*")
        yspeed = random.randint(1, 2)
        self.set_velocity(Point(0,yspeed))
