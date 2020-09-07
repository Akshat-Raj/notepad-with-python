import tkinter as tk
from tkinter import *
from tkinter import filedialog

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.file = tk.Button(self)
        self.file["text"] = "Save\n"
        self.file["width"] = 5
        self.file["command"] = self.File
        self.file.place(x=0,y=0)

        self.edit = tk.Button(self)
        self.edit["text"] = "Open\n"
        self.edit["width"] = 5
        self.edit["command"] = self.Edit
        print(self.file["width"])
        self.edit.place(x=48,y=0)
        

        self.format = tk.Button(self)
        self.format["text"] = "Format\n"
        self.format["width"] = 5
        self.format["command"] = self.Format
        self.format.place(x=96,y=0)

        self.view = tk.Button(self)
        self.view["text"] = "Dark\n"
        self.view["width"] = 5
        self.view["command"] = self.View
        self.view.pack(side="top")

        self.Text = tk.Text(self, height=700, width=500)
        self.Text.pack(side = "bottom")
        self.Text['font']=15
        self.m = Menu(root, tearoff = 0) 
        self.m.add_command(label ="Cut") 
        self.m.add_command(label ="Copy") 
        self.m.add_command(label ="Paste") 
        def do_popup(event): 
            try: 
                self.m.tk_popup(event.x_root, event.y_root) 
            finally: 
                self.m.grab_release() 
        self.Text.bind("<Button-3>", do_popup) 

    
  
    


    def File(self):
        input = self.Text.get("1.0","end-1c")
        file_name = filedialog.asksaveasfilename()
        f=open(file_name,"w")
        f.write(input)

    def Edit(self):
        file_name = filedialog.askopenfilename()
        f=open(file_name,"r")
        input=f.read()
        self.Text.delete("1.0","end-1c")
        self.Text.insert("1.0",input)

    def Format(self):
        self.Text.delete("1.0","end-1c")

    def View(self):
        if self.view['text']=="dark":
      	    self.view['text']="light"
      	    self.Text["bg"]="#303331"
      	    self.Text["fg"]="orange"
      	    self.Text["insertbackground"]="white"
        else:
        	self.Text["insertbackground"]="black"
        	self.view['text']="dark"
        	self.Text["bg"]="white"
        	self.Text["fg"]="black"

root = tk.Tk()
app = Application(master=root)
app.mainloop()