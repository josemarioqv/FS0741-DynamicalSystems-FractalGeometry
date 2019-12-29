import numpy as np
import random
import pyglet


class Fern():

    def __init__(self):
        self.W = np.array([[[0., 0.], [0., 0.4]],
                          [[0.85, 0.04], [-0.04, 0.85]],
                          [[0.2, -0.26], [0.23, 0.22]],
                          [[-0.15, 0.28], [0.25, 0.24]]])
        self.B = np.array([[0., 0.01],
                          [1.6, 0.85],
                          [1.6, 0.07],
                          [0.44, 0.07]])
        self.X = np.array([0.5, 0.6])

    def update(self):
        i = random.choices(population=[0, 1, 2, 3],
                           weights=[0.01, 0.85, 0.07, 0.07])[0]
        self.X = np.dot(self.W[i], self.X) + self.B[i]

    def draw(self):
        point = self.X*35
        point = tuple(point.astype(int))
        print(point)
        pyglet.graphics.draw(1, pyglet.gl.GL_POINTS, ('v2i', point),
                             ('c3B', (40, 200, 40)))


class Window(pyglet.window.Window):

    def __init__(self):
        # pyglet window initialization
        super().__init__()
        self.set_size(400, 400)
        pyglet.clock.schedule_interval(self.update, 0.001)
        # initialization
        self.fern = Fern()

    def on_draw(self):
        self.fern.draw()

    def update(self, dt):
        self.fern.update()
        pass


if __name__ == '__main__':
    window = Window()
    pyglet.app.run()
