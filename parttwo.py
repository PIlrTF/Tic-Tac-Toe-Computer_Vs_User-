#X AND 0 PART - II

#ALIAS PAR


'''----------------------------------------------------------_MODULE_--------------------------------------------------------------------------'''

from graphics import*

import time as _time

import random as _random

import math as _math

'''------------------------------------------------------------------------------''''''-----------------------------'''
def delcompl(n,compl):
    for i in range(len(compl)):
        if compl[i]==n:
            compl.pop(i)
            break

def check(listr,soft,ch):
    
    cvu=False
    ml=[]
    for i in soft:
        for k in listr:
            if k==i[0]:
                ml.append(k)
            elif k==i[1]:
                ml.append(k)
            elif k==i[2]:
                ml.append(k)
        else:
            if len(ml)==3:
                if ch=='X' or ch=='x':
                    print('I won')
                    exit(0)
                elif ch=='0' or ch=='o' or ch=='O':
                    print('you won the game')
                    exit(0)
                cvu=True
                return cvu
            else:
                ml=[]
    else:
        cvu=False
        return cvu

def drawgrid():
    
    Line(Point(0,100),Point(300,100)).draw(win)
    Line(Point(0,200),Point(300,200)).draw(win)
    Line(Point(100,0),Point(100,300)).draw(win)
    Line(Point(200,0),Point(200,300)).draw(win)
    win.setBackground("turquoise")

def binsearch(item, listl):
    listl=sort(listl)
def delh(pres,item):
    for i in range(len(pres)):
        if pres[i]==item:
            pres.pop(i)
            break
        return pres

def  position(s,t):
    if 0<=t<=100 and 200<=s<=300:
        position=1
    if 0<=t<=100 and 100<=s<=200:
        position=4
    if 0<=t<=100 and 0<=s<=100:
        position=7
    if 100<=t<=200 and 200<=s<=300:
        position=2
    if 100<=t<=200 and 100<=s<=200:
        position=5
    if 100<=t<200 and 0<=s<100:
        position=8
    if 200<=t<300 and 100<=s<200:
        position=6
    if 200<=t<300 and 200<=s<300:
        position=3
    if 200<=t<=300 and 0<=s<=100:
        position=9
    return position

def plotx(n,pos):
    if pos==1:        
        q=Text(Point(50,250),n)
        q.setSize(36)
        q.draw(win)
        
    elif pos==2:        
        q=Text(Point(150,250),n)
        q.setSize(36)
        q.draw(win)
        
    elif pos==3:
        q=Text(Point(250,250),n)
        q.setSize(36)
        q.draw(win)
        
    elif pos==4:        
        q=Text(Point(50,150),n)
        q.setSize(36)
        q.draw(win)
        
    elif pos==5:        
        q=Text(Point(150,150),n)
        q.setSize(36)
        q.draw(win)
        
    elif pos==6:        
        q=Text(Point(250,150),n)
        q.setSize(36)
        q.draw(win)
        
    elif pos==7:        
        q=Text(Point(50,50),n)
        q.setSize(36)
        q.draw(win)
        
    elif pos==8:        
        q=Text(Point(150,50),n)
        q.setSize(36)
        q.draw(win)
        
    elif pos==9:
        q=Text(Point(250,50),n)
        q.setSize(36)
        q.draw(win)
        

class post:    
    def __init__(self):        
        self.pos=[]
        
    def sort(self,pos):        
        for i in range(1,len(pos)):
            key=pos[i]
            j=i-1
            while j>=0 and key<pos[j]:
                pos[j+1]=pos[j]
                j=j-1
            else:
                pos[j+1]=key
        return pos
    
    def delforms(self, softy,position):
        
        for i in softy:
            for k in range(len(i)):
                if i[k]==position:
                    i.pop(k)
                    break
    def app(self,post,position):
        post.append(position)
        return post
    def thirdchance(self,soft,softy,queue,compl,pres,pot):
        f=[]
        for k in queue:
            if len(k)==3:
                for m in k:
                    if m==pot[0]:
                        f.append(m)
                    elif m==pot[1]:
                        f.append(m)
                else:
                    if len(f)==2:
                        print('k',k)
                        for l in k:
                            if l==f[0]:
                                pass
                            elif l==f[1]:
                                pass
                            else:
                                g=l
                                if g in compl:
                                    return [g]
                                else:
                                    return [None]
                    else:
                        g=0
                        f=[]
        else:
            return [None]
        
                        
                    
                
                            
            


