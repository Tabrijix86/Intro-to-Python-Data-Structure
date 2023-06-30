import turtle

wn = turtle.Screen()  # creates a graphics window
tj = turtle.Turtle()  # create a turtle named tj
tj.shape("turtle")
tj.speed(1.5)
for side_length in range(50, 100, 10):
    for i in range(4):
        tj.forward(side_length)
        tj.left(90)

tj.left(90)
turtle.exitonclick()
