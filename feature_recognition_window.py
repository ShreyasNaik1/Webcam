from tkinter import *
from tkinter.ttk import *
import feature_options as fo
import math

master = Tk() 
master.title("Feature Recognition")

frame = Frame(master)
frame.pack(side = BOTTOM)

label = Label(master, text = "Please decide on which feature you want to recognize") 
label.pack(pady = 10) 


class quitButton(Button):
    def __init__(self, parent):
        Button.__init__(self, parent)
        self['text'] = 'Quit'
        # Command to close the window (the destory method)
        self['command'] = parent.destroy
        self.pack(side=RIGHT)

quitButton(master)


def return_path(name):
	for feat in fo.features: 
		if feat.name == name:
			return fo.recog_features[feat]

feature_names = [i.name for i in fo.features]
buttons_list = []
for name in feature_names: 
	button = Button(frame, text=name, command=return_path(name))
	button.pack(side=TOP, pady=1, padx=10)
	buttons_list.append(button)


mainloop() 