# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from Tkinter import *
import os
import webbrowser

class Window(Frame):
    
    def __init__(self, master = None):
        Frame.__init__(self, master, bg= 'black')
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Micromouse Project")
        self.pack(fill=BOTH, expand=1)
        StartButton = Button(self, text="Start", command = self.options, width = 50, bg = "white", font=("Helvetica", 10))
        StartButton.place(relx=0.5, rely=0.1, anchor=CENTER)
        QuitButton = Button(self, text="Quit", command = self.quit, width = 50, bg = "white", font=("Helvetica", 10))
        QuitButton.place(relx=0.5, rely=.9, anchor=CENTER)

        
    def options(self):
        StartButton = Button(self, text="Start", state = DISABLED, width = 50, bg = "white", font=("Helvetica", 10))
        StartButton.place(relx=0.5, rely=0.1, anchor=CENTER)
        
        DFButton = Button(self, text="Depth First", command = self.DepthFirst, width = 25, bg = "white", font=("Helvetica", 10))
        DFButton.place(relx=0.5, rely=0.33, anchor=CENTER)
        
        LHFButton = Button(self, text="Left Hand Follower", command = self.LeftHandFollower, width = 25, bg = "white", font=("Helvetica", 10))
        LHFButton.place(relx=0.5, rely=0.45, anchor=CENTER)
        
        RHButton = Button(self, text="Right Hand Follower", command = self.RightHandFollower , width = 25, bg = "white", font=("Helvetica", 10))
        RHButton.place(relx=0.5, rely=0.57, anchor=CENTER)
        
        WebButton = Button(root, text="Webpage", command = self.OpenUrl, width = 25, bg = "white", font=("Helvetica", 10))
        WebButton.place(relx=0.5, rely=.87, anchor=CENTER)
        
    def OpenUrl(self):
        webbrowser.open_new(url)
        
        
    def DepthFirst(self):
        os.system("python /home/jey/Documents/depth_first_main.py") 
        
    def LeftHandFollower(self):
        os.system("python /home/jey/Documents/leftwall_follower_main.py")
        
    def RightHandFollower(self):
        os.system("python /home/jey/Documents/rightwall_follower_main.py")
        
    def quit(self):
        exit()
        
root = Tk()
url = 'http://sensornetworks.engr.uga.edu/micro_mouse/pages/mouse1.html'
text = Text(root, height=1, width =31, bg = "black", fg = "white", font=("Helvetica", 16))
text.insert(INSERT, "CSEE 4240: Wireless Sensor Networks")
text.insert(END, "\n")
text.pack()

text1 = Text(root, height=20, width =75)
photo = PhotoImage(file='./georgia.gif')
#text1.insert(END,'')
text1.insert(INSERT,'')
text1.image_create(END, image=photo)
text1.pack(side = TOP)
root.geometry("700x600")
root.bind("<Escape>", lambda e: e.widget.quit())
app = Window(root)
root.configure(background='black')
root.mainloop()
