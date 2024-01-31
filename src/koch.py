import fractal
import pygame
import math


def init(array):
    array.extend([fractal.Vec(0, 0), fractal.Vec(1, 0)])

def iterate(array):
    updated_array = []

    for j in range(len(array) - 1):
        start = array[j]
        end = array[j + 1]
        edge_length = math.dist(start, end) / 3
        angle = math.atan2(-start.y + end.y, -start.x + end.x)
        adjusted_angle = angle - math.pi / 3

        center0 = start + fractal.Vec(math.cos(angle), math.sin(angle)) * edge_length
        center1 = center0 + fractal.Vec(math.cos(adjusted_angle), math.sin(adjusted_angle)) * edge_length
        center2 = (center0 + end) * 0.5
        updated_array.extend([start, center0, center1, center2, end])

    array[:] = updated_array[:]

def draw(array):
    window = pygame.display.get_surface()
    width, height = window.get_size()

    fractal_draw = []
    for vec in array:
        fractal_draw.append((vec.x * width, vec.y * width + height / 2))

    pygame.draw.lines(window, (255, 255, 255), False, fractal_draw)


if __name__ == "__main__":
    koch_curve = fractal.Fractal()
    koch_curve.iterations = 5
    koch_curve.func_init = init
    koch_curve.func_iter = iterate
    koch_curve.func_draw = draw
    koch_curve.run()
