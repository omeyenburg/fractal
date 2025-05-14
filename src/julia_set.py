from fractal import Fractal, Color
from math import *


def iterate(pixel):
    floats = []

    # Nice looking parameters:
    c = complex(-0.8, 0.2)
    # c = complex(0, 1)
    # c = 0

    for delta_x in (-1 / 3, 0, 1 / 3):
        for delta_y in (-1 / 3, 0, 1 / 3):
            x = (pixel[0] - julia_set.width / 2 + delta_x) / julia_set.height * 2.5
            y = (pixel[1] - julia_set.height / 2 + delta_y) / julia_set.height * 2.5

            z = complex(x, y)
            for i in range(julia_set.iterations):
                z = z**2 + c
                distance = sqrt(z.real**2 + z.imag**2)
                if distance > 1_000_000:
                    floats.append(i / julia_set.iterations * (1 - log(distance) * 0.01))
                    break
            else:
                floats.append(-1)

    inside = floats.count(-1)
    if inside == 9:
        return

    while -1 in floats:
        floats.remove(-1)
    f = sum(floats) / len(floats)

    r = 255 * f
    g = 20 + 230 * (f - 0.1) ** 5
    b = 80 + 200 * f**5

    julia_set.window.set_at(
        (pixel[0], julia_set.height - pixel[1]),
        tuple(
            Color(r, g, b) * (len(floats) / 9) + Color(0, 0, 0) * (1 - len(floats) / 9)
        ),
    )


if __name__ == "__main__":
    julia_set = Fractal("Julia Set", iterations=50, pixel=True, threads=16)
    julia_set.func_init = False
    julia_set.func_iter = iterate
    julia_set.func_draw = False
    julia_set.run()
