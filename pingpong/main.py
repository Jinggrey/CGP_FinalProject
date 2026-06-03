import turtle

# Game Settings
WIDTH = 800
HEIGHT = 600
WIN_SCORE = 5

# Screen
wn = turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor("black")
wn.setup(width=WIDTH, height=HEIGHT)
wn.tracer(0)

# Scores
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("cyan")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("magenta")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("lime")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15

# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(
    "Player A: 0  Player B: 0",
    align="center",
    font=("Courier", 24, "bold")
)

# Paddle Controls
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        paddle_a.sety(y + 20)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -250:
        paddle_a.sety(y - 20)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        paddle_b.sety(y + 20)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -250:
        paddle_b.sety(y - 20)

# Keyboard
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Winner Display
def show_winner(winner):
    msg = turtle.Turtle()
    msg.hideturtle()
    msg.color("lime")
    msg.penup()

    msg.goto(0, 40)
    msg.write(
        f"{winner} WINS!",
        align="center",
        font=("Courier", 36, "bold")
    )

    msg.goto(0, -40)
    msg.color("red")
    msg.write(
        "GAME OVER",
        align="center",
        font=("Courier", 24, "bold")
    )

# Main Loop
running = True

while running:
    wn.update()

    # Move Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Top and Bottom Collision
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Right Wall
    if ball.xcor() > 390:
        score_a += 1
        ball.goto(0, 0)
        ball.dx *= -1

        pen.clear()
        pen.write(
            f"Player A: {score_a}  Player B: {score_b}",
            align="center",
            font=("Courier", 24, "bold")
        )

    # Left Wall
    if ball.xcor() < -390:
        score_b += 1
        ball.goto(0, 0)
        ball.dx *= -1

        pen.clear()
        pen.write(
            f"Player A: {score_a}  Player B: {score_b}",
            align="center",
            font=("Courier", 24, "bold")
        )

    # Paddle B Collision
    if (
        340 < ball.xcor() < 350
        and paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50
    ):
        ball.setx(340)
        ball.dx *= -1

    # Paddle A Collision
    if (
        -350 < ball.xcor() < -340
        and paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50
    ):
        ball.setx(-340)
        ball.dx *= -1

    # Win Condition
    if score_a >= WIN_SCORE:
        show_winner("PLAYER A")
        running = False

    if score_b >= WIN_SCORE:
        show_winner("PLAYER B")
        running = False

wn.mainloop()