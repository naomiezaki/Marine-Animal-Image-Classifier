# Import libraries and functions
import tkinter as tk
import os
from tkinter import *
from tkinter import ttk
from PIL import ImageTk

from retrain import startRetrain
from test import startTest

HEIGHT = 300
WIDTH = 350

# Create Instance
windows = tk.Tk()

# Add a title to GUI
windows.title("Marine Animal Image Classifier")

frame = tk.Frame(windows)
frame.pack()

#set canvas size
canvas = tk.Canvas(windows, height=HEIGHT, width=WIDTH)
canvas.pack()

image = ImageTk.PhotoImage(file = os.getcwd() +"/assets/ocean-background.png")
canvas.create_image(0, 0, image = image, anchor = NW)

# Put "False" to make non-resizable
windows.resizable(False, False)

#tk.[widgetname](root window, properties/cofiguration)

#TITLE
label = tk.Label(windows, text="Marine Animal \n Image Classifier", font="Helvetica 18 bold")
label.place(anchor='s', relx=0.5, rely=0.2)

#When Retrain button is clicked, retrain process starts
retrain_button = tk.Button(windows, text="Retrain", bg='#ff6600', command=startRetrain)
retrain_button.place(anchor='s', relx=0.5, rely=0.4)

#when Test button is clicked, test process starts
test_button = tk.Button(windows, text="Test", bg='#ff6600', command=startTest)
test_button.place(anchor='s', relx=0.5, rely=0.5)

# perform(tk, windows)

# Start the GUI/Create the main loop
windows.mainloop()