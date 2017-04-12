from random import *
from Tkinter import *
import os
import time

width=500
height=500

def occupied(x,y,x1,y1,x2,y2,x3,y3):
	if(x==x1 and y==y1):
		return True
	elif(x==x2 and y==y2):
		return True
	elif(x==x3 and y==y3):
		return True
	else:
		return False



def rightFollow(mouse,x1,y1,x2,y2,x3,y3):
	if(mouse.direc=="up"):
		if(arr[mouse.y][mouse.x+1]):
			mouse.direc="right"
			mouse.right()
		elif(arr[mouse.y-1][mouse.x]):
			mouse.forward()
		else:
			mouse.direc="left"
			if(arr[mouse.y][mouse.x-1]):
				mouse.left()
			
	elif(mouse.direc=="down"):
		if(arr[mouse.y][mouse.x-1]):
			mouse.direc="left"
			mouse.left()
		elif(arr[mouse.y+1][mouse.x]):
			mouse.backward()
		else:
			mouse.direc="right"
			if(arr[mouse.y][mouse.x+1]):
				mouse.right()
			
	elif(mouse.direc=="left"):
		if(arr[mouse.y-1][mouse.x]):
			mouse.direc="up"
			mouse.forward()
		elif(arr[mouse.y][mouse.x-1]):
			mouse.left()
		else:
			mouse.direc="down"
			if(arr[mouse.y+1][mouse.x]):
				mouse.backward()
			
	elif(mouse.direc=="right"):
		if(arr[mouse.y+1][mouse.x]):
			mouse.direc="down"
			mouse.backward()
		elif(arr[mouse.y][mouse.x+1]):
			mouse.right()
		else:
			mouse.direc="up"
			if(arr[mouse.y-1][mouse.x]):
				mouse.forward()
			
def updateMaze(mouse):
	mouse.map[mouse.y][mouse.x]=1
	mouse.map[mouse.y][mouse.x+1]=arr[mouse.y][mouse.x+1]
	mouse.map[mouse.y+1][mouse.x]=arr[mouse.y+1][mouse.x]
	mouse.map[mouse.y][mouse.x-1]=arr[mouse.y][mouse.x-1]
	mouse.map[mouse.y-1][mouse.x]=arr[mouse.y-1][mouse.x]

def updateCanvas(mous1,mous2,mous3,mous4):
	combArr = []
	for num in range(0,33):
		combArr.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
	for num1 in range(0,33):
		for num2 in range(0,33):
			if(mous1.map[num1][num2]==1):
				combArr[num1][num2]=1
			elif(mous2.map[num1][num2]==1):
				combArr[num1][num2]=1
			elif(mous3.map[num1][num2]==1):
				combArr[num1][num2]=1
			elif(mous4.map[num1][num2]==1):
				combArr[num1][num2]=1
	for row in range(0, 33):
		for col in range(0, 33):
			x = (col - 1) * side
			y = (row - 1) * side
			if(row==mous1.y and col==mous1.x):
				drawSquare(canvas, x, y, side, 'yellow')
			elif(row==mous2.y and col==mous2.x):
				drawSquare(canvas, x, y, side, 'blue')
			elif(row==mous3.y and col==mous3.x):
				drawSquare(canvas, x, y, side, 'black')
			elif(row==mous4.y and col==mous4.x):
				drawSquare(canvas, x, y, side, 'green')
            		elif(combArr[row][col]):
                		drawSquare(canvas, x, y, side, 'white')
            		else:
                		drawSquare(canvas, x, y, side, 'red')
    	canvas.update()

def drawSquare(canvas, x, y, side, color):
    id = canvas.create_rectangle(x, y, x + side, y + side, fill=color)
    return id


