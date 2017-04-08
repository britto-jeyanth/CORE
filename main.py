import os
import time

def inVisited(visitX, visitY, x, y):
	for num in range(1,len(visitX)):
		if(x==visitX[num-1] and y==visitY[num-1]):
			return 0
	return 1

def reverse(path1,mouse):
	last = path1.pop()
	if(last=="up"):
		mouse.backward()
	elif(last=="down"):
		mouse.forward()
	elif(last=="right"):
		mouse.left()
	elif(last=="left"):
		mouse.right()
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
    def __init__(self, xpos, ypos, idM):
	os.system("coresendmsg node number="+str(idM)+" xpos="+str(xpos)+" ypos="+str(ypos))        
	self.xpos = xpos
        self.ypos = ypos
        self.idM = idM
        self.strx= xpos
        self.stry= ypos
        if idM==1:
            self.x=1
            self.y=1
        elif idM==2:
            self.x=31
            self.y=1
        elif idM==3:
            self.x=1
            self.y=31
        else:
            self.x=31
            self.y=31
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
#for row in arr:
    #print(row)

#visitedX=[]
#visitedY=[]
#path=[]
mouse1 = Mouse(42, 25, 1)
while(1):
	mouse1.visitedX.append(mouse1.x)
	mouse1.visitedY.append(mouse1.y)
	time.sleep(0.25)
	if(mouse1.x==15 and mouse1.y==15):
		break	
	elif(arr[mouse1.y][mouse1.x+1] and inVisited(mouse1.visitedX,mouse1.visitedY,mouse1.x+1,mouse1.y)):		
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
		reverse(mouse1.path,mouse1)
	
#for num in range(0,31):
#	time.sleep(0.25)
#	mouse1.right()
#for num in range(0,10):
#	print(arr[num][1])
