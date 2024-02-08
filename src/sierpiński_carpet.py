from fractal import Vec, Square, Fractal
from math import *
import pygame


def init():
    width, height = pygame.display.get_surface().get_size()

    square = Square(width / 2, height / 2, height / 4)
    carpet.array = [set(), {square}]


def iterate():
    parents = set(carpet.array[0])
    children = set()

    for child in carpet.array[1]:
        for x_offset in (-1, 0, 1):
            for y_offset in (-1, 0, 1):
                if not (x_offset or y_offset):
                    continue
                square = Square(child.x + (x_offset) * child.a,
                                child.y + (y_offset) * child.a, child.a / 3)
                children.add(square)
        parents.add(child)

    carpet.array = [parents, children]


def draw():
    for square in carpet.array[0].union(carpet.array[1]):
        pygame.draw.rect(carpet.window, (255, 255, 255), (*square,))


if __name__ == "__main__":
    carpet = Fractal()
    carpet.iterations = 5
    carpet.delay = 0.5
    carpet.func_init = init
    carpet.func_iter = iterate
    carpet.func_draw = draw
    carpet.run()
