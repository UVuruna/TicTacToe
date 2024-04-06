import tkinter as tk

class View(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("TicTacToe")
        self.minsize(640,480)

class TableFrame(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)

class AnalyzeFrame(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)

class OptionsFrame(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)

if __name__=='__main__':
    a = View()
    a.mainloop()