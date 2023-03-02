# The goal of this project is to create a fractal tree which changes the angle at which the fractal gets drawn based on the position of the mouse.
# We are using turtle which is a library that lets us draw the fractal on a virtual canvas. For now I do not have the code update based on the position of the mouse but I it can draw a fractal tree based on an initial angle provided.

#Looking at your code it makes a cool fractal tree and I really like it, I don't exactly see how you could make it change with the mouse position but I don't know turtle

import turtle

n = int(input("What angle: "))

# Define the recursive function to draw the tree
def draw_tree(length, angle, level):
    if level == 0:
        return
    t.forward(length)
    new_length = length * 0.7
    t.left(angle)
    draw_tree(new_length, angle, level - 1)
    t.right(angle * 2)
    draw_tree(new_length, angle, level - 1)
    t.left(angle)
    t.backward(length)

window = turtle.Screen()
window.setup(width=800, height=800)  #this window size seems a bit big especially at the bottom for the size tree that its making, maybe make it smaller or is there a way to zoom in on the window to see the tree up closer?
window.title("Fractal Tree")

t = turtle.Turtle()
t.left(90)
t._tracer(0)
t.speed(0)
t.color('black')  #if you wanted to add another interactive element you could let the user input or choose a color pretty easily here I think

draw_tree(100, n, 10)
t.penup()
# Keep the turtle window open
turtle.mainloop()

