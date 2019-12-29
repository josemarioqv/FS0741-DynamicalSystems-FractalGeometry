import numpy as np
import random
import pyglet


class Tree():

    def __init__(self):
        self.W = np.array([[[0., 0.], [0., 0.5]],
                          [[0.42, -0.42], [0.42, 0.42]],
                          [[0.42, 0.42], [-0.42, 0.42]]])
        self.B = np.array([[0., 0.],
                          [0., 0.2],
                          [0., 0.2]])
        self.X = np.array([2, 2])

    def update(self):
        i = random.choices(population=[0, 1, 2],
                           weights=[0.05, 0.4, 0.4])[0]
        self.X = np.dot(self.W[i], self.X) + self.B[i]

    def draw(self):
        point = self.X*800
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
        self.tree = Tree()

    def on_draw(self):
        self.tree.draw()

    def update(self, dt):
        self.tree.update()
        pass


if __name__ == '__main__':
    window = Window()
    pyglet.app.run()