#__main__
    
#constants


triplet=[[7,5,9],[1,5,3],[1,5,7],[3,5,9]]
kile=[[1,2,3],[4,5,6],[7,8,9],[3,6,9],[1,4,7],[2,5,8],[1,5,9],[3,5,7]] 
queue=[[1,2,3],[4,5,6],[7,8,9],[3,6,9],[1,4,7],[2,5,8],[1,5,9],[3,5,7]]
compl=[1,2,3,5,6,7,8,9,4]
soft=[[1,2,3],[4,5,6],[7,8,9],[3,6,9],[1,4,7],[2,5,8],[1,5,9],[3,5,7]]          #Remains constant throughout the program
softy= [[1,2,3],[4,5,6],[7,8,9],[3,6,9],[1,4,7],[2,5,8],[1,5,9],[3,5,7]]       # Will reduce as the game proceeds
p='0x4554433132'
win=GraphWin("Hello world",400,400)                               
win.setCoords(0,0,300,300)
win.setBackground('gold')

drawgrid()

variable='X'

#___________COMP INPUT - 1

presco=post()   
_random.shuffle(compl)
_time.sleep(1)
plotx('X',compl[0])
posit=compl[0]

presco.pos.append(posit)
presco.delforms(softy,posit)
delcompl(posit,compl)
presco.delforms(kile,posit)  

#__________________USER INPUT-1

while posit not in compl:
    f1=win.getMouse()
    t=f1.getX()
    s=f1.getY()
    posit=position(s,t)
else:
    plotx('0',posit)

pres=post()
pres.pos.append(posit)
delcompl(posit,compl)
pres.delforms(queue,posit)
print('queue1',queue)
pres.delforms(kile,posit)      

#__________________COMP INPUT-2

ifone=0
if (pres.pos[0] in [2,8]) and presco.pos[0]==4:
    _time.sleep(1)
    plotx('X',5)
    posit=5
    ifone=1
else:
    count=False
    queue2=list(queue)
    #g=[]
    _random.shuffle(queue2)
    for k in queue2:
        if count==True:
            break
        _random.shuffle(k)
        if len(k)==3:
            _random.shuffle(k)
            if presco.pos[0] in k:
                for m in k:
                    if m!=presco.pos[0] :
                        _time.sleep(1)
                        plotx('X',m)
                        posit=m
                        count=True
                        break


presco.pos.append(posit)
delcompl(posit,compl)
presco.delforms(softy,posit)
presco.delforms(kile,posit)
iota=check(presco.pos,soft,'X') 
#---------------------------------------- USER INPUT-2

while posit not in compl:
    f1=win.getMouse()
    t=f1.getX()
    s=f1.getY()
    posit=position(s,t)
else:
    plotx('0',posit)


pres.pos.append(posit)
delcompl(posit,compl)
pres.delforms(queue,posit)
pres.delforms(kile,posit)  
print('pres',pres.pos)

#---------------------------------------- COMPUTER INPUT-3
pipe='9'
q='D'
if 6 not in compl:
    q='okay'
    if ifone==1:
        _time.sleep(1)
        plotx('X',7)
        posit=7
        presco.pos.append(posit)
        delcompl(posit,compl)
        presco.delforms(softy,posit)
        presco.delforms(kile,posit)     
    else:
        q='D' 
