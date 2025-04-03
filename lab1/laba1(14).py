import turtle

def draw_star(t, size, points):
    angle = 180 - (180 / points)
    for _ in range(points):
        t.forward(size)
        t.right(angle)

screen = turtle.Screen()
screen.bgcolor("white")

star_turtle = turtle.Turtle()
star_turtle.speed(5)

star_turtle.penup()
star_turtle.goto(-100, 0)
star_turtle.pendown()
star_turtle.color("black")
draw_star(star_turtle, 100, 5)

star_turtle.penup()
star_turtle.goto(100, 0)
star_turtle.pendown()
star_turtle.color("black")
draw_star(star_turtle, 50, 11)

star_turtle.hideturtle()
turtle.done()
