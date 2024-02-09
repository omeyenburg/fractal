from fractal import Vec, Fractal
from math import *
import pygame


def draw():
    length = tree.height / 5
    nodes = [(tree.width / 2, tree.height - length, -pi / 2)]
    # angle = (pi / 5) / (max(1, pygame.mouse.get_pos()[1]))
    angle = pi / 6
    pygame.draw.line(tree.window, (255, 255, 255),
                     nodes[0][:2], (nodes[0][0], nodes[0][1] + length))

    for _ in range(tree.iterations):
        length *= 0.8
        angle *= 0.9
        parents = nodes[:]
        nodes = []

        for parent in parents:
            left = (
                cos(parent[2] - angle) * length + parent[0],
                sin(parent[2] - angle) * length + parent[1],
                parent[2] - angle
            )
            nodes.append(left)
            pygame.draw.line(tree.window, (255, 255, 255),
                             parent[:2], left[:2])

            right = (
                cos(parent[2] + angle) * length + parent[0],
                sin(parent[2] + angle) * length + parent[1],
                parent[2] + angle
            )
            nodes.append(right)
            pygame.draw.line(tree.window, (255, 255, 255),
                             parent[:2], right[:2])


if __name__ == "__main__":
    tree = Fractal("Fractal Tree")
    tree.iterations = 11
    tree.delay = 0.5
    tree.func_init = False
    tree.func_iter = False
    tree.func_draw = draw
    tree.run()
