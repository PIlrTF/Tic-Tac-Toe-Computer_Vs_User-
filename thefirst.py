# conect the other two modules

import graphics as gs

import time as _time

win=gs.GraphWin('THE FIRST WINDOW',300,300)
win.setCoords(0,0,300,300)

win.setBackground('#c5de58')
for i in range(2,298,3):
    line1=gs.Line(gs.Point(i,2),gs.Point(i,298))
    line1.setFill('black')
    line1.draw(win)
for k in range(2,298,3):
    line1=gs.Line(gs.Point(2,k),gs.Point(298,k))
    line1.setFill('black')
    line1.draw(win)
rec=gs.Line(gs.Point(1,1),gs.Point(299,1))
rec.setFill('black')
rec.draw(win)
rec=gs.Line(gs.Point(2,2),gs.Point(298,2))
rec.setFill('black')
rec.draw(win)

rec=gs.Line(gs.Point(1,1),gs.Point(1,299))
rec.setFill('black')
rec.draw(win)
rec=gs.Line(gs.Point(2,2),gs.Point(2,298))
rec.setFill('black')
rec.draw(win)

rec=gs.Line(gs.Point(1,299),gs.Point(299,299))
rec.setFill('black')
rec.draw(win)

rec=gs.Line(gs.Point(2,298),gs.Point(298,298))
rec.setFill('black')
rec.draw(win)

rec=gs.Line(gs.Point(299,299),gs.Point(299,1))
rec.setFill('blue')
rec.draw(win)

rec=gs.Line(gs.Point(298,298),gs.Point(298,2))
rec.setFill('black')
rec.draw(win)

rec4=gs.Rectangle(gs.Point(10,10),gs.Point(292,292))
rec4.setFill('black')
rec4.draw(win)
rec3=gs.Rectangle(gs.Point(15,15),gs.Point(287,287))
rec3.setFill('blue')
rec3.draw(win)
rec2=gs.Rectangle(gs.Point(20,20),gs.Point(282,282))
rec2.setFill('black')
rec2.draw(win)
rec1=gs.Rectangle(gs.Point(30,30),gs.Point(270,270))
rec1.setFill('#24df47')
rec1.draw(win)


rec=gs.Rectangle(gs.Point(160,180),gs.Point(260,220))
rec.setFill('black')
rec.draw(win)
rec=gs.Rectangle(gs.Point(162,182),gs.Point(258,218))
rec.setFill('#fdba06')
rec.draw(win)

m=gs.Text(gs.Point(210,200),'X')
m.setSize(32)
m.setStyle('bold')
m.setFill('black')

m.draw(win)

rec=gs.Rectangle(gs.Point(160,70),gs.Point(260,110))
rec.setFill('black')
rec.draw(win)

rec=gs.Rectangle(gs.Point(162,72),gs.Point(258,108))
rec.setFill('#fdba06')
rec.draw(win)

m=gs.Text(gs.Point(210,90),'0')
m.setSize(32)
m.setStyle('bold')
m.setFill('black')
m.draw(win)

rec=gs.Rectangle(gs.Point(48,68),gs.Point(132,232))
rec.setFill('black')
rec.draw(win)


rec=gs.Rectangle(gs.Point(50,70),gs.Point(130,230))
rec.setFill('#04d8ff')
rec.draw(win)

p=True
while p==True:
    g=n=0
    f=win.getMouse()
    p=f.getX()
    t=f.getY()
    if 162<=p<=258 and 72<=t<=108:
        g="0"
        n="X"
        m=gs.Text(gs.Point(90,150),'0')
        m.setSize(36)
        m.setStyle('bold')
        m.setFill('red')
        m.draw(win)
    elif 162<=p<=258 and 182<=t<=218:
        g="X"
        n="0"
        m=gs.Text(gs.Point(90,150),'X')
        m.setSize(36)
        m.setStyle('bold')
        m.setFill('red')
        m.draw(win)
    else:
        p=True
else:
    if g=="X":        
        _time.sleep(1)
        win.close()
        import xor0
    else:
        _time.sleep(1)
        win.close()
        import parttwo
