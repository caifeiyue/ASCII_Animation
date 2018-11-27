#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from random import randint
from asciimatics.screen import Screen
from asciimatics.effects import Cycle, Stars, Print, Sprite
from asciimatics.renderers import FigletText, StaticRenderer, BarChart
from asciimatics.scene import Scene
from asciimatics.paths import Path
from asciimatics.exceptions import ResizeScreenError

from resources.ascii_art import china, train, arrow, CS, GZ


def print_ascii(screen, ascii_obj):
    effects = [
        Print(screen,
              # FigletText("ASCIIMATICS", font='big'),
              StaticRenderer(images=[ascii_obj]),
              int(screen.height / 2 - 16),
              start_frame=1)
    ]

    effects.append(Print(screen,
                         StaticRenderer(images=[CS]),
                         int(screen.height / 2 + 7),
                         int(screen.width / 2 + 14),
                         start_frame=30))
    effects.append(Print(screen,
                         StaticRenderer(images=["/"]),
                         int(screen.height / 2 + 8),
                         int(screen.width / 2 + 14),
                         start_frame=35))
    effects.append(Print(screen,
                         StaticRenderer(images=["\\"]),
                         int(screen.height / 2 + 9),
                         int(screen.width / 2 + 14),
                         start_frame=40))
    effects.append(Print(screen,
                         StaticRenderer(images=["/"]),
                         int(screen.height / 2 + 10),
                         int(screen.width / 2 + 14),
                         start_frame=45))
    effects.append(Print(screen,
                         StaticRenderer(images=["\\"]),
                         int(screen.height / 2 + 11),
                         int(screen.width / 2 + 14),
                         start_frame=50))
    effects.append(Print(screen,
                         StaticRenderer(images=[GZ]),
                         int(screen.height / 2 + 12),
                         int(screen.width / 2 + 14),
                         start_frame=55))
    return effects
    # screen.play([Scene(effects, 0)])


def move_animation(screen, ascii_obj):
    centre = (screen.width // 2, screen.height // 2)
    path = Path()
    # path.jump_to(screen.width + 16, centre[1])
    obj_length = 64
    path.jump_to(-obj_length, centre[1])
    path.move_straight_to(screen.width+obj_length, centre[1], (screen.width + obj_length) // 5)
    sprite = Sprite(
            screen,
            renderer_dict={
                        "default": StaticRenderer(images=[ascii_obj])
                    },
            path=path)
    effects = [sprite]
    return effects
    # screen.play([Scene(effects, 0)])


def my_future_come(screen):
    sences = []
    china_geo = print_ascii(screen, china)
    train_move = move_animation(screen, train)
    sences.append(Scene(china_geo, 80))
    sences.append(Scene(train_move, 90))
    # effects.append(train_move)
    screen.play(sences, stop_on_resize=True, repeat=False)


# wrapper: call the function
# Screen: the args of wrapper func
while True:
    try:
        Screen.wrapper(my_future_come)
        sys.exit(0)
    except ResizeScreenError:
        pass
