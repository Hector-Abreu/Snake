import turtle
import time 
import random

pospose = 0.1

# Scores
score = 0
highScore = 0

# Text
text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.hideturtle()
text.goto(0, -260)
text.write("Score: 0  High Score: 0", align="center")

# Windows conf
wn = turtle.Screen()
wn.title("Test")
wn.setup(width=600, height=600)
wn.bgcolor("black")
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Food 
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0,100)

# Snake body
array = []

# Functions
def up():
  head.direction = "up"
def down():
  head.direction = "down"
def right():
  head.direction = "right"
def left():
  head.direction = "left"

# Teclado
wn.listen()
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(right, "Right")
wn.onkeypress(left, "Left")

def mov():
  if head.direction == "up":
    y = head.ycor()
    head.sety(y + 20)
  if head.direction == "down":
    y = head.ycor()
    head.sety(y - 20)
  if head.direction == "right":
    x = head.xcor()
    head.setx(x + 20)
  if head.direction == "left":
    x = head.xcor()
    head.setx(x - 20)

# Main loop
while True:
  wn.update()

  # Border collision
  if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
    time.sleep(1)
    head.goto(0,0)
    head.direction = "stop"

    # Hide segs (Check this)
    for seg in array:
      seg.goto(1000,1000)

    # Clean segs list
    array.clear()

    # Reset score
    score = 0
    text.clear()
    text.write("Score: {}  High Score: {}".format(score, highScore), align="center")

  if head.distance(food) < 20:
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    food.goto(x, y)

    # Snake head
    seg = turtle.Turtle()
    seg.speed(0)
    seg.shape("square")
    seg.color("grey")
    seg.penup()
    array.append(seg)

    score += 1

    if score > highScore:
      highScore = score
    
    text.clear()
    text.write("Score: {}  High Score: {}".format(score, highScore), align="center")


  totalSegs = len(array)
  for index in range(totalSegs - 1, 0, -1):
    x = array[index - 1].xcor()
    y = array[index - 1].ycor()
    array[index].goto(x,y)

  if totalSegs > 0:
    array[0].goto(head.xcor(), head.ycor())

  mov()

  # Body collision
  for seg in array:
    if seg.distance(head) < 20:
      time.sleep(1)
      head.goto(0,0)
      head.direction = "stop"

      score = 0

      text.clear()
      text.write("Score: {}  High Score: {}".format(score, highScore), align="center")

      for seg in array:
        seg.goto(1000, 1000)

      array.clear()

  time.sleep(pospose)

# Mantener ventana abierta
# wn.mainloop()