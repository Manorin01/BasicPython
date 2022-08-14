import turtle
tao = turtle.Pen()#make your pen
tao.shape('turtle')#Evolution it turtle
turtle.bgcolor('green')
def M():

    for i in range(4):
        tao.right(90)
        tao.forward(150)
        
def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()        
M()
