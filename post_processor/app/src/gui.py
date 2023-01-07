
import tkinter as tk
from tkinter import *

class GUI():

	tkroot = None # Tkinter root object
	r = None # top/root
	w = None # window

	ready = False

# ================================================================================ #
# Initialize Graphics Object
# ================================================================================ #

	def __init__(self,root):
		print('[ TRY  ] GUI initialized.')
		self.r = root
		self.tkroot = tk.Tk()
		self.top = self.setup(self.tkroot)
		photo = PhotoImage(file = "icon.png")
		self.tkroot.iconphoto(False, photo)

		self.tkroot.protocol("WM_DELETE_WINDOW", self.onClose)
		self.tkroot.resizable(False, False)

		print('[ OKAY ] GUI initialized.')

	def onClose(self):
		self.r.exit()

	def update(self):
		try:
			self.tkroot.update_idletasks()
			self.tkroot.update()
		except Exception as e:
			print('[ ERR ] Exception caught in canvas update: ' + str(e))

		try:
			
			self.ready = True

		except Exception as e:
			print('[ ERR ] Exception caught in graphics update: ' + str(e))



# ================================================================================ #
# Setup Graphics
# ================================================================================ #

	def setup(self, top=None):

		'''This class configures and populates the toplevel window.
		   top is the toplevel containing window.'''
		_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
		_fgcolor = '#000000'  # X11 color: 'black'
		_compcolor = '#d9d9d9' # X11 color: 'gray85'
		_ana1color = '#d9d9d9' # X11 color: 'gray85'
		_ana2color = '#ececec' # Closest X11 color: 'gray92'

		top.geometry("400x200")
		# top.minsize(130, 10)
		# top.maxsize(5150, 1071)
		# top.resizable(1,  1)
		top.title("CPB Loop Post Processor")
		top.configure(background="#d9d9d9")
		top.configure(highlightbackground="#d9d9d9")
		top.configure(highlightcolor="black")

		self.setupElements(top)

	def setupElements(self, top=None):
		self.resume_press = tk.Button(top)
		self.resume_press.place(relx=0.267, rely=0.133, height=30, width=70)
		self.resume_press.configure(activebackground="#ececec")
		self.resume_press.configure(activeforeground="#000000")
		self.resume_press.configure(background="#d9d9d9")
		self.resume_press.configure(disabledforeground="#a3a3a3")
		self.resume_press.configure(foreground="#000000")
		self.resume_press.configure(highlightbackground="#d9d9d9")
		self.resume_press.configure(highlightcolor="black")
		self.resume_press.configure(pady="0")
		self.resume_press.configure(state='normal') # disabled
		self.resume_press.configure(text='''Resume''')