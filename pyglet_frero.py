"""                               
 TOUR DE HANNOI
Le projet consiste a résoudre le casse tête de "La tour de Hannoi" et de crée une interface
graphique ou le joueur peut interragir avec les differents objets de la fennêtre.
"""
import pyglet

window = pyglet.window.Window(720, 380, resizable = True)
pyglet.gl.glClearColor(1,0.40,0.3, 1)
batch = pyglet.graphics.Batch()
label = pyglet.text.Label('Bravo, vous avez gagné',
                          font_name='Times New Roman',
                          font_size=36,
                          x=760, y=472,
                          anchor_x='center', anchor_y='center')
"""
Pour ce faire nous créons une fenetre en deffinissant l'arriere plans c'est-à-dire la couleur 
via le systeme RGB ansi que l'opacité de la fenetre
Nous rentrons aussi dans les paramètre de la fênetre la resolution c'est-à-dire la taille de notre fenétre
(ici 720*380 )
Ainsi que le messqge en cas de réussite
"""
class Rectangle:
    """
    Afin d'eviter la repetitons de notre code, nous créons une classe qui vas nous permettre de crée un ensemble de
    rectangle. Notre code est optimiser au maximum. On peut y retrouver plusieurs methode
    """

    def __init__(self, x_pos, y_pos, x, y, r, g, b):
        """
        Tout d'abord nous initialisons notre objet (rectangle) en informant le programme des caractéristique primaire
        du rectangle c'est-à-dire les cordonné de son point le plus en bas gauche(x, y) ansi que sa taille sur (x, y) 
        mais aussi sa couleur, toujours en suivant le systéme RGB.
        """
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
      """
      Cette méthode permet de sélectione le rectangle qu'on souhairte manipuler. On recupere les cordonnées du curseur
      au moment du click. Ellle prend donc en paramétre les cordonée x et y et nous renvoie TRUE si c'est cordonnée sont 
      compris a l'interrieur d'un rectangle:
      if self.xpos <= x <= self.x_pos + self.x and self.y_pos<= y <= self.y_pos + self.y:
      >>> True
      """
        if x >= self.x_pos and y >= self.y_pos and x <= self.x + self.x_pos and y <= self.y + self.y_pos:
                return True

    
    def click_aura(self, x, y):
        """
        Cette methode permet de sélectioner la base sur laquelle vas être déposer
        le rectangle et fonctionnent de la même manière que la méthode précedente:
        x >= self.x_pos and y >= self.y_pos and x <= self.x + self.x_pos and y <= self.y + self.y_pos
        >>> True
        """
        if x >= self.x_pos and y >= self.y_pos:
            if x <= self.x + self.x_pos and y <= 300:
                return True

    def new_pos(self, x2, y2):
        """
        cette dernière méthode permet de redéfinir les positions initiale de notre rectangle pour pouvoir
        recommencer les maneuvres précèdentes
        """
        self.x_pos = x2
        self.y_pos = y2
        self.rectangle = Rectangle(self.x_pos, self.y_pos, self.x, self.y, self.r, self.g, self.b)


def rectangle_select(x,y):
    """
    LA fonction rectangle_select est une fonction qui prend en entré les cordonées (x, y ) du curseur lors du clik et
    qui renvoie la pile et la base correspondant au réctangle sélèctioner, elle est ici associer à la méthode click de 
    notre classe "Rectangle":
    >>> pile 2, base2
    elle admet aussi des exeption :
    >>> IndexError
    """
    try :
                
        if pile2[-1].click(x, y):
            return pile2, base2
    except(IndexError, AttributeError):
        pass
    try:        
        if pile1[-1].click(x, y):
            return pile1, base1
    except(IndexError, AttributeError):
        pass
    try:                  
        if pile3[-1].click(x, y):
            return pile3, base3
    except(IndexError, AttributeError):
        pass


def base_select(x, y):
    """
    La fonction de base_select est ici une fonction associér a la méthode click_aura de notre classe. Elle prend en entréé
    les cordonné du curseur lors du click et nous renvoi la pile et la base correspondant au clik:
    >>> base1, pile1
    """
    if base1.click_aura(x, y):
        return base1, pile1
    elif base2.click_aura(x, y):
        return base2, pile2
    elif base3.click_aura(x, y):
        return base3, pile3
    else :
        return None, None 

            
def victoire(pile3):
    """
    Est une fonction qui prend en paraméte la pile3 et qui retourne Ture ou False selon le nombre élèment de la liste, si il y'a 
    5 élèments (le nombre maximum possible dans une pile dans notre code) elle renvoi TRUE sinon FALSE
    len(pile3)= 5
    >>> True
    """
    if  len(pile3) == 5 :
        return True
    else :
        return False 
    



barre1 = Rectangle(175, 0, 25, 300, 255, 255, 255)
base1 = Rectangle(35, 0, 300, 30, 255, 255, 255)

barre2 = Rectangle(700, 0, 25, 300, 255, 255, 255)
base2 = Rectangle(560, 0, 300, 30, 255, 255, 255)

barre3 = Rectangle(1225, 0, 25, 300, 255, 255, 255)
base3 = Rectangle(1085, 0, 300, 30, 255, 255, 255)


rectangle5 = Rectangle(50, 30, 275, 30, 93, 172, 255)
rectangle4 = Rectangle(75, 60, 225, 30, 51, 141, 255)
rectangle3 = Rectangle(100, 90, 175, 30, 245, 241, 11)
rectangle2 = Rectangle(125, 120, 125, 30, 21,209, 125) 
rectangle1 = Rectangle(150, 150, 75, 30, 223,209, 125)



pile1 = [rectangle5, rectangle4, rectangle3, rectangle2, rectangle1]
pile2 = []
pile3 = []


select = False
p_select = None
old_b = None
jeu = True


@window.event
def on_mouse_press(x, y, button, modifiers):
    global select, p_select, old_b, jeu
    
    if not select:
        select = True
        try:
            p_select, old_b = rectangle_select(x, y)
        except TypeError:
            pass

    elif select:
        while select:
            try:
                b_select, new_p = base_select(x,y)
                if new_p and p_select[-1].x > new_p[-1].x:
                    pass         
                elif not b_select :
                    pass
                elif p_select == new_p :
                    pass
                elif p_select == None:
                    pass
                else :    
                    p_select[-1].new_pos(b_select.x_pos + (p_select[-1].x_pos-old_b.x_pos), b_select.y + len(new_p)*30)
                    new_p.append(p_select[-1])
                    p_select.pop(-1)        
            except TypeError:
                pass

            p_select = None
            select = False
            if victoire(pile2, pile3):
                jeu = False
            else :
                pass
   

"""
cette derniére partie permet de créé l'évènement Window qui permet de configurer et de lancer les ordre donner à la
fenêtre:
"clear" permetet d'effacer, 
"draw",permet de dessiner
"label" permet d'écrire 
"""



@window.event
def on_draw():
    window.clear()
    batch.draw()
    if not jeu:
        label.draw()
pyglet.app.run()#lance la fenêtre
