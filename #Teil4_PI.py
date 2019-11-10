import turtle as tu

lines = 10000 #Anzahl Linien

with open("1_million_digits_of_pi.txt", "r") as f:
    pi = f.read()

tu.mode("logo")
tu.tracer(False)
tu.screensize(2000,2000,"black")
tu.colormode(255)


for n in range(lines):
    color = int(n/(lines/255))
    tu.pencolor(255,255-color,color)
    zahl = int(pi[n])
    rotation = zahl * 36
    tu.setheading(rotation)
    tu.forward(5) #Linienlänge
    if n % 1_000 == 0: #Update nach
        tu.update()

tu.getcanvas().postscript(file=("PI_Picture.ps"))
tu.done()
