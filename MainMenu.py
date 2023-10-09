from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import winsound, WorldGen, os, LivePlayer

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("DaftCity 2000©")

        self.style = Style(master)
        self.style.configure("TLabel", font=("Calibri", 12), anchor=CENTER, padding=10)
        self.style.configure("TButton",padding=10, font=("Calibri", 12))

        self.frame = Frame(master, padding=(5,5,5,10))
        self.frame.grid()
        self.create_widgets()

    def create_widgets(self):
        winsound.PlaySound('C:/Users/Tristan/Desktop/A Level and Programming/A-Level/A-Level compsci/ProgrammingProject/Music/Welcome.wav', winsound.SND_ASYNC)
        main_label=Label(self.frame, text="DaftCity 2000")
        main_label.grid(row=0, sticky=EW, pady=10)

        button1 = Button(self.frame, width=30, text="New Game", command=self.window1)
        button1.grid(row=1, sticky=EW)

        button2 = Button(self.frame, width=30, text="Load Game", command=self.window2)
        button2.grid(row=2, sticky=EW)

    def window1(self):
        self.master.withdraw()
        self.window1 = Window1(self.master)
    
    def window2(self):
        self.master.withdraw()
        self.window2 = Window2(self.master)
    

class Window1:
    def __init__(self, master):
        self.master = master
        self.window1 = Toplevel(master)
        self.window1.title("New Game")
        self.window1.protocol("WM_DELETE_WINDOW", self.Main_Window)

        self.frame = Frame(self.window1, padding=(5,5,5,10))
        self.frame.grid()
        self.create_widgets()

    def create_widgets(self):
        LoginLabel = Label(self.frame, width=30, text="Name of your world")
        LoginLabel.grid(row=1, column=0, sticky=EW)
    
        LoginLabel2 = Label(self.frame, width=30, text="Size of your world (X x Y)")
        LoginLabel2.grid(row=2, column=0, sticky=EW)

        global Entry1
        Entry1 = Entry(self.frame, width=30, text="Name of your world")
        Entry1.grid(row=1, column=1,sticky=EW)

        global Entry2
        Entry2 = Entry(self.frame, width=30,text="Size of your World")
        Entry2.grid(row=2, column=1,sticky=EW)

        SignIn = Button(self.frame, width=30, text="Create!", command=self.second_window)
        SignIn.grid(row=3, columnspan=2, sticky=EW)

        Exit = Button(self.frame, width=30, text="Cancel", command=self.Main_Window)
        Exit.grid(row=4, columnspan=2,sticky=EW)
        exitStyle = Style(Exit)

    def Main_Window(self):
        self.window1.destroy()
        self.master.deiconify()
    
    def second_window(self):
        global Entry1
        global Entry2
        if int(Entry2.get()) >= 10 and int(Entry2.get()) <= 50:
            WorldGen.createWorldFile(int(Entry2.get()), int(Entry2.get()), Entry1.get())
            WorldGen.createRivers(f"C:/Users/Tristan/Desktop/A Level and Programming/A-Level/A-Level compsci/ProgrammingProject/PlayerWorlds/{Entry1.get()}/{Entry1.get()}#WORLD.txt")
            WorldGen.createFoliage(f"C:/Users/Tristan/Desktop/A Level and Programming/A-Level/A-Level compsci/ProgrammingProject/PlayerWorlds/{Entry1.get()}/{Entry1.get()}#WORLD.txt", Entry1.get())
            self.window1.destroy()
            self.window2 = Window2(self.master)
        else:
            messagebox.showinfo("Error!", "Your size needs to be between 10 and 50")


class Window2:
    def __init__(self, master):
        self.master = master
        self.window2 = Toplevel(master)
        self.window2.title("Load a world")
        self.window2.protocol("WM_DELETE_WINDOW", self.Main_Window)

        self.frame = Frame(self.window2, padding=(5,5,5,10))
        self.frame.grid()
        self.create_widgets()

    def create_widgets(self):
        LoginLabel = Label(self.frame, width=30, text="Enter your World Name")
        LoginLabel.grid(row=1, column=0, sticky=EW)

        global Entry1
        Entry1 = Entry(self.frame, width=30, text="world name")
        Entry1.grid(row=1, column=1,sticky=EW)

        SignIn = Button(self.frame, width=30, text="Load", command=self.Window_One)
        SignIn.grid(row=4, columnspan=2, sticky=EW)

        Exit = Button(self.frame, width=30, text="Cancel", command=self.Main_Window)
        Exit.grid(row=5, columnspan=2,sticky=EW)

    def Main_Window(self):
        print("Exited")
        self.window2.destroy()
        self.master.deiconify()

    def Window_One(self):
        global Entry1
        LivePlayer.renderWorld(Entry1.get())
        
root = Tk()
app = App(root)
root.mainloop()