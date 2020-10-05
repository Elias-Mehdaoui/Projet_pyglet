import pyglet

window = pyglet.window.Window(960,540)
batch = pyglet.graphics.Batch()

class Rectangle:
    
    def __init__(self, x_pos, y_pos, x, y, r, g, b):
        self.x = x
        self.y = y
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.r = r
        self.g = g
        self.b = b
        self.rectangle = pyglet.shapes.Rectangle(x_pos, y_pos, x, y, color=(r, g, b), batch=batch)




rectangle1 = Rectangle(50, 0, 275, 50, 255, 22, 20)
rectangle2 = Rectangle(75, 50, 225, 50, 18, 59, 132)
rectangle3 = Rectangle(87.5, 75, 175, 50, 245, 241, 11)

    

@window.event
def on_draw():
    window.clear()
    batch.draw()
    
pyglet.app.run()