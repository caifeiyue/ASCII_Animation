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

from resources.ascii_art import love, hug_two, bike_two, tree

def move_straight_animation(screen, ascii_obj, height, speed=1, color=7):
    obj_len = 5
    path = Path()
    path.jump_to(-obj_len, height)
    path.move_straight_to(screen.width, height, (screen.width + obj_len) // speed)
    sprite = Sprite(screen, renderer_dict={"default": StaticRenderer(images=[ascii_obj])},
                    path=path, colour=color)
    # effects = [sprite]
    # return effects
    return sprite


def main(screen):
    scenes = []
    effects = [
        Stars(screen, screen.width),
        Print(screen,
              SpeechBubble("Press space to see it again"),
              y=screen.height - 3,
              start_frame=300)
    ]
    effects.append(Print(screen,
                        StaticRenderer(images=tree),
                        x=screen.width - 15,
                        y=screen.height - 15,
                        colour=Screen.COLOUR_GREEN))
    effects.append(Print(screen,
                        StaticRenderer(images=tree),
                        x=1,
                        y=screen.height - 15,
                        colour=Screen.COLOUR_GREEN))
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
        effects.insert(1,
                       firework(screen, randint(0, screen.width),
                                randint(screen.height // 8, screen.height * 3 // 4),
                                randint(start, stop),
                                start_frame=randint(0, 250)))

    effects.append(Print(screen,
                         StaticRenderer(images=[hug_two]),
                         screen.height-18,
                         speed=2,
                         start_frame=20))

    """effects.append(Print(screen,
                         Rainbow(screen, FigletText("HAPPY")),
                         screen.height // 2 - 16,
                         speed=1,
                         start_frame=100))

    effects.append(Print(screen,
                         Rainbow(screen, FigletText("BIRTHDAY!")),
                         screen.height // 2 - 10,
                         speed=1,
                         start_frame=100))
    """
    height = 20
    move_animation = move_straight_animation(screen, bike_two, height)
    effects.append(move_animation)

    # whole ascii animation
    scenes.append(Scene(effects, -1))
    screen.play(scenes, stop_on_resize=True)


while True:
    try:
        # Screen.wrapper(my_future_come)
        Screen.wrapper(main)
        sys.exit(0)
    except ResizeScreenError:
        pass

