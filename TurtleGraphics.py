# TurtleGraphics.py
# Name: Michael Walton
# Date: 09/22/2024
# Assignment: Lab 4 TurtleGraphics

import turtle  # Needed generally but not in CodeHS
hide_turtle()  # This hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    myTurtle.penup()
    myTurtle.goto(-size // 2, size // 2)
    myTurtle.pendown()
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)
    return size

def drawPolygon(myTurtle, sides):
    size = 100
    myTurtle.penup()
    myTurtle.goto(-size // 2, size // 2)
    myTurtle.pendown()
    angle = 360 / sides
    for i in range(sides):
        myTurtle.forward(size)
        myTurtle.right(angle)

def fillCorner(myTurtle, corner):
    size = drawSquare(myTurtle, 100)  #change size here. size is scaleable with drawSquare, wasn't sure what size to use
    cornerFill = size / 2

    #select corner position (formulas to scale)
    myTurtle.penup()
    myTurtle.hideturtle()
    if corner == 1:  #upper left
        myTurtle.goto(-size // 2, size // 2)
        myTurtle.goto(-size // 2, size // 2)
    elif corner == 2:  #upper right
        myTurtle.goto(size // 2, size // 2)
        myTurtle.goto(size // 2 - cornerFill, size // 2)
    elif corner == 3:  #lower left
        myTurtle.goto(-size // 2, -size // 2)
        myTurtle.goto(-size // 2, -size // 2 + cornerFill)
    elif corner == 4:  #lower right
        myTurtle.goto(size // 2, -size // 2)
        myTurtle.goto(size // 2 - cornerFill, -size // 2 + cornerFill)

    #fill corner
    myTurtle.showturtle()
    myTurtle.pendown()
    myTurtle.begin_fill()
    myTurtle.fillcolor("green")
    for i in range(4):
        myTurtle.forward(cornerFill)
        myTurtle.right(90)
    myTurtle.end_fill()

def squaresInSquares(myTurtle, numSquares):
    size = 100
    for i in range(numSquares):
        myTurtle.penup()
        myTurtle.goto(-size // 2, size // 2)
        myTurtle.pendown()
        drawSquare(myTurtle, size)
        size += 20  #each square gets bigger

def main():
    myTurtle = turtle.Turtle()
    
    #drawSquare(myTurtle, 100)

    #drawPolygon(myTurtle, 5)  # Draws a pentagon
    #drawPolygon(myTurtle, 8)  # Draws an octagon

    #!!!do not call drawSquare in main to run fillCorner
    #made fillCorner scaleable for size with drawSquare call inside fillCorner
    #fillCorner(myTurtle, 2)  # Draws a square with top right corner filled in
    #fillCorner(myTurtle, 3)  # Draws a square with bottom left corner filled in

    #squaresInSquares(myTurtle, 5)  # Draws 5 concentric squares
    #squaresInSquares(myTurtle, 3)  # Draws 3 concentric squares
    
    myTurtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
main()
