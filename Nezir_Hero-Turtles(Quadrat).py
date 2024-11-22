import turtle

screen = turtle.Screen()
screen.bgcolor("black")


drawer = turtle.Turtle()
drawer.color("red")
drawer.speed(5)
drawer.shape("turtle")

def schildkroete():
    drawer.forward(100)
    drawer.left(90)
    drawer.forward(100)
    drawer.left(90)
    drawer.forward(100)
    drawer.left(90)
    drawer.forward(100)
    
schildkroete()

screen.mainloop()
