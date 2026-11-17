import turtle,random

t = turtle.Turtle()
t.speed(0) 
turtle.colormode(255)

def kwadrat(r,g,b):
        t.color("black", (r,g,b))
        t.begin_fill()
        for _ in range(4):
            t.forward(15)
            t.left(90)
        t.end_fill()
        t.forward(15)


def ostateczna_funkcja():
        y = 15
        for x in range(2):
            for x in range(5):
                for x in range(2):
                    for x in range(5):
                        r = random.randint(1, 100)
                        g = random.randint(1, 100)
                        b = random.randint(1, 100)
                        kwadrat(r,g,b)
                    for x in range(5):
                        r = random.randint(50, 255)
                        g = random.randint(50, 255)
                        b = random.randint(50, 255)
                        kwadrat(r,g,b)
                t.penup()
                t.goto(0,y)
                t.pendown()
                y += 15
            for x in range(5):
                        for x in range(2):
                            for x in range(5):
                                r = random.randint(50, 255)
                                g = random.randint(50, 255)
                                b = random.randint(50, 255)
                                kwadrat(r,g,b)
                            for x in range(5):
                                r = random.randint(1, 100)
                                g = random.randint(1, 100)
                                b = random.randint(1, 100)
                                kwadrat(r,g,b)
                            
                        t.penup()
                        t.goto(0,y)
                        t.pendown()
                        y += 15
ostateczna_funkcja()
turtle.done()