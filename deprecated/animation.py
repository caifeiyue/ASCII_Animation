from random import randint
from asciimatics.screen import Screen
from asciimatics.effects import Cycle, Stars, Print
from asciimatics.renderers import FigletText, StaticRenderer
from asciimatics.scene import Scene

bike = """
     ,--.      <__)
     `- |________7
        |`.      |\\
     .--|. \     |.\--.
    /   j \ `.7__j__\  \\
   |   o   | (o)____O)  |
    \     /   J  \     /
     `---'        `---'
"""




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


def bike_show(screen):
    effects = [
        Print(screen,
              # FigletText("ASCIIMATICS", font='big'),
              StaticRenderer(images=[bike]),
              int(screen.height / 2 - 8))
        # Stars(screen, 200)
    ]
    screen.play([Scene(effects, 500)])


Screen.wrapper(bike_show)
