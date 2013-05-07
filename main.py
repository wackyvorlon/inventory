

from Tkinter import *


class App:
	"""A simple inventory app."""
	def __init__(self, arg):
		super(App, self).__init__()
		self.arg = arg

		frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
    	print "Hello, world!"


root = Tk()

app = App(root)

root.mainloop()
