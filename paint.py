from turtle import *
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle(start, end):
    "Draw circle from start to end."
    up() # Levanta el lapiz
    goto(start.x, start.y)  # Mueve el cursor al punto inicial
    down() # Baja el lapiz para dibujar
    begin_fill() # Comienza a rellenar la forma
    radius = ((end.x - start.x)**2 + (end.y - start.y)**2)**0.5  # Calcula el radio circulo 
    turtle.circle(radius)  # Dibuja el circulo usando el radio calculado 
    end_fill() # Termina de rellenar el circulo

def rectangle(start, end):
    "Draw rectangle from start to end."
    up()  # Levanta el lapiz
    goto(start.x, start.y)  # Mueve el cursor al punto inicial
    down()  # Baja el lapiz para dibujar
    begin_fill() # Comienza a rellenar la forma
    width = end.x - start.x # Calcula el ancho del rectangulo
    height = end.y - start.y  # Calcula la altura del rectangulo
    for _ in range(2): # Dibuja los lados del rectangulo (dos pares de lados opuestos)
        forward(width)  # Dibuja un lado
        left(90) # Gira 90 grados a la izquierda
        forward(height)  # Dibuja el otro lado
        left(90) # Gira 90 grados a la izquierda
    end_fill() # Termina de rellenar el rectangulo

def triangle(start, end):
    "Draw triangle from start to end."
    up()  # Levanta el lapiz
    goto(start.x, start.y) # Mueve el cursor al punto inicial
    down() # Baja el lapiz para dibujar
    begin_fill() # Comienza a rellenar la forma
    for _ in range(3): # Dibuja tres lados para formar un triangulo
        forward(end.x - start.x) # Dibuja un lado del triangulo
        left(120) # Gira 120 grados a la izquierda para formar el angulo del triangulo
    end_fill() # Termina de rellenar el triangulo

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']  # Obtiene la forma que se va a dibujar
        end = vector(x, y)
        shape(start, end)
        state['start'] = None # Resetea el punto de inicio despues de dibujar

def store(key, value):
    "Store value in state at key."
    state[key] = value # Guarda valor en diccionario

# Diccionario: almacena el estado de inicio y la forma actual seleccionada
state = {'start': None, 'shape': line}
#Tamaño de la ventana de dibujo
setup(420, 420, 370, 0)
# Detecta clics en pantalla para iniciar el dibujo
onscreenclick(tap)
listen()

# Asignacion de teclas para deshacer y cambiar colores
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y')

# Asignacion de teclas para seleccionar las formas a dibujar
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')

done()# Finaliza el programa y cierra la ventana
