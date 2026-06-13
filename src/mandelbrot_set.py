from fractal import Fractal, Color
from math import *
import numpy as np


def iterate(pixel):
    floats = []

    for delta_x in (-1 / 3, 0, 1 / 3):
        for delta_y in (-1 / 3, 0, 1 / 3):
            x = (
                (pixel[0] - mandelbrot_set.width / 1.5 + delta_x)
                / mandelbrot_set.height
                * 2.5
            )
            y = (
                (pixel[1] - mandelbrot_set.height / 2 + delta_y)
                / mandelbrot_set.height
                * 2.5
            )

            z = 0
            for i in range(mandelbrot_set.iterations):
                z = z**2 + complex(x, y)
                distance = sqrt(z.real**2 + z.imag**2)
                if distance > 1_000_000:
                    floats.append(
                        i / mandelbrot_set.iterations * (1 - log(distance) * 0.01)
                    )
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

    return Color(r, g, b) * (len(floats) / 9) + Color(0, 0, 0) * (1 - len(floats) / 9)


def draw(pixels):
    height, width = pixels.shape[:2]

    iterations = mandelbrot_set.iterations
    threshold = 1e6

    x_min, x_max = -2.5, 1.0
    y_min, y_max = -3.0, 2.0

    center_x = (x_min + x_max) / 2
    center_y = (y_min + y_max) / 2

    x = np.linspace(x_min, x_max, width, dtype=np.float32)
    y = np.linspace(y_max, y_min, height, dtype=np.float32)  # note max → min

    X, Y = np.meshgrid(x, y)
    C = 1j * (X - center_x) - (Y - center_y)

    Z = np.zeros_like(C, dtype=np.complex64)
    strength = np.zeros_like(C, dtype=np.float32)
    mask = np.ones_like(C, dtype=bool)

    for i in range(iterations):
        Z[mask] = Z[mask] ** 2 + C[mask]

        distance = np.abs(Z)
        escaped = mask & (distance > threshold)
        mask[escaped] = False

        strength[escaped] = i / iterations * (1 - np.log(distance[escaped]) * 0.01)

    mask_escape = strength > 0
    pixels[:, :, 0][mask_escape] = strength[mask_escape] * 255
    pixels[:, :, 1][mask_escape] = ((strength[mask_escape] - 0.1) ** 5) * 230 + 20
    pixels[:, :, 2][mask_escape] = (strength[mask_escape] ** 5) * 200 + 80


if __name__ == "__main__":
    # Draw in one go
    mandelbrot_set = Fractal("Mandelbrot Set", iterations=50)
    mandelbrot_set.func_init_draw = draw

    # Draw incrementally across multiple threads
    # mandelbrot_set = Fractal("Mandelbrot Set", iterations=50, pixel=True, threads=8)
    # mandelbrot_set.func_iter = iterate

    mandelbrot_set.run()
