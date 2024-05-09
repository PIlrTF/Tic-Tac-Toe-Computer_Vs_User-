#the x and 0 game

'''----------------------------------------------------------_MODULE_--------------------------------------------------------------------------'''

from graphics import*

import time as _time

import random as _random

import math as _math



'''--------------------------------------------------------_FUNCTIONS_--------------------------------------------------------------'''

#RECTIFY THIS ERROR!!

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
                    print('You won')
                elif ch=='0' or ch=='o' or ch=='O':
                    print('Computer won the game')
                cvu=True
                return cvu
            else:
                ml=[]
    else:
        cvu=False
        return cvu

#########################################################################################                

def delcompl(n,compl):
    for i in range(len(compl)):
        if compl[i]==n:
            compl.pop(i)
            break
        
#########################################################################################        

def binsearch(item, listl):
    listl=sort(listl)
def delh(pres,item):
    for i in range(len(pres)):
        if pres[i]==item:
            pres.pop(i)
            break
        return pres
    
#########################################################################################################

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

##################################################################################################################

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
        
################################################################################################################

def drawgrid(flushit=False):
    if flushit==False:
        l1=Line(Point(0,100),Point(300,100))
        l1.draw(win)
        l2=Line(Point(0,200),Point(300,200))
        l2.draw(win)
        l3=Line(Point(100,0),Point(100,300))
        l3.draw(win)
        l4=Line(Point(200,0),Point(200,300))
        l4.draw(win)
        win.setBackground("turquoise")
    '''elif flushit==True:
        image=Image(Point(150,150),'yep3.png')

        image.draw(win)'''
        
        

##########################################################################################################

'''---------------------------------------------------------_CLASS - POST_---------------------------------------------------------------'''

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
                
    def findpos(self,soft,softy,queue,pres,pos,compl):        
        g=[]
        s=qw=0
        t=[]
        mapo=[]
        if len(pos)==1:            
            for i in soft:                
                for k in range(len(i)):                    
                    if i[k]==pres[0] :                       
                        g.append(i[k])                       
                    elif i[k]==pres[1]:                       
                        g.append(i[k])                        
                else:
                    if len(g)==2:                        
                        print('else',g)
                        s=list(i)
                        break
                    
                    else:                        
                        g=[]                       
            print(g)
            print(s)
            if s!=0:                
                for m in range(len(s)):                    
                    if g[0]==s[m] or g[1]==s[m]:                        
                        pass
                    
                    else:                        
                        for d in softy:                            
                            for  l in range(len(d)):
                                if d[l]==s[m]:                                  
                                    t.append(s[m])
                                    return t
                                
                            else:                                
                                t=[]
                else:                   
                    found=place=0                    
                    if t==[]:                        
                        for kt in queue:
                            print('insode for kt in queue')                            
                            if len(kt)>1:
                                for ms in range(len(kt)):
                                    if kt[ms]==pos[0]:
                                        found=kt[ms]
                                        place=list(kt)
                                        break
                                    
                                    else:                                        
                                        pass                                    
                        if found!=0 and place!=0:
                            _random.shuffle(place)                            
                            for i in place:                                
                                if i!=found:
                                    t.append(i)
                                    return t
                                
                            else:
                                print('compl')
                                _random.shuffle(compl)
                                t.append(compl[0])
                                print('t',t)
                                return t
                                                            
            elif g==[]:                
                for kt in queue:
                    print('insode for kt in queue')                    
                    if len(kt)>1:                        
                        for ms in range(len(kt)):                            
                            if kt[ms]==pos[0]:
                                found=kt[ms]
                                place=list(kt)
                                break
                            
                            else:
                                pass
                            
                if found!=0 and place!=0:
                    _random.shuffle(place)                    
                    for i in place:                        
                        if i!=found:
                            t.append(i)
                            return t
                
            else:
                print('compl')
                _random.shuffle(compl)
                t.append(compl[0])
                print('t',t)
                return t
        if len(pos)==2:
            prep=[]
            q=0
            for ket in soft:
                for kli in ket:
                    if kli==pos[0]:
                        prep.append(kli)
                    elif kli==pos[1]:
                        prep.append(kli)
                    else:
                        q=kli
                if len(prep)==2:
                    prep=[]
                    print('kli',q)
                    for lm in softy:
                        for hj in lm:
                            print('lrn:',len(lm))
                            if hj==q:
                                t.append(q)
                                #print('prep',prep)
                                print('m in fiest if')
                                return t
                     #else:
                         #elsepos(soft,softy,pres,pos,q)
                else:
                    prep=[]
                        
        if len(pos)==2:
            less=[]
            q=0
            for ip in soft:
                if ip==pres:
                    print('you won')
                    exit(0)
                else:
                    break
            for kam in soft:
                for pk in kam:
                    if pk==pres[0]:
                        less.append(pk)
                    elif pk==pres[1]:
                        less.append(pk)
                    elif pk==pres[2]:
                        less.append(pk)
                    else:
                        q=pk
                if len(less)==2:
                    print('q',q)
                    for men in softy:
                        for women in men:
                            if women==q:
                                t.append(women)
                                
                                print('less',less)
                                print('in women')
                                return t
                    else:
                        q=0
                        less=[]
                else:
                    q=0
                    less=[]
            else:
                dot=[]
                pest=[]
                lest=0
                count=False
                for it in queue:
                    if len(it)==3:
                        
                        for fg in it:
                            if fg==pos[0]:
                                count=True
                                pest.append(fg)
                                lest=it
                                break
                            elif fg==pos[1]:
                                count=True
                                lest=it
                                pest.append(fg)
                                break
                            else:
                                count='098'
                                pest=[]
                        if count==True:
                            print('count is true')
                            for pq in lest:
                                if pq==pest[0]:
                                    pass
                                else:
                                    dot.append(pq)
                        else:
                            pest=[]
                            lest=0
                        for qm in dot:
                            if qm in compl:
                                t.append(qm)
                                return t
                else:
                    return ['098']

    def third(self,soft,softy,pos,pres,compl):
        f=[]
        count=0
        petra=[]
        for i in soft:
            for j in range(len(i)):
                if pos[0]==i[j]:
                    f.append(i[0])
                elif pos[1]==i[j]:
                    f.append(i[1])
                elif pos[2]==i[j]:
                    f.append(i[2])
            else:
                if len(f)==2:
                    h=list(i)
                    count+=1
                    print(h)
                    for ku in h:
                        if ku not in pos:                            
                            if ku in compl:
                                return [ku]
                    else:
                        if count<len(soft):
                            f=[]
                            h=0
                        else:
                            pass                                   
                else:
                    f=[]
        else:
            f=[]
            for k in soft:
                for s in range(len(pres)):
                    if pres[s]==k[0]:
                        f.append(k[0])
                    elif pres[s]==k[1]:
                        f.append(k[1])
                    elif pres[s]==k[2]:
                        f.append(k[2])
                    else:
                        g=pres[s]
                        petra=k
                else:
                    if len(f)==2:
                        for mn in k:
                            if f[0]==mn or mn==f[1]:
                                pass
                            else:
                                if mn in compl:
                                    return [mn]                            
                        else:
                            f=[]
                    else:
                        f=[]           
            return '098'
                    
    def app(self,post,position):
        post.append(position)
        return post

    
    