class Mouse:
    xpos = 0
    ypos = 0
    x = 0
    y = 0
    idM = 0
    strx = 0
    stry = 0
    visitedX=[]
    visitedY=[]
    path=[]
    centerx = 0
    centery = 0
    direc = "up"
    def __init__(self, xpos, ypos, idM):
	os.system("coresendmsg node number="+str(idM)+" xpos="+str(xpos)+" ypos="+str(ypos))        
	self.xpos = xpos
        self.ypos = ypos
        self.idM = idM
        self.strx= xpos
        self.stry= ypos
	self.map= []
	for num in range(0,33):
		self.map.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
	
        if idM==1:
            self.x=1
            self.y=1
	    self.centerx = 15
	    self.centery = 15
        elif idM==2:
            self.x=31
            self.y=1
	    self.centerx = 16
	    self.centery = 15
        elif idM==3:
            self.x=1
            self.y=31
	    self.centerx = 15
	    self.centery = 16
        else:
            self.x=31
            self.y=31
	    self.centerx = 17
	    self.centery = 17
    def forward(self):
        self.ypos = self.ypos - 24;
	self.y = self.y - 1;	
        os.system("coresendmsg node number="+str(self.idM)+" xpos="+str(self.xpos)+" ypos="+str(self.ypos))
    
    def backward(self):
        self.ypos = self.ypos + 24;
	self.y = self.y + 1;
        os.system("coresendmsg node number="+str(self.idM)+" xpos="+str(self.xpos)+" ypos="+str(self.ypos))
    
    def right(self):
        self.xpos = self.xpos + 36;
	self.x = self.x + 1;
        os.system("coresendmsg node number="+str(self.idM)+" xpos="+str(self.xpos)+" ypos="+str(self.ypos))
	#print("x: "+str(self.xpos)+" y: "+str(self.ypos))
        
    def left(self):
        self.xpos = self.xpos - 36;
	self.x = self.x - 1;
        os.system("coresendmsg node number="+str(self.idM)+" xpos="+str(self.xpos)+" ypos="+str(self.ypos))

class Mouse1:
    xpos = 0
    ypos = 0
    x = 0
    y = 0
    idM = 0
    strx = 0
    stry = 0
    visitedX=[]
    visitedY=[]
    path=[]
    centerx = 0
    centery = 0
    direc = "up"
    def __init__(self, xpos, ypos, idM):
	os.system("coresendmsg node number="+str(idM)+" xpos="+str(xpos)+" ypos="+str(ypos))        
	self.xpos = xpos
        self.ypos = ypos
        self.idM = idM
        self.strx= xpos
        self.stry= ypos
	self.map= []
	for num in range(0,33):
		self.map.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        if idM==1:
            self.x=1
            self.y=1
	    self.centerx = 15
	    self.centery = 15
        elif idM==2:
            self.x=31
            self.y=1
	    self.centerx = 16
	    self.centery = 15
        elif idM==3:
            self.x=1
            self.y=31
	    self.centerx = 15
	    self.centery = 16
        else:
            self.x=31
            self.y=31
	    self.centerx = 17
	    self.centery = 17
    def forward(self):
        self.ypos = self.ypos - 24;
	self.y = self.y - 1;	
        os.system("coresendmsg node number="+str(self.idM)+" xpos="+str(self.xpos)+" ypos="+str(self.ypos))
    
    def backward(self):
        self.ypos = self.ypos + 24;
	self.y = self.y + 1;
        os.system("coresendmsg node number="+str(self.idM)+" xpos="+str(self.xpos)+" ypos="+str(self.ypos))
    
    def right(self):
        self.xpos = self.xpos + 36;
	self.x = self.x + 1;
        os.system("coresendmsg node number="+str(self.idM)+" xpos="+str(self.xpos)+" ypos="+str(self.ypos))
	#print("x: "+str(self.xpos)+" y: "+str(self.ypos))
        
    def left(self):
        self.xpos = self.xpos - 36;
	self.x = self.x - 1;
        os.system("coresendmsg node number="+str(self.idM)+" xpos="+str(self.xpos)+" ypos="+str(self.ypos))

