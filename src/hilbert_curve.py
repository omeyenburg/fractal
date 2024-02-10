from fractal import Vec, Fractal
from math import *


def init():
    hilbert_curve.array = [
        Vec(0, 1),
        Vec(1, 0),
        Vec(0, -1)
    ]


def iterate():
    def rotate_right(point):
        return Vec(point.y, point.x)

    def rotate_left(point):
        return Vec(-point.y, -point.x)

    hilbert_curve.array = [
        *map(rotate_right, hilbert_curve.array),
        Vec(0, 1),
        *hilbert_curve.array,
        Vec(1, 0),
        *hilbert_curve.array,
        Vec(0, -1),
        *map(rotate_left, hilbert_curve.array)
    ]


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


if __name__ == "__main__":
    hilbert_curve = Fractal(
        "Hilbert Curve",
        iterations=6,
        delay=0.5,
        colour=True
    )
    hilbert_curve.func_init = init
    hilbert_curve.func_iter = iterate
    hilbert_curve.func_draw = draw
    hilbert_curve.run()
