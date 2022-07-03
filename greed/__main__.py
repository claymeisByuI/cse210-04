import os
import random

from game.casting.actor import Actor
from game.casting.rock import Rock
from game.casting.gem import Gem
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "GREED"
WHITE = Color(255, 255, 255)
DEFAULT_ROCK = 20
DEFAULT_GEMS = 20


def main():
    
    # create the cast
    cast = Cast(FONT_SIZE, COLS, ROWS, CELL_SIZE)
    
    # create the score
    score = Actor()
    score.set_text("Score:0")
    score.set_font_size(FONT_SIZE)
    score.set_color(WHITE)
    score.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("score", score)
    
    # create the player
    x = int(COLS / 2)
    y = int(ROWS-2)
    position = Point(x, y)
    position = position.scale(CELL_SIZE)

    player = Actor()
    player.set_text("#")
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)
    player.set_position(position)
    cast.add_actor("player", player)
    

    for n in range(DEFAULT_ROCK):
        rock = cast.new_actor(Rock())
        cast.add_actor("rock", rock)
    
    for n in range(DEFAULT_GEMS):
        gem = cast.new_actor( Gem())
        cast.add_actor("gem", gem)

    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, ROWS, COLS, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()