class Mouse2:
    xpos = 0
    ypos = 0
    x = 0
    y = 0
    idM = 0
    strx = 0
    stry = 0
    visitedX=[]
    visitedY=[]
    path=[]
    centerx = 0
    centery = 0
    direc = "up"
    def __init__(self, xpos, ypos, idM):
	os.system("coresendmsg node number="+str(idM)+" xpos="+str(xpos)+" ypos="+str(ypos))        
	self.xpos = xpos
        self.ypos = ypos
        self.idM = idM
        self.strx= xpos
        self.stry= ypos
	self.map= []
	for num in range(0,33):
		self.map.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        if idM==1:
            self.x=1
            self.y=1
	    self.centerx = 15
	    self.centery = 15
        elif idM==2:
            self.x=31
            self.y=1
	    self.centerx = 17
	    self.centery = 15
        elif idM==3:
            self.x=1
            self.y=31
	    self.centerx = 15
	    self.centery = 16
        else:
            self.x=31
            self.y=31
	    self.centerx = 17
	    self.centery = 17
    def forward(self):
        self.ypos = self.ypos - 24;
	self.y = self.y - 1;	
        os.system("coresendmsg node number="+str(self.idM)+" xpos="+str(self.xpos)+" ypos="+str(self.ypos))
    
    def backward(self):
        self.ypos = self.ypos + 24;
	self.y = self.y + 1;
        os.system("coresendmsg node number="+str(self.idM)+" xpos="+str(self.xpos)+" ypos="+str(self.ypos))
    
    def right(self):
        self.xpos = self.xpos + 36;
	self.x = self.x + 1;
        os.system("coresendmsg node number="+str(self.idM)+" xpos="+str(self.xpos)+" ypos="+str(self.ypos))
	#print("x: "+str(self.xpos)+" y: "+str(self.ypos))
        
    def left(self):
        self.xpos = self.xpos - 36;
	self.x = self.x - 1;
        os.system("coresendmsg node number="+str(self.idM)+" xpos="+str(self.xpos)+" ypos="+str(self.ypos))

class Mouse3:
    xpos = 0
    ypos = 0
    x = 0
    y = 0
    idM = 0
    strx = 0
    stry = 0
    visitedX=[]
    visitedY=[]
    path=[]
    centerx = 0
    centery = 0
    direc = "up"
    def __init__(self, xpos, ypos, idM):
	os.system("coresendmsg node number="+str(idM)+" xpos="+str(xpos)+" ypos="+str(ypos))        
	self.xpos = xpos
        self.ypos = ypos
        self.idM = idM
        self.strx= xpos
        self.stry= ypos
	self.map= []
	for num in range(0,33):
		self.map.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        if idM==1:
            self.x=1
            self.y=1
	    self.centerx = 15
	    self.centery = 15
        elif idM==2:
            self.x=31
            self.y=1
	    self.centerx = 16
	    self.centery = 15
        elif idM==3:
            self.x=1
            self.y=31
	    self.centerx = 15
	    self.centery = 17
        else:
            self.x=31
            self.y=31
	    self.centerx = 17
	    self.centery = 17
    def forward(self):
        self.ypos = self.ypos - 24;
	self.y = self.y - 1;	
        os.system("coresendmsg node number="+str(self.idM)+" xpos="+str(self.xpos)+" ypos="+str(self.ypos))
    
    def backward(self):
        self.ypos = self.ypos + 24;
	self.y = self.y + 1;
        os.system("coresendmsg node number="+str(self.idM)+" xpos="+str(self.xpos)+" ypos="+str(self.ypos))
    
    def right(self):
        self.xpos = self.xpos + 36;
	self.x = self.x + 1;
        os.system("coresendmsg node number="+str(self.idM)+" xpos="+str(self.xpos)+" ypos="+str(self.ypos))
	#print("x: "+str(self.xpos)+" y: "+str(self.ypos))
        
    def left(self):
        self.xpos = self.xpos - 36;
	self.x = self.x - 1;
        os.system("coresendmsg node number="+str(self.idM)+" xpos="+str(self.xpos)+" ypos="+str(self.ypos))

