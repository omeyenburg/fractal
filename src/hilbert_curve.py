from fractal import Vec, Fractal
from math import *
import pygame


def init():
    hilbert_curve.array.append(Vec(0, 1))
    hilbert_curve.array.append(Vec(1, 0))
    hilbert_curve.array.append(Vec(0, -1))


def iterate():
    def rotate_right(point):
        return Vec(point.y, point.x)

    def rotate_left(point):
        return Vec(-point.y, -point.x)

    updated_array = []
    old_array = hilbert_curve.array[:]

    updated_array.extend(map(rotate_right, old_array))
    updated_array.append(Vec(0, 1))
    updated_array.extend(old_array)
    updated_array.append(Vec(1, 0))
    updated_array.extend(old_array)
    updated_array.append(Vec(0, -1))
    updated_array.extend(map(rotate_left, old_array))

    hilbert_curve.array = updated_array


def draw():
    width, height = hilbert_curve.width, hilbert_curve.height
    fractal_size = round(pow(len(hilbert_curve.array) + 1, 0.5) * 0.5)

    fractal_draw = []
    point = Vec(0, 0)
    for vec in [Vec(0, 0)] + hilbert_curve.array:
        point += vec
        fractal_draw.append((
            (point.x - fractal_size + 0.5) *
            height / 4 / fractal_size + width / 2,
            (fractal_size - point.y - 0.5) *
            height / 4 / fractal_size + height / 2
        ))

    hilbert_curve.draw_lines(fractal_draw, False)
    #pygame.draw.lines(
    #    hilbert_curve.window,
    #    (255, 255, 255),
    #    False,
    #    fractal_draw
    #)


if __name__ == "__main__":
    hilbert_curve = Fractal()
    hilbert_curve.iterations = 7
    hilbert_curve.delay = 0.5
    hilbert_curve.func_init = init
    hilbert_curve.func_iter = iterate
    hilbert_curve.func_draw = draw
    hilbert_curve.run()
