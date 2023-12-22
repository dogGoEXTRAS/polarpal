import turtle as t


window = t.Screen()
window.title("Cookie Clicker by PolarPal A.I.")
window.bgcolor('#D2E3F0')

window.register_shape('cookie.gif')

c = t.Turtle()
c.shape('cookie.gif')

clicks = 0
p = t.Turtle()
p.hideturtle()
p.color('black')
p.penup()
p.goto(0, 230)
p.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))

def clicked(x, y): 
    global clicks
    clicks += 1
    p.clear()
    p.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))

c.onclick(clicked)

window.mainloop()

