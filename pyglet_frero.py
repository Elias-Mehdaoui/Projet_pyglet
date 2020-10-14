import pyglet

window = pyglet.window.Window(720, 380, resizable = True)
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
        self.anchor_position = self.x/2, self.y/2  
    
    def click(self, x, y):
        print(x, y)
        if x >= self.x_pos and y >= self.y_pos:
            if x <= self.x + self.x_pos and y <= self.y + self.y_pos:
                return True

    
    def click_aura(self, x, y):
        if x >= self.x_pos and y >= self.y_pos:
            if x <= self.x + self.x_pos and y <= 300:
                return True

    



barre1 = Rectangle(175, 0, 25, 300, 255, 255, 255)
base1 = Rectangle(35, 0, 300, 30, 255, 255, 255)

barre2 = Rectangle(700, 0, 25, 300, 255, 255, 255)
base2 = Rectangle(560, 0, 300, 30, 255, 255, 255)

barre3 = Rectangle(1225, 0, 25, 300, 255, 255, 255)
base3 = Rectangle(1085, 0, 300, 30, 255, 255, 255)


rectangle5 = Rectangle(50, 30, 275, 50, 93, 172, 255)
rectangle4 = Rectangle(75, 80, 225, 45, 51, 141, 255)
rectangle3 = Rectangle(100, 125, 175, 40, 245, 241, 11)
rectangle2 = Rectangle(125, 165, 125, 35, 21,209, 125) 
rectangle1 = Rectangle(150, 200, 75, 30, 223,209, 125)



pile1 = [rectangle5, rectangle4, rectangle3, rectangle2, rectangle1]
pile2 = []
pile3 = []

piles = [pile1, pile2, pile3]

bases = [base1, base2, base3]


@window.event
def on_mouse_press(x, y, button, modifiers):
        if pile1[-1].click(x, y):
            print("bien joue")        
        
        for base in bases:
            if base.click_aura:
                print("ok")
        



@window.event
def on_draw():
    window.clear()
    batch.draw()
pyglet.app.run()