if q=='D':
    b=presco.thirdchance(soft,softy,queue,compl,pres.pos,presco.pos)
    if b[0]!=None:
        _time.sleep(1)
        plotx('X',b[0])
        posit=b[0]
        presco.pos.append(posit)
        delcompl(posit,compl)
        presco.delforms(softy,posit)
        presco.delforms(kile,posit)    
        
    else:
        cont=False
        _random.shuffle(softy)
        softy.append(['a','b','c'])
        for lt in  softy:
            if len(lt)==3:
                
                if cont==True:
                    
                    delcompl(posit,compl)
                    presco.delforms(softy,posit)
                    presco.delforms(kile,posit)      
                    break
                pres.sort(pres.pos)
                if (pres.pos[0] in lt) and (pres.pos[1] in lt):
                    for mk in lt:
                        if mk==pres.pos[0] :
                            pass
                        elif mk==pres.pos[1]:
                            pass
                        else:
                            _time.sleep(1)
                            if  mk in compl:
                                posit=mk
                                _time.sleep(1)
                                plotx('X',mk)
                                presco.pos.append(posit)
                                cont=True
                                break
                
        else:
            pipe='55'
            
            print('else')
print(softy)
print('pres',pres.pos)
presco.sort(presco.pos)
pres.sort(pres.pos)
if pipe=='55':
    if (presco.pos in [[1,3],[7,9]]) and (pres.pos in [[2,6],[6,8]]):
        _time.sleep(1)
        plotx('X',5)
        posit=5
        presco.pos.append(posit)
        delcompl(posit,compl)
        presco.delforms(softy,posit)
        presco.delforms(kile,posit)      
    elif (presco.pos== [2,7]) and (pres.pos ==[6,9]) :
        _time.sleep(1)
        posit=3
        plotx('X',3)
        presco.pos.append(posit)
        delcompl(posit,compl)
        presco.delforms(softy,posit)
        presco.delforms(kile,posit)      
    elif (presco.pos== [2,9]) and (pres.pos ==[4,7]) :
        posit=1
        plotx('X',1)
        presco.pos.append(posit)
        delcompl(posit,compl)
        presco.delforms(softy,posit)
        presco.delforms(kile,posit)
    else:
        proceed=0
        for kl in queue:
            if len(kl)==3:
                if presco.pos[0] in kl:   
                    for j in kl:
                        if j!=presco.pos[0]:
                            if j in compl:
                                plotx('X',j)
                            
                                posit=j
                                presco.pos.append(posit)
                                delcompl(posit,compl)
                                presco.delforms(softy,posit)
                                presco.delforms(kile,posit)
                                proceed='true'
                                break
                elif presco.pos[1] in kl:
                    for  g in kl:
                        if g!=presco.pos[1]:
                            if g in compl:
                                plotx('X',g)
                                posit=g
                                proceed='true'
                                presco.pos.append(posit)
                                delcompl(posit,compl)
                                presco.delforms(softy,posit)
                                presco.delforms(kile,posit)
                                break                        
            if proceed=='true':
                break

presco.pos=presco.sort(presco.pos)                    
for inu in soft:
    if presco.pos==inu:
        print('I won')
        exit(0)

#---------------------------------------- USER INPUT-3

while posit not in compl:
    f1=win.getMouse()
    t=f1.getX()
    s=f1.getY()
    posit=position(s,t)
else:
    plotx('0',posit)
pres.pos.append(posit)
delcompl(posit,compl)
pres.delforms(queue,posit)
print('pres',pres.pos)
pres.delforms(kile,posit)

iota=check(pres.pos,soft,'0')    


#-------------------------------------------------------COMPUTER INPUT 4

prt=False
presco.sort(presco.pos)
for j in soft:
    if j==presco.pos:
        print('I won')
        exit(0)
    else:
        pres.sort(pres.pos)
        if j==pres.pos:
            print('you won')
            exit(0)
