#!/usr/bin/python3
# -*- coding: utf-8 -*-


from random import randint
from asciimatics.screen import Screen
from asciimatics.effects import Cycle, Stars, Print, Sprite
from asciimatics.renderers import FigletText, StaticRenderer, BarChart
from asciimatics.scene import Scene
from asciimatics.paths import Path

from fireworks import demo as firework
from ascii_lib.ascii_art import bike_series


def demo1(screen):
    while True:
        screen.print_at('Hello world!', randint(0, screen.width),
                        randint(0, screen.height), colour=randint(0, screen.colours - 1),
                        bg=randint(0, screen.colours - 1))
        ev = screen.get_key()
        if ev in (ord('Q'), ord('q')):
            return
        screen.refresh()


def demo2(screen):
    effects = [
        Cycle(screen,
              FigletText("ASCIIMATICS", font='big'),
              int(screen.height / 2 - 8)),
        Cycle(screen,
              FigletText("ROCKS!", font='big'),
              int(screen.height / 2 + 3)),
        Stars(screen, 200)
    ]
    screen.play([Scene(effects, 500)])


def bike(screen):
    centre = (screen.width // 2, screen.height // 2)
    path = Path()
    path.jump_to(screen.width + 16, centre[1])
    path.move_straight_to(-16, centre[1], (screen.width + 16) // 1)
    """effects = [
        Print(screen,
              # FigletText("ASCIIMATICS", font='big'),
              StaticRenderer(images=[bike_ascii]),
              int(screen.height / 2 - 8))
        # Stars(screen, 200)
    ]"""
    sprite = Sprite(
            screen,
            renderer_dict={
                        "default": StaticRenderer(images=[bike_series])
                    },
            path=path)
    effects = [sprite]
    screen.play([Scene(effects, 0)])





# wrapper: call the function
# Screen: the args of wrapper func
Screen.wrapper(firework)