#########################################################################################################

'''---------------------------------------------------_MAIN_------------------------------------------------------------------------------------'''
#__main__
    
#constants
triplet=[[7,5,9],[1,5,3],[1,5,7],[3,5,9]]
queue=[[1,2,3],[4,5,6],[7,8,9],[3,6,9],[1,4,7],[2,5,8],[1,5,9],[3,5,7]]
compl=[1,2,3,5,6,7,8,9,4]
soft=[[1,2,3],[4,5,6],[7,8,9],[3,6,9],[1,4,7],[2,5,8],[1,5,9],[3,5,7]]          #Remains constant throughout the program
softy= [[1,2,3],[4,5,6],[7,8,9],[3,6,9],[1,4,7],[2,5,8],[1,5,9],[3,5,7]]       # Will reduce as the game proceeds

'''--------------------------------------Building up the 1st part-------------------------------------------------------------'''

########################### DESIGNING GUI ############################################

p='0x4554433132'
win=GraphWin("Hello world",400,400)                               
win.setCoords(0,0,300,300)
drawgrid()
g="X"
q=n='0'

'''--------------------------------------Building up the 2nd part-------------------------------------------------------------'''

#--------------------------------->USER INPUT - 1
    
f1=win.getMouse()
t=f1.getX()
s=f1.getY()
posit=position(s,t)
pres=post()                                     #constructor of the class post
pres.app(pres.pos,posit)
plotx(g,posit)

for i in  range(len(compl)):
    if compl[i]==pres.pos[0]:
        compl.pop(i)
        break

pres.delforms(softy,posit)
pres.delforms(queue,posit)
print(softy)   


#---------------------------------------->COMP INPUT - 1

