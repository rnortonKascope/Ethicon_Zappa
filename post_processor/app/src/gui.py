import sys
import time
import PIL.Image
import PIL.ImageTk
from PIL import ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
#import math


class GUI():


	r = None # top
	tkroot = None # Tkinter root object
	w = None # window

	ready = False

	lastUpdateGraphTime     = 0

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

		top.geometry("1200x700+183+148")
		top.minsize(130, 10)
		top.maxsize(5150, 1071)
		top.resizable(1,  1)
		top.title("CPB Loop Controller")
		top.configure(background="#d9d9d9")
		top.configure(highlightbackground="#d9d9d9")
		top.configure(highlightcolor="black")

		self.setupRecordingControl(top)


	def setupRecordingControl(self, top=None):

		self.Frame2 = tk.Frame(top)
		self.Frame2.place(relx=0.5, rely=0.0, relheight=0.107, relwidth=0.25)
		self.Frame2.configure(relief='groove')
		self.Frame2.configure(borderwidth="2")
		self.Frame2.configure(relief="groove")
		self.Frame2.configure(background="#d9d9d9")
		self.Frame2.configure(highlightbackground="#d9d9d9")
		self.Frame2.configure(highlightcolor="black")

		# self.Button2_1 = tk.Button(self.Frame2)
		# self.Button2_1.place(relx=2.223, rely=1.587, height=55, width=55)
		# self.Button2_1.configure(activebackground="#ececec")
		# self.Button2_1.configure(activeforeground="#000000")
		# self.Button2_1.configure(background="#d9d9d9")
		# self.Button2_1.configure(disabledforeground="#a3a3a3")
		# self.Button2_1.configure(font="-family {Segoe UI} -size 24")
		# self.Button2_1.configure(foreground="#000000")
		# self.Button2_1.configure(highlightbackground="#d9d9d9")
		# self.Button2_1.configure(highlightcolor="black")
		# self.Button2_1.configure(pady="0")
		# self.Button2_1.configure(text='''▶''')

		# self.Button2_2 = tk.Button(self.Frame2)
		# self.Button2_2.place(relx=2.543, rely=2.307, height=55, width=55)
		# self.Button2_2.configure(activebackground="#ececec")
		# self.Button2_2.configure(activeforeground="#000000")
		# self.Button2_2.configure(background="#d9d9d9")
		# self.Button2_2.configure(disabledforeground="#a3a3a3")
		# self.Button2_2.configure(font="-family {Segoe UI} -size 24")
		# self.Button2_2.configure(foreground="#000000")
		# self.Button2_2.configure(highlightbackground="#d9d9d9")
		# self.Button2_2.configure(highlightcolor="black")
		# self.Button2_2.configure(pady="0")
		# self.Button2_2.configure(text='''▶''')

		self.resume_press = tk.Button(self.Frame2)
		self.resume_press.place(relx=0.267, rely=0.133, height=30, width=70)
		self.resume_press.configure(activebackground="#ececec")
		self.resume_press.configure(activeforeground="#000000")
		self.resume_press.configure(background="#d9d9d9")
		self.resume_press.configure(disabledforeground="#a3a3a3")
		self.resume_press.configure(foreground="#000000")
		self.resume_press.configure(highlightbackground="#d9d9d9")
		self.resume_press.configure(highlightcolor="black")
		self.resume_press.configure(pady="0")
		self.resume_press.configure(state='disabled')
		self.resume_press.configure(text='''Resume''')

		self.pause_press = tk.Button(self.Frame2)
		self.pause_press.place(relx=0.5, rely=0.133, height=30, width=70)
		self.pause_press.configure(activebackground="#ececec")
		self.pause_press.configure(activeforeground="#000000")
		self.pause_press.configure(background="#d9d9d9")
		self.pause_press.configure(disabledforeground="#a3a3a3")
		self.pause_press.configure(foreground="#000000")
		self.pause_press.configure(highlightbackground="#d9d9d9")
		self.pause_press.configure(highlightcolor="black")
		self.pause_press.configure(pady="0")
		self.pause_press.configure(state='disabled')
		self.pause_press.configure(text='''Pause''')

		self.stop_press = tk.Button(self.Frame2)
		self.stop_press.place(relx=0.733, rely=0.133, height=30, width=70)
		self.stop_press.configure(activebackground="#ececec")
		self.stop_press.configure(activeforeground="#000000")
		self.stop_press.configure(background="#d9d9d9")
		self.stop_press.configure(disabledforeground="#a3a3a3")
		self.stop_press.configure(foreground="#000000")
		self.stop_press.configure(highlightbackground="#d9d9d9")
		self.stop_press.configure(highlightcolor="black")
		self.stop_press.configure(pady="0")
		self.stop_press.configure(state='disabled')
		self.stop_press.configure(text='''Stop''')

		self.record_press = tk.Button(self.Frame2)
		self.record_press.place(relx=0.033, rely=0.133, height=30, width=70)
		self.record_press.configure(activebackground="#ececec")
		self.record_press.configure(activeforeground="#000000")
		self.record_press.configure(background="#d9d9d9")
		self.record_press.configure(disabledforeground="#a3a3a3")
		self.record_press.configure(foreground="#000000")
		self.record_press.configure(highlightbackground="#d9d9d9")
		self.record_press.configure(highlightcolor="black")
		self.record_press.configure(pady="0")
		self.record_press.configure(text='''Record''')
		self.record_press.configure(state='normal')

		self.Label1 = tk.Label(self.Frame2)
		self.Label1.place(relx=0.027, rely=0.6, height=21, width=60)
		self.Label1.configure(activebackground="#f9f9f9")
		self.Label1.configure(activeforeground="black")
		self.Label1.configure(background="#d9d9d9")
		self.Label1.configure(disabledforeground="#a3a3a3")
		self.Label1.configure(foreground="#000000")
		self.Label1.configure(highlightbackground="#d9d9d9")
		self.Label1.configure(highlightcolor="black")
		self.Label1.configure(text='''Timestamp''')

		self.timestamp = tk.Entry(self.Frame2,justify="center")
		self.timestamp.place(relx=0.267, rely=0.6, height=20, relwidth=0.7)
		self.timestamp.configure(background="white")
		self.timestamp.configure(disabledbackground="#cccccc")
		self.timestamp.configure(font="TkFixedFont")
		self.timestamp.configure(foreground="#000000")
		self.timestamp.configure(highlightbackground="#d9d9d9")
		self.timestamp.configure(highlightcolor="black")
		self.timestamp.configure(insertbackground="black")
		self.timestamp.configure(selectbackground="blue")
		self.timestamp.configure(selectforeground="white")
		self.timestamp.configure(state='disable')
