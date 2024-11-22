import turtle
import time

screen = turtle.Screen()
screen.bgcolor("black")

leonardo = turtle.Turtle()
leonardo.color("green")
leonardo.shape("turtle")

time.sleep(1)

def bewegung():
    leonardo.left(180)
    leonardo.forward(100)
    
    
bewegung()
  
screen.mainloop()