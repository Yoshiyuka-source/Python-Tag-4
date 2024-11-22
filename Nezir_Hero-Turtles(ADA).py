import turtle
import time

screen = turtle.Screen()
screen.bgcolor("black")

time.sleep(1)

ADA = turtle.Turtle()
ADA.color("green")
ADA.shape("turtle")

ADA.penup()
ADA.goto(-150, 100)
ADA.pendown()

ADA.write("A", font=("Arial", 50, "bold"))

ADA.penup()
ADA.goto(-100, 100)
ADA.pendown()

ADA.write("D", font=("Arial", 50, "bold"))

ADA.penup()
ADA.goto(-50, 100)
ADA.pendown()

ADA.write("A", font=("Arial", 50, "bold"))

turtle.done()
  
screen.mainloop()