else:
    ml=[]
    count=0
    for msc in soft:
        print('in first for')
        if count=='0x98':
             break
        for ghy in msc:
            if ghy==presco.pos[0]:
                ml.append(ghy)
            elif ghy==presco.pos[1]:
                ml.append(ghy)
            elif ghy==presco.pos[2]:
                ml.append(ghy)
        if len(ml)==2:
            print('ml',ml)
            for ket in msc:
                if ket in compl:
                    posit=ket
                    _time.sleep(1)
                    plotx("X",posit)
                    presco.pos.append(posit)
                    delcompl(posit,compl)
                    presco.delforms(softy,posit)
                    presco.delforms(kile,posit)
                    count='0x98'
                    prt=True
                    break 
                else:
                    ml=[]
                            
        else:
            ml=[]
                
    else:
        ml=[]
        count=0
        pres.sort(pres.pos)
        if prt==False:
            
            for kaf in soft:
                if count=='0x98':
                    break
                print('in second for')
                for thy in kaf:
                    if count=='0x98':
                        break
                    if thy==pres.pos[0]:
                        ml.append(thy)
                    elif thy==pres.pos[1]:
                        ml.append(thy)
                    elif thy==pres.pos[2]:
                        ml.append(thy)
                if len(ml)==2:
                    for kete in kaf:
                        if kete in compl:
                            posit=kete
                            _time.sleep(1)
                            plotx('X',posit)
                            presco.pos.append(posit)
                            delcompl(posit,compl)
                            presco.delforms(softy,posit)
                            presco.delforms(kile,posit)
                            count='0x98'
                            break
                        else:
                            ml=[]
                            
                else:
                    ml=[]
if count!='0x98':
    pest=0
    lo=[]
    ml=[]
    for hu in soft:
        if count=='0x98':
            break
        for ku in hu:
            if count=='0x98':
                break
            if ku==presco.pos[0]:
                ml.append(ku)
            elif ku==presco.pos[1]:
                ml.append(ku)
            elif ku==presco.pos[2]:
                ml.append(ku)
        if len(ml)==1:
            for lu in hu:
                presco.sort(compl)
                if lu in compl:
                    pest+=1
                    lo.append(lu)
            if lu==2:
                plotx('X',lo[0])
                posit=lo[0]
                presco.pos.append(posit)
                delcompl(posit,compl)
                presco.delforms(softy,posit)
                presco.delforms(kile,posit)
                count='0x98'
                break
            else:
                lo=[]
                ml=[]
    
    else:
        presco.sort(compl)
        plotx('X',compl[0])
        posit=compl[0]
        presco.pos.append(posit)
        delcompl(posit,compl)
        presco.delforms(softy,posit)
        presco.delforms(kile,posit)
        count='0x98'
                
                    
            
iota=check(presco.pos,soft,'X')                            

#---------------------------------------------------------CHECKING

if count=='petra':
    print('you won')
else:
    count=True

#-------------------------------------------------------------USER  INPUT - 4

if count==True:
    
    while posit not in compl:
        f1=win.getMouse() 
        t=f1.getX()
        s=f1.getY()
        posit=position(s,t)
    else:
        plotx('0',posit)
    pres.pos.append(posit)
    delcompl(posit,compl)
    pres.delforms(queue,posit)
    print('pres',pres.pos)
    pres.delforms(kile,posit)

iota=check(pres.pos,soft,'0')    

#---------------------------------------------------COMPUTER - 5

ml=[]
for jpg in soft:
    for kilt in jpg:
        if kilt==presco.pos[0]:
            ml.append(kilt)
        elif kilt==presco.pos[1]:
            ml.append(kilt)
        elif kilt==presco.pos[2]:
            ml.append(kilt)
        elif kilt==presco.pos[3]:
            ml.append(kilt)
    if len(ml)==2:
        for pkl in jpg:
            if pkl in compl:
                _time.sleep(0.09)
                plotx('X',pkl)
                posit=pkl
            else:
                ml=[]
    else:
        ml=[]
else:
    plotx('X',compl[0])

iota=check(presco.pos,soft,'X') 
if len(compl)==1 and iota==False:
    print('draw')

   
print('end')
                
            
    
                        
                

