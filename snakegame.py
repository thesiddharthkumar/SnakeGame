import turtle
from random import randrange
from freegames import square, vector
food = vector(0, 0)
man = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change man direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move man forward one segment."
    head = man[-1].copy()
    head.move(aim)

    if not inside(head) or head in man:
        square(head.x, head.y, 9, 'red')
        turtle.update()
        return

    man.append(head)

    if head == food:
        print('Snake:', len(man))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        man.pop(0)

    turtle.clear()

    for body in man:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'black')
    turtle.update()
    turtle.ontimer(move, 100)


turtle.hideturtle()
turtle.tracer(False)
turtle.listen()
turtle.onkey(lambda: change(10, 0), 'Right')
turtle.onkey(lambda: change(-10, 0), 'Left')
turtle.onkey(lambda: change(0, 10), 'Up')
turtle.onkey(lambda: change(0, -10), 'Down')
move()
turtle.done()