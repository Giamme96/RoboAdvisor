from tkinter import *
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from matplotlib.figure import Figure as fig
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as figcan


master = Tk()

Label(text="one").pack()

separator = Frame(height=2, bd=10, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

Label(text="two").pack()

frames = Frame()
x = [1, 2, 3, 4, 5]

y = [150, 155, 200, 220, 180]
plt.plot(x,y)
#plt.show()


mainloop()