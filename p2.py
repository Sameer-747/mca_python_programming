from turtle import *
speed(-1)
side = 6 
pencolor('red')
pensize(6)
colors = ['red' , 'blue']
for i in range(side):
    for i in range(side):
        fd(50)
        for i in range(side):
            dot(2)
            fd(25)
            lt(360/side) #360/5
            
        fd(50)
        lt(360/side)
    fd(100)
    lt(360/side)

hideturtle()
mainloop()