file = open("maze.txt", 'r')
arr = []
for line in file.readlines():
    arr1 = []
    for c in line:
        if(c.isspace() and (c!="\n")):
            arr1.append(1)
        elif(c!="\n"):
            arr1.append(0)
    arr.append(arr1)

window = Tk()
canvas = Canvas(window, width=width, height=height)
canvas.pack()
side = width / (len(arr)-2)

#for row in arr:
    #print(row)

#visitedX=[]
#visitedY=[]
#path=[]
mouse1 = Mouse(42, 25, 1)
mouse1.direc="up"
mouse2 = Mouse2(1122,25,2)
mouse2.direc="right"
mouse3 = Mouse3(42, 745,3)
mouse3.direc="left"
mouse4 = Mouse1(1122, 745, 4)
mouse4.direc="down"
while(1):
	mouse1.visitedX.append(mouse1.x)
	mouse1.visitedY.append(mouse1.y)
	mouse4.visitedX.append(mouse4.x)
	mouse4.visitedY.append(mouse4.y)
	mouse2.visitedX.append(mouse2.x)
	mouse2.visitedY.append(mouse2.y)
	mouse3.visitedX.append(mouse3.x)
	mouse3.visitedY.append(mouse3.y)

	updateMaze(mouse1)
	updateMaze(mouse2)
	updateMaze(mouse3)
	updateMaze(mouse4)
	updateCanvas(mouse1,mouse2,mouse3,mouse4)
	#time.sleep(0.25)
	if(mouse1.x==mouse1.centerx and mouse1.y==mouse1.centery and mouse2.x==mouse2.centerx and mouse2.y==mouse2.centery and mouse3.x==mouse3.centerx and mouse3.y==mouse3.centery and mouse4.x==mouse4.centerx and mouse4.y==mouse4.centery):
		break
	else:
		rightFollow(mouse1,mouse2.x,mouse2.y,mouse3.x,mouse3.y,mouse4.x,mouse4.y)
		rightFollow(mouse2,mouse1.x,mouse1.y,mouse3.x,mouse3.y,mouse4.x,mouse4.y)
		rightFollow(mouse3,mouse2.x,mouse2.y,mouse1.x,mouse1.y,mouse4.x,mouse4.y)
		rightFollow(mouse4,mouse2.x,mouse2.y,mouse3.x,mouse3.y,mouse1.x,mouse1.y)	
	'''elif(arr[mouse1.y][mouse1.x+1] and inVisited(mouse1.visitedX,mouse1.visitedY,mouse1.x+1,mouse1.y)):		
		mouse1.right()
		mouse1.path.append("right")
	elif(arr[mouse1.y+1][mouse1.x] and inVisited(mouse1.visitedX,mouse1.visitedY,mouse1.x,mouse1.y+1)):
		mouse1.backward()
		mouse1.path.append("down")
	elif (arr[mouse1.y][mouse1.x-1] and inVisited(mouse1.visitedX,mouse1.visitedY,mouse1.x-1,mouse1.y)):
		mouse1.left()
		mouse1.path.append("left")
	elif(arr[mouse1.y-1][mouse1.x] and inVisited(mouse1.visitedX,mouse1.visitedY,mouse1.x,mouse1.y-1)):
		mouse1.forward()
		mouse1.path.append("up")
	else:
		reverse(mouse1.path,mouse1)'''
combArr = []
for num in range(0,33):
	combArr.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
for num1 in range(0,33):
	for num2 in range(0,33):
		if(mouse1.map[num1][num2]==1):
			combArr[num1][num2]=1
		elif(mouse2.map[num1][num2]==1):
			combArr[num1][num2]=1
		elif(mouse3.map[num1][num2]==1):
			combArr[num1][num2]=1
		elif(mouse4.map[num1][num2]==1):
			combArr[num1][num2]=1
print("mapped array")
for row in combArr:
	print(row)

window.mainloop()
#for num in range(0,31):
#	time.sleep(0.25)
#	mouse1.right()
#for num in range(0,10):
#	print(arr[num][1])
