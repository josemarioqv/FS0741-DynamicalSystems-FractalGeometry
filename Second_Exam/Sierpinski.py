import numpy as np
import random
import pyglet


class Triangle():

    def __init__(self):
        self.W = np.array([[[0.5, 0.], [0., 0.5]],
                          [[0.5, 0.], [0., 0.5]],
                          [[0.5, 0.], [0., 0.5]]])
        self.B = np.array([[1., 1.],
                          [1., 50.],
                          [50., 50.]])
        self.X = np.array([2, 2])

    def update(self):
        i = random.choices(population=[0, 1, 2],
                           weights=[0.33, 0.33, 0.34])[0]
        self.X = np.dot(self.W[i], self.X) + self.B[i]

    def draw(self):
        point = self.X*3
        point = tuple(point.astype(int))
        print(point)
        pyglet.graphics.draw(1, pyglet.gl.GL_POINTS, ('v2i', point),
                             ('c3B', (200, 200, 200)))


class Window(pyglet.window.Window):

    def __init__(self):
        # pyglet window initialization
        super().__init__()
        self.set_size(400, 400)
        pyglet.clock.schedule_interval(self.update, 0.00001)
        # initialization
        self.triangle = Triangle()

    def on_draw(self):
        self.triangle.draw()

    def update(self, dt):
        self.triangle.update()
        pass


if __name__ == '__main__':
    window = Window()
    pyglet.app.run()
