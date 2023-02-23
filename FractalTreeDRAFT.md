# The goal of this project is to create a fractal tree which changes the angle at which the fractal gets drawn based on the position of the mouse.
# We are using turtle which is a library that lets us draw the fractal on a virtual canvas. For now I do not have the code update based on the position of the mouse but I it can draw a fractal tree based on an initial angle provided.


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
window.setup(width=800, height=800)
window.title("Fractal Tree")

t = turtle.Turtle()
t.left(90)
t._tracer(0)
t.speed(0)
t.color('black')

draw_tree(100, n, 10)
t.penup()
# Keep the turtle window open
turtle.mainloop()

