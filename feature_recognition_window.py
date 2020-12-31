from tkinter import Tk, RIGHT, BOTTOM, TOP, mainloop
from tkinter.ttk import Button
import feature_options as fo
import math

ret = None

class quit_button(Button):
	def __init__(self, parent):
		Button.__init__(self, parent)
		self['text'] = 'Quit'
		# Command to close the window (the destory method)
		self['command'] = parent.destroy
		self.pack(side=RIGHT)

def button_press(fn, *args):
	global ret 
	ret = fn(*args)

def get_ret():
	return ret

def func():
	master = Tk() 
	master.title("Feature Recognition")

	frame = Frame(master)
	frame.pack(side = BOTTOM)

	label = Label(master, text = "Please decide on which feature you want to recognize") 
	label.pack(pady = 10) 

	quit_button(master)

	def onclick(args):
		for feat in fo.features: 
			if feat.name == args:
				return fo.recog_features[feat]

	feature_names = [i.name for i in fo.features]
	buttons_list = []
	for name in feature_names: 
		button = Button(frame, text=name, command=lambda name=name: button_press(onclick, name))
		button.pack(side=TOP, pady=1, padx=10)
		buttons_list.append(button)

	mainloop() 