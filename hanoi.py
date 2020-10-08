import pyglet

window = pyglet.window.Window(fullscreen = True)
pyglet.gl.glClearColor(0.28,0.407,0.372, 1)
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

barre1 = Rectangle(175, 0, 25, 300, 255, 255, 255)
base1 = Rectangle(35, 0, 300, 30, 255, 255, 255)

barre2 = Rectangle(700, 0, 25, 300, 255, 255, 255)
base2 = Rectangle(560, 0, 300, 30, 255, 255, 255)

barre3 = Rectangle(1225, 0, 25, 300, 255, 255, 255)
base3 = Rectangle(1085, 0, 300, 30, 255, 255, 255)

rectangle1 = Rectangle(50, 30, 275, 50, 0, 170, 255)
rectangle2 = Rectangle(75, 80, 225, 45, 0, 212, 255)
rectangle3 = Rectangle(100, 125, 175, 40, 0, 255, 228)
rectangle4 = Rectangle(125, 165, 125, 35, 21,255, 189) 
rectangle5 = Rectangle(150, 200, 75, 30, 0,255, 178)

"""
Nous avond donc crée une classe Rectangle afin de modeliser nos differents
rectangle de notre mini-jeu. Ainsi, on a pu optimiser notre rectangle en lui
donnat sa position (x, y) ainsi que sa taille sur X et sur Y. Et enfin nous 
avons informer notre code de la couleur.
"""
@window.event
def on_draw():
    window.clear()
    batch.draw()
pyglet.app.run()
