#!/usr/bin/env python3

from collections import deque
import os


class LinesBuffer:
	"""
	A collection of lines which is stored in a circular buffer.
	Has functionality to preprocess lines.
	"""
	
	def __init__(self, ratio):
		cols, tot_lines = os.get_terminal_size()
		lines = tot_lines * float(ratio[0]) / ratio[1]
		self.buffer = deque(maxlen=lines)

		self.preprocessors = lambda x : x
	
	def add(self, string):
		"""
		Add line to the buffer.
		"""
		self.buffer.append_left(string)


	def resize(self, ratio):
		"""
		Function that resizes the buffer.
		"""
		w_size = list(os.get_terminal_size()) #[x, y]
		self.size[1] = int(math.floor(self.ratio[0]/self.ratio[1])) * w_size[1]

		#Ignore change in x for now. #TODO

		self.buffer = deque(itertools.islice(self.buffer))
		self.buffer.maxlen(self.size[1])

	def get_lines(self):
		"""
		Returns a list of lines from the buffer after preprocessing.
		"""

		# Apply preprocessor to every string in the buffer.
		return list(self.buffer)
