import os

class Mouse:
    xpos = 0
    ypos = 0
    x = 0
    y = 0
    idM = 0
    strx = 0
    stry = 0
    def __init__(self, xpos, ypos, idM):
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
        self.ypos = self.ypos - 23;
        os.system("coresendmsg node number="+str(self.idM)+" xpos="+str(self.xpos)+" ypos="+str(self.ypos))
    
    def backward(self):
        self.ypos = self.ypos + 23;
        os.system("coresendmsg node number="+str(self.idM)+" xpos="+str(self.xpos)+" ypos="+str(self.ypos))
    
    def right(self):
        self.xpos = self.xpos + 35;
        os.system("coresendmsg node number="+str(self.idM)+" xpos="+str(self.xpos)+" ypos="+str(self.ypos))
        
    def left(self):
        self.xpos = self.xpos - 35;
        os.system("coresendmsg node number="+str(self.idM)+" xpos="+str(self.xpos)+" ypos="+str(self.ypos))
