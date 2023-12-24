import turtle
import random

def draw_triangle(size, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)
    
    turtle.end_fill()

def draw_rectangle(width, height, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    
    turtle.end_fill()

def draw_star(size, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    
    turtle.end_fill()

def draw_light(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()

def draw_text(message, x, y, size):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("red")
    turtle.write(message, font=("Arial", size, "normal"))

def draw_tree(trunk_width, trunk_height, tree_height, tree_color, trunk_color, star_size, star_color, num_lights):
    turtle.speed(2)
    
    # Draw trunk
    turtle.penup()
    turtle.goto(-trunk_width / 2, -trunk_height / 2)
    turtle.pendown()
    draw_rectangle(trunk_width, trunk_height, trunk_color)
    
    # Draw tree
    turtle.penup()
    turtle.goto(-tree_width / 2, -trunk_height / 2 + trunk_height)
    turtle.pendown()
    draw_triangle(tree_width, tree_color)
    
    # Draw star
    turtle.penup()
    turtle.goto(-star_size / 2, -trunk_height / 2 + trunk_height + tree_height)
    turtle.pendown()
    draw_star(star_size, star_color)
    
    # Draw lights
    for _ in range(num_lights):
        x = random.uniform(-tree_width / 2, tree_width / 2)
        y = random.uniform(-trunk_height / 2 + trunk_height, -trunk_height / 2 + trunk_height + tree_height)
        color = random.choice(["red", "yellow", "purple", "blue"])
        draw_light(x, y, color)
    
    # Draw text
    message = "SELAMAT HARI NATAL SEMUANYAAA"
    x_text = -150
    y_text = -trunk_height / 2 + trunk_height + tree_height + 30
    text_size = 12
    draw_text(message, x_text, y_text, text_size)

if __name__ == "__main__":
    # Set the dimensions and colors for the tree, trunk, star, and lights
    tree_width = 200
    trunk_width = 40
    trunk_height = 60
    tree_color = "green"
    trunk_color = "brown"
    star_size = 40
    star_color = "yellow"
    num_lights = 20
    
    # Draw the Christmas tree with lights and text
    draw_tree(trunk_width, trunk_height, tree_width, tree_color, trunk_color, star_size, star_color, num_lights)
    
    # Hide the turtle
    turtle.hideturtle()
    
    # Keep the window open
    turtle.done()