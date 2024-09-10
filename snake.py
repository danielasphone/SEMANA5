from turtle import *
from random import randrange
from freegames import square, vector

# Para definir la comida y la serpiente
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Para la direccion en la que la comida se movera al azar
food_direction = vector(10, 0)

def change(x, y):
    "Cambiar la dirección de la serpiente."
    aim.x = x
    aim.y = y

def inside(head):
    "Devuelve True si la cabeza está dentro de los límites."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Mueve la serpiente un segmento hacia adelante."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Serpiente:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    # Mover la comida un paso en la direccion actual
    food.move(food_direction)

    # Cambiar direccion de la comida si llega a los limites de la ventana
    if not inside(food):
        food_direction.x = randrange(-1, 2) * 10
        food_direction.y = randrange(-1, 2) * 10

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

# Configuracion inicial del juego
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
