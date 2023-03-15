import turtle

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

# Set up the turtle window and turtle
window = turtle.Screen()
window.setup(width=800, height=800)
window.title("Fractal Tree")
t = turtle.Turtle()
t.left(90)
t._tracer(0)
t.speed(0)
t.color('black')

# Ask the user for the angle to use
angle_str = turtle.textinput("Fractal Tree", "Enter the angle:")
angle = int(angle_str) if angle_str is not None else 45

# Ask the user for the depth to use
depth_str = turtle.textinput("Fractal Tree", "Enter the depth:")
depth = int(depth_str) if depth_str is not None else 10

# Draw the fractal tree with the specified angle and depth
draw_tree(100, angle, depth)
t.penup()

# Keep the turtle window open
turtle.mainloop()