import turtle
import time
import random

delay = 0.1
score = 0
previous_score = 0
highscore = 0
body = []
playing = True
move_made = True

file = open("/Users/khuang22/PycharmProjects/Snake/highscores.txt")
highscore = int(file.read())
file.close()


# Panel
panel = turtle.Screen()
panel.title("Snake")
panel.setup(590, 590)
panel.bgcolor("black")
panel.tracer(0)

# Head Piece
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(-5, 5)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(-5, 100)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0, 260)
pen.hideturtle()


# Movement
def go_up():
    global move_made
    if head.direction != "down" and move_made:
        head.direction = "up"
        move_made = False


def go_down():
    global move_made
    if head.direction != "up" and move_made:
        head.direction = "down"
        move_made = False


def go_left():
    global move_made
    if head.direction != "right" and move_made:
        head.direction = "left"
        move_made = False


def go_right():
    global move_made
    if head.direction != "left" and move_made:
        head.direction = "right"
        move_made = False


def stop_moving():
    head.direction = "stop"
    print("paused")


def add_body():
    part = turtle.Turtle()
    part.speed(0)
    part.color("gray")
    part.shape("square")
    part.penup()
    if head.direction == "up":
        part.goto(head.xcor(), head.ycor() - 20)
    if head.direction == "down":
        part.goto(head.xcor(), head.ycor() + 20)
    if head.direction == "left":
        part.goto(head.xcor() - 20, head.ycor())
    if head.direction == "right":
        part.goto(head.xcor() + 20, head.ycor())
    body.append(part)

# for index in range(len(body)-1, 0, -1):
#         x = body[index-1].xcor()
#         y = body[index-1].ycor()
#         body[index].goto(x, y)


def move_body():
    if head.direction != "stop":
        if len(body) >= 1:
            body[-1].goto(head.xcor(), head.ycor())
            body.insert(0, body.pop(-1))

    # if len(body) == 1:
    #     body[-1].goto(head.xcor(),head.ycor())
    # elif len(body) > 1:
    #     for i in range(len(body) - 1, 0, -1):
    #         body[i].goto(body[i-1].xcor(), body[i-1])


def move_head():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)
    if head.xcor() < -285 or head.xcor() > 285 or head.ycor() < -285 or head.ycor() > 285:
        end_game()
    for b in body:
        if b.distance(head) <= 10:
            end_game()
            break


def eat_food():
    if head.distance(food) <= 10:
        food.goto((random.randint(-12, 12) * 20 - 5), (random.randint(-12, 12) * 20 + 5))
        global score
        score += 100
        add_body()


def end_game():
    global playing
    global previous_score
    global highscore
    global score
    playing = not playing
    for b in body:
        b.hideturtle()
    body.clear()
    head.goto(-5, 5)
    head.direction = "stop"
    food.goto(-5, 100)
    previous_score = score

    if score > highscore:
        highscore = score
        file = open("/Users/khuang22/PycharmProjects/Snake/highscores.txt", "w")
        file.write(str(score))
        file.close()

    score = 0

def draw_text():
    pen.clear()
    if playing is False:
        pen.goto(0, 200)
        pen.write("Previous Score: " + str(previous_score) + "\nHighscore: " + str(highscore), font=("Arial", 18, "normal"), align="center")
    else:
        pen.goto(0, 200)
        pen.write("Score: " + str(score), font=("Arial", 18, "normal"), align="center")


# Keyboard Controls
panel.listen()
panel.onkeypress(go_up, "Up")
panel.onkeypress(go_down, "Down")
panel.onkeypress(go_left, "Left")
panel.onkeypress(go_right, "Right")
panel.onkeypress(end_game, "r")
panel.onkeypress(stop_moving, "p")

while True:
    panel.update()
    draw_text()
    if head.direction != "stop":
        playing = True
    if playing:
        move_body()
        move_head()
        eat_food()
        time.sleep(delay)
        move_made = True

turtle.mainloop()
