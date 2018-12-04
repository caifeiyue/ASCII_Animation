from asciimatics.effects import Stars, Print, Sprite
from asciimatics.particles import RingFirework, SerpentFirework, StarFirework, \
    PalmFirework
from asciimatics.renderers import SpeechBubble, FigletText, Rainbow, StaticRenderer
from asciimatics.scene import Scene
from asciimatics.paths import Path
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
from random import randint, choice
import sys

from resources.ascii_art import love, hug_two

def move_animation(screen, ascii_obj):
    centre = (screen.width // 2, screen.height // 2 - 3)
    path = Path()
    # path.jump_to(screen.width + 16, centre[1])
    obj_len = 2
    half_length = 10
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
    # return effects
    return sprite


def demo(screen):
    scenes = []
    effects = [
        Stars(screen, screen.width),
        Print(screen,
              SpeechBubble("Press space to see it again"),
              y=screen.height - 3,
              start_frame=300)
    ]
    for _ in range(20):
        fireworks = [
            (PalmFirework, 25, 30),
            (PalmFirework, 25, 30),
            (StarFirework, 25, 35),
            (StarFirework, 25, 35),
            (StarFirework, 25, 35),
            (RingFirework, 20, 30),
            (SerpentFirework, 30, 35),
        ]
        firework, start, stop = choice(fireworks)
        effects.insert(
            1,
            firework(screen,
                     randint(0, screen.width),
                     randint(screen.height // 8, screen.height * 3 // 4),
                     randint(start, stop),
                     start_frame=randint(0, 250)))

    effects.append(Print(screen,
                         StaticRenderer(images=[hug_two]),
                         screen.height - 18,
                         speed=2,
                         start_frame=50))

    effects.append(Print(screen,
                         Rainbow(screen, FigletText("HAPPY")),
                         screen.height // 2 - 6,
                         speed=1,
                         start_frame=100))
    effects.append(Print(screen,
                         Rainbow(screen, FigletText("BIRTHDAY!")),
                         screen.height // 2 + 1,
                         speed=1,
                         start_frame=100))
    love_move = move_animation(screen, love)
    effects.append(love_move)
    scenes.append(Scene(effects, -1))
    # scenes.append(Scene(love_move, -1))
    screen.play(scenes, stop_on_resize=True)