presco=post()
_random.shuffle(compl)
presco.app(presco.pos,compl[0])
_time.sleep(1)
plotx(q,compl[0])
presco.delforms(softy,compl[0])
compl.pop(0)
print(softy)

#------------------------------------->USER INPUT-2

while posit not in compl:       
    f1=win.getMouse()
    t=f1.getX()
    s=f1.getY()         
    posit=position(s,t)
else:
    plotx(g,posit)
pres.app(pres.pos,posit)
pres.delforms(softy,posit)
delcompl(posit,compl)
print(softy)
pres.delforms(queue,posit)
#-------------------------------------->COMP INPUT -2

b=presco.findpos(soft,softy,queue,pres.pos,presco.pos,compl)
print('b is : ',b)
_time.sleep(1)
plotx(n,b[0])
presco.delforms(softy,b[0])
delcompl(b[0],compl)
presco.app(presco.pos,b[0])

print(softy)    
print('queue',queue)
print(queue  is softy)

#-----------------------------------------> USER INPUT-3

while posit not in compl:       
    f1=win.getMouse()
    t=f1.getX()
    s=f1.getY()         
    posit=position(s,t)
else:
    plotx(g,posit)
delcompl(posit,compl)
pres.delforms(queue,posit)
pres.delforms(softy,posit)
pres.app(pres.pos,posit)
print(softy)
print('queue',queue)
cvu=True
pres.sort(pres.pos)
ch=g
iota=check(pres.pos,soft,ch)


#------------------------------------------>COMP INPUT-3

pres.sort(pres.pos)
print('pres',pres.pos)
presco.sort(presco.pos)
if (pres.pos==[1,6,8] or pres.pos==[3,4,8]) and (5 not in presco.pos) :
    _time.sleep(1)
    plotx(n,5)
    delcompl(5,compl)
    presco.app(presco.pos,5)
    presco.delforms(softy,5)
else:
    b=presco.findpos(soft,softy,queue,pres.pos,presco.pos,compl)
    _time.sleep(1)
    if b!=None and b[0]!='098':
        plotx(n,b[0])
        presco.delforms(softy,b[0])
        delcompl(b[0],compl)
        presco.app(presco.pos,b[0])
    else:
        _random.shuffle(compl)
        plotx(n,compl[0])
print('b',b)
cvu=False
presco.sort(presco.pos)
ch=n
iota=check(presco.pos,soft,ch)

#-----------------------------------------> USER INPUT-4

while posit not in compl:
    if iota==False:
       
        f1=win.getMouse()
        t=f1.getX()
        s=f1.getY()         
        posit=position(s,t)
    else:
        exit(0)
else:    
    plotx(g,posit)
    
delcompl(posit,compl)
pres.delforms(queue,posit)
pres.delforms(softy,posit)
pres.app(pres.pos,posit)
print(softy)
print('queue',queue)
cvu=True
pres.pos=pres.sort(pres.pos)
ch=g
iota=check(pres.pos,soft,ch)

#------------------------------------------>COMP INPUT-4

pres.sort(pres.pos)

b=presco.third(soft,softy,presco.pos,pres.pos,compl)
if b=='098' and iota==False:
    _random.shuffle(compl)
    _time.sleep(1)
    _time.sleep(1)
    plotx(n,compl[1])        
    presco.app(presco.pos,compl[1])
    presco.delforms(softy,compl[1])
    plotx(n,compl[1])
    delcompl(compl[1],compl)
    ch=n
    iota=check(presco.pos,soft,ch)
elif iota==True:
    exit(0)
   
elif b!='098' and iota==False:
    _time.sleep(1)
    plotx(n,b[0])    
    delcompl(b[0],compl)
    presco.app(presco.pos,b[0])
    presco.delforms(softy,b[0])
    ch=n
    iota=check(presco.pos,soft,ch)
elif iota==True:
    exit(0)
    
#------------------------------------------>USER INPUT-5

while posit not in compl:
    if iota==False:      
        f1=win.getMouse()
        t=f1.getX()
        s=f1.getY()         
        posit=position(s,t)
    else:
        exit(0)
else:    
    plotx(g,posit)
    delcompl(posit,compl)
pres.delforms(queue,posit)
pres.delforms(softy,posit)
pres.app(pres.pos,posit)
print(softy)
print('queue',queue)
pres.pos=pres.sort(pres.pos)
ch=g
iota=check(pres.pos,soft,ch)

    
if len(compl)==0 and iota==False:
    print('DRAW')


drawgrid(flushit=True)



                

        
