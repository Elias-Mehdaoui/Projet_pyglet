import pyglet
from pyglet import shapes

window = pyglet.window.Window(960,540)
pyglet.gl.glClearColor(1,0.40,0.3, 1)
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

barre1 = Rectangle(175, 0, 10, 200, 255, 22, 20 )

rectangle1 = Rectangle(50, 0, 275, 50, 93, 172, 255)
rectangle2 = Rectangle(75, 50, 225, 45, 51, 141, 255)
rectangle3 = Rectangle(100, 95, 175, 40, 245, 241, 11)
rectangle4 = Rectangle(125, 135, 125, 35, 21,209, 125 ) 
rectangle5 = Rectangle(150, 170, 75, 30, 223,209, 125 ) 


@window.event
def on_draw():
    window.clear()
    batch.draw()
pyglet.app.run()
