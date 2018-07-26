"""
Created on Thu Jul 26 09:24:59 2018

@author: haithama
"""
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import messagebox
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from scipy import signal
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import Tk


def square(list):
    return [i ** 2 for i in list]

# define a function for square root calculation
def sqrtList(list):
    return [j ** (1/2) for j in list]


def display_1():
    txt = tkvar.get()
    if (txt == "None"):
        messagebox.showinfo("Make a selsction", "Please make a selection")
        txt = tkvar.get()
    elif (txt == "Acceleration in X dir"):
        win1 = tk.Toplevel(bg='white')
        win1.title('top/child window win1')
        win1.geometry("450x300")
        fig = Figure(figsize=(6,6))
        a = fig.add_subplot(111)
        a.plot(accX)
        a.set_title ("Acceleration in X dir", fontsize=16)
        a.set_ylabel("velocity", fontsize=14)
        a.set_xlabel("time", fontsize=14)
        a.invert_yaxis()
        canvas = FigureCanvasTkAgg(fig, win1)
        canvas.get_tk_widget().pack()
        canvas.draw()
        txt = tkvar.get()
    elif (txt == "Acceleration in Y dir"):
        win1 = tk.Toplevel(bg='white')
        win1.title('top/child window win1')
        win1.geometry("450x300")
        fig = Figure(figsize=(6,6))
        a = fig.add_subplot(111)
        a.plot(accY)
        a.set_title ("Acceleration in Y dir", fontsize=16)
        a.set_ylabel("velocity", fontsize=14)
        a.set_xlabel("time", fontsize=14)
        a.invert_yaxis()
        canvas = FigureCanvasTkAgg(fig, win1)
        canvas.get_tk_widget().pack()
        canvas.draw()
        txt = tkvar.get()
    elif (txt == "Acceleration in Z dir"):
        win1 = tk.Toplevel(bg='white')
        win1.title('top/child window win1')
        win1.geometry("450x300")
        fig = Figure(figsize=(6,6))
        a = fig.add_subplot(111)
        a.plot(accZ)
        a.set_title ("Acceleration in Z dir", fontsize=16)
        a.set_ylabel("velocity", fontsize=14)
        a.set_xlabel("time", fontsize=14)
        a.invert_yaxis()
        canvas = FigureCanvasTkAgg(fig, win1)
        canvas.get_tk_widget().pack()
        canvas.draw()
        txt = tkvar.get()
        

def display_2():
        Lb = Label(root, text=len(peakind))
        Lb.grid(column=2, row=4)


messagebox.showinfo("Read this note please",\
                    "This code is for steps calculation\n\
                    Steps to run the app: \n\
                    1. Locate your excel or csv file, this data is \n\
                    collected from PowerSense iOS App \n\
                    2. be sure that your data are in the first sheet \n\
                    3. (optional) select acceleration data to display \n\
                    4. Click on Calculate steps botton \n\
                    Enjoy! ")

filename = askopenfilename(initialdir = "C:/",title = "choose your file",\
                           filetypes = (("Excel file","*.xls"),("CSV file","\
                                        *.csv"),("all files","*.*")))

root = Tk()
root.title("Steps Calc App")
root.minsize(300,100)
root.geometry("320x100")

# Load the xls data, and use Sheet3
loc = filename
file = pd.ExcelFile(loc)
sheets = file.sheet_names
df = file.parse(sheets[0])

#Extract the acceleration data and save them to seperate lists
accX = df['user_acc_x(G)']
accY = df['user_acc_y(G)']
accZ = df['user_acc_z(G)']

# determining the magnitude of the acceleration data in 3 axises     
accT = list(np.array(square(accX)) + np.array(square(accY)) + np.array(square\
            (accY)))
Mag = sqrtList(accT)
# plot the magnitude
plt.plot(Mag, 'g')
plt.xlabel('time')
plt.ylabel('velocity')
plt.title('Acceleration data magnitude')
plt.legend()
plt.show()

# finding the number of steps
peakind = signal.find_peaks_cwt(Mag, np.arange(1,len(Mag)))

print("Number of steps = ", len(peakind))

# Create a Tkinter variable
tkvar = StringVar(root)
 
# Dictionary with options
choices = { 'None','Acceleration in X dir','Acceleration in Y dir',\
           'Acceleration in Z dir'}
tkvar.set('None') # set the default option
 
popupMenu = OptionMenu(root, tkvar, *choices)
Label(root, text="Choose acceleration direction to display").grid(row = 2, \
     column = 1)
popupMenu.grid(row =3 , column =1)

# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )

txt = tkvar.get()
# link function to change dropdown
tkvar.trace('w', change_dropdown)

btn_1 = Button(root, text = "Display plot", command = display_1)
btn_1.grid(column=2, row=3)

btn_2 = Button(root, text = "Calculate steps", command = display_2)
btn_2.grid(column=1, row=4)

root.mainloop()

#root.mainloop()