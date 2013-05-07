#!/usr/bin/env python

from Tkinter import *

root = Tk()

w = Label(root, text="Hello, world!")
w.pack()

root.mainloop()

class App(object):
	"""docstring for App"""
	def __init__(self, arg):
		super(App, self).__init__()
		self.arg = arg
		