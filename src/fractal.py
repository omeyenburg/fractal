from threading import Thread
import pygame
import time


class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)

    def __truediv__(self, scalar):
        return Vec(self.x / scalar, self.y / scalar)

    def __mul__(self, scalar):
        return Vec(self.x * scalar, self.y * scalar)

    def __repr__(self):
        return f"Vec({round(self.x, 3)}, {round(self.y, 3)})"


class Square:
    def __init__(self, x, y, a):
        self.x = x
        self.y = y
        self.a = a

    def __iter__(self):
        return (i for i in (self.x - self.a / 2, self.y - self.a / 2, self.a, self.a))

    def __repr__(self):
        return f"Square({round(self.x, 3)}, {round(self.y, 3)}, {round(self.a, 3)})"


class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __iter__(self):
        return (i for i in (self.r, self.g, self.b))

    def __add__(self, other):
        return Color(self.r + other.r, self.g + other.g, self.b + other.b)

    def __mul__(self, scalar):
        return Color(self.r * scalar, self.g * scalar, self.b * scalar)


def gradient(f):
    if f < 1/3:
        f = f * 3
        return Color(255, 0, 0) * f + Color(0, 255, 0) * (1 - f)
    elif f < 2/3:
        f = (f - 1/3) * 3
        return Color(0, 0, 255) * f + Color(255, 0, 0) * (1 - f)
    else:
        f = (f - 2/3) * 3
        return Color(0, 255, 0) * f + Color(0, 0, 255) * (1 - f)


class Fractal:
    def __init__(self):
        pygame.init()
        info = pygame.display.Info()

        self.width = int(info.current_w / 3 * 2)
        self.height = int(info.current_h / 5 * 3)
        self.window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

        self.array = []
        self.iterations = 0
        self.delay = 0
        self.func_init = None
        self.func_iter = None
        self.func_draw = None

    def iterate(self):
        for i in range(self.iterations):
            time.sleep(self.delay)
            if self.func_iter.__code__.co_argcount:
                self.func_iter(i)
            else:
                self.func_iter()

    def draw_lines(self, points, connected):
        if connected:
            points.append(points[0])

        for i in range(len(points) - 1):
            f = i / len(points)
            pygame.draw.line(self.window, tuple(gradient(f)),
                             points[i], points[i + 1])

    def run(self):
        if self.func_init is None:
            raise RuntimeError("Fractal.func_init was not set.")
        if self.func_iter is None:
            raise RuntimeError("Fractal.func_iter was not set.")
        if self.func_draw is None:
            raise RuntimeError("Fractal.func_draw was not set.")

        # Init
        self.func_init()
        thread = Thread(target=self.iterate, daemon=True)
        thread.start()

        # Render
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit(0)

            self.window.fill((0, 0, 0))
            self.func_draw()

            pygame.display.flip()
            self.clock.tick(60)
