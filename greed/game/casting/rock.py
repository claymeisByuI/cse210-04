import random
from game.casting.actor import Actor

from game.shared.color import Color
from game.shared.point import Point


class Rock(Actor):
    """A rock that is in the game. 
    
    The responsibility of Actor is to keep track of its appearance, position and velocity in 2d 
    space.

    Attributes:
        Everything from Actor.

    """

    def __init__(self):
        """Constructs a new Actor."""
        self.set_text("O")
        yspeed = random.randint(1, 5)
        self.set_velocity(Point(0,yspeed))
