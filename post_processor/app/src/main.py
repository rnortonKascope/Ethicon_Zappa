import threading
from datetime import datetime
import time
import sys

from gui import GUI

import numpy as np
import random

import tkinter as tk
from tkinter import messagebox

import warnings
warnings.simplefilter('error', RuntimeWarning)



class Main():

	g = None 
	running = True

	def __init__(self,debug=False):
		print(debug)

		global g
		g = GUI(self)

		


		ready = True
		
		if ready:

			print('[ OKAY ] Main class initialized.')

			while self.running:
				g.update()

			try:
				g.tkroot.destroy()
			except Exception:
				print('[ OKAY ] Window already destroyed.')
		else:
			print('[ WARN ] User rejected startup conditions. Exiting.')

		stopAllThreads()
		e.closeAllFiles()


	def exit(self):
		self.running = False
		

# Check for command line argument for debugger
debug_flag = False
debug_keyword = 'debug'
if __name__ == "__main__":
	for i, arg in enumerate(sys.argv):
		if debug_keyword in arg:
			debug_flag = True

# Start the program
m = Main(debug_flag)

# Instructions for pyinstaller (https://realpython.com/pyinstaller-python/)
# >> conda install pyinstaller (if havent already)
# >> pyinstaller main.py --name ZappaCPBLoop -w --icon=icon.ico
#
# Note: --add-data commands may be useful for storing settings and other non-code files