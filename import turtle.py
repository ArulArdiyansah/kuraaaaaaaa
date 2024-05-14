import turtle

# Setup screen 
wn = turtle.Screen()
wn.title("Save the Earth Animation")
wn.bgcolor("black")
wn.setup(width=800, height=600)

# Create turtle
earth = turtle.Turtle()
earth.shape("circle")
earth.color("blue")
earth.shapesize(strech_wid=5, strech_len=5)
earth.penup()
earth.goto(0, 0)

# Create text turtle
text_turtle = turtle.Turtle()
text_turtle.color("white")
text_turtle.penup()
text_turtle.hideturtle()
text_turtle.goto(0, -50)

# Animation function
def save_the_earth_animation():
    for _ in range(36):
        earth.right(10)
        text_turtle.clear()
        text_turtle.write("Save the Earth!", align="center", font=("Arial", 24, "normal"))
        wn.update()
        turtle.time.sleep(0,1)

# Run animation
save_earth_animation()

# Close window on click
wn.exitonclick()

    
                          