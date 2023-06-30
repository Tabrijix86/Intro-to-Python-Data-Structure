import turtle

wn = turtle.Screen()  # creates a graphics window
tj = turtle.Turtle()  # create a turtle named tj
tj.shape("turtle")
tj.speed(1)
for i in range(12):
    tj.forward(10)
    tj.penup()
    tj.forward(30)
    tj.pendown()
    tj.left(30)
    tj.forward(10)
tj.left(90)
turtle.exitonclick()
