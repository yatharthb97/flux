#!/usr/bin/env python3

from collections import deque
import os





# Object that manages the view and `parsar`.
"""
The view is made up of three 

"""
class ConsoleManager:

	def __init__(self, name=None):

		self.console = Console() #For parse user input

		self.header = LinesBuffer([1,8]) # <- 1/8 Ratio of screen (in y)
		self.data = LinesBuffer([5,8]) # <- Ratio of screen (in y)
		self.consolelog = LinesBuffer([2,8]) # <- Ratio  of screen (in y)
		self.printlist = [self.header, self.data, self.consolelog]

		self.page = utility.welcome_message() #Maintains the lines in current view
		print(utility.listprint(self.last_print))
		self.last_page = self.page # Last printed page

		self.all_lines = sum([lines.size() for lines in self.printlist])

		self.object_name = "console"
		self.head_in = f"| {name}-{self.object_name} →IN>"
		self.head_out = f"| {name}-{self.object_name} →OUT>"
	
	def update(self):
		"""
		Reads the line buffers and updates the page
		"""
		self.last_page = list(self.page)
		for buffer in self.printlist
			self.page = buffer.get_lines(self.page, self.mutex) #No formatting here TODO
		
		print(utility.listprint(self.page))


	def input(self):
		new_input = raw_input(self.console_header, fill_timeout_later)
		self.input.add(f"{self.head_in}  {new_input}")
		self.console.push(new_input)


	def add_data(self, string):
		self.data.add(string)


	def set_header(self, string):
		self.header.add(string)

	#For erasing lines
	def eraser(self):
		for i, lines in enumerate(self.printlist):
			if lines.updated():	
				if i == 2:
					utilities.erase_lines(lines)
					return
				else:
					utilities.erase_lines(self.all_lines)
					return

	@classmethod
	def ratio(num, den):
		"""
		Returns the number of lines in window for the  given ratio.
		"""
		pass

## Objects that need to be made -> Parsar (Console), 
## Formaters (which will give specific colors to the three different buffers),
## Console
##     ∟ User defined commands
##	   ∟ Linux (system) commands
##     ∟ ACK / NACK machine (with context management)



