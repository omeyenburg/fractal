from fractal import Fractal, Color
from math import *


def iterate(pixel):
    floats = []

    for delta_x in (-1/3, 0, 1/3):
        for delta_y in (-1/3, 0, 1/3):
            x = (pixel[0] - mandelbrot_set.width / 1.5 +
                 delta_x) / mandelbrot_set.height * 2.5
            y = (pixel[1] - mandelbrot_set.height / 2 +
                 delta_y) / mandelbrot_set.height * 2.5

            z = 0
            for i in range(mandelbrot_set.iterations):
                z = z ** 2 + complex(x, y)
                distance = sqrt(z.real ** 2 + z.imag ** 2)
                if distance > 1_000_000:
                    floats.append(i / mandelbrot_set.iterations *
                                  (1 - log(distance) * 0.01))
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
    g = 20 + 230 * (f-0.1) ** 5
    b = 80 + 200 * f ** 5

    mandelbrot_set.window.set_at(
        pixel,
        tuple(Color(r, g, b) * (len(floats) / 9) + Color(0, 0, 0) * (1 - len(floats) / 9))
    )


if __name__ == "__main__":
    mandelbrot_set = Fractal(
        "Mandelbrot Set",
        iterations=50,
        pixel=True,
        threads=16
    )
    mandelbrot_set.func_init = False
    mandelbrot_set.func_iter = iterate
    mandelbrot_set.func_draw = False
    mandelbrot_set.run()
