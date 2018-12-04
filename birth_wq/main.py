#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
import pdb
from random import randint
from asciimatics.screen import Screen
from asciimatics.effects import Cycle, Stars, Print, Sprite
from asciimatics.renderers import FigletText, StaticRenderer, BarChart
from asciimatics.scene import Scene
from asciimatics.paths import Path
from asciimatics.exceptions import ResizeScreenError

from fireworks import demo as firework
from resources.ascii_art import china, name, love


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


def print_ascii(screen, ascii_obj):
    effects = [
        Print(screen,
              # FigletText("ASCIIMATICS", font='big'),
              StaticRenderer(images=[ascii_obj]),
              int(screen.height / 2 - 16),
              start_frame=1)
    ]

    effects.append(Print(screen,
                         StaticRenderer(images=[name]),
                         int(screen.height / 2 + 7),
                         int(screen.width / 2 + 14),
                         start_frame=30))
    """effects.append(Print(screen,
                         StaticRenderer(images=[arrow]),
                         int(screen.height / 2 + 7),
                         int(screen.width / 2 + 13),
                         start_frame=40))
    """
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
                         StaticRenderer(images=[name]),
                         int(screen.height / 2 + 12),
                         int(screen.width / 2 + 14),
                         start_frame=55))
    return effects
    # screen.play([Scene(effects, 0)])


def move_animation(screen, ascii_obj):
    centre = (screen.width // 2, screen.height // 2)
    path = Path()
    # path.jump_to(screen.width + 16, centre[1])
    obj_len = 2
    half_length = 8
    for i in range(half_length):
        path.jump_to(centre[0]-i*2, centre[1]-i)
        path.jump_to(centre[0]+i*2, centre[1]-i)
    for i in range(half_length):
        path.jump_to(centre[0]-(half_length-1)*2-1-i*2, centre[1]-(half_length-1)+i)
        path.jump_to(centre[0]+(half_length-1)*2+1+i*2, centre[1]-(half_length-1)+i)
    for i in range(1, 2*half_length-1):
        path.jump_to(centre[0]-(half_length-1)*2*2+i*2, centre[1]+i)
        path.jump_to(centre[0]+(half_length-1)*2*2-i*2, centre[1]+i)

    # path.move_straight_to(screen.width+obj_length, centre[1], (screen.width + obj_length) // 2)
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
                        "default": StaticRenderer(images=[ascii_obj])
                    },
            path=path,
            colour=255,
            clear=False)
    effects = [sprite]
    return effects
    # screen.play([Scene(effects, 0)])


def my_future_come(screen):
    sences = []
    china_geo = print_ascii(screen, china)
    train_move = move_animation(screen, love)
    # sences.append(Scene(china_geo, 80))
    sences.append(Scene(train_move, 300))
    screen.play(sences, stop_on_resize=True, repeat=False)


# wrapper: call the function
# Screen: the args of wrapper func
while True:
    try:
        # Screen.wrapper(my_future_come)
        Screen.wrapper(firework)
        sys.exit(0)
    except ResizeScreenError:
        pass
