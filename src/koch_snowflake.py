from fractal import Vec, Fractal
from math import *


def init():
    center = Vec(koch_curve.width / 2, koch_curve.height / 2)
    length = koch_curve.height / 3

    for i in range(3):
        angle = pi / 1.5 * i + pi / 6
        coord = center + Vec(
            cos(angle) * length,
            sin(angle) * length,
        )
        koch_curve.array.append(coord)


def iterate():
    updated_array = []

    for j in range(-1, len(koch_curve.array) - 1):
        start = koch_curve.array[j]
        end = koch_curve.array[j + 1]
        edge_length = dist(start, end) / 3
        angle = atan2(-start.y + end.y, -start.x + end.x)
        adjusted_angle = angle - pi / 3

        center0 = start + Vec(
            cos(angle),
            sin(angle)
        ) * edge_length
        center0 = (start * (2 / 3) + end * (1 / 3))
        center1 = center0 + Vec(
            cos(adjusted_angle),
            sin(adjusted_angle)
        ) * edge_length
        center2 = (start * (1 / 3) + end * (2 / 3))
        updated_array.extend([start, center0, center1, center2, end])

    koch_curve.array = updated_array


def draw():
    fractal_draw = []
    for vec in koch_curve.array:
        fractal_draw.append((vec.x, vec.y))

    koch_curve.draw_lines(fractal_draw, True)


if __name__ == "__main__":
    koch_curve = Fractal(
        "Koch Snowflake",
        iterations=6,
        delay=0.5,
        colour=True
    )
    koch_curve.func_init = init
    koch_curve.func_iter = iterate
    koch_curve.func_draw = draw
    koch_curve.run()
