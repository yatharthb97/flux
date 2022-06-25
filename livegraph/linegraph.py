from collections import deque
from PyQtGraphStack.pyqtgraphstack import PyQtGraphStack

class LiveGraph:



	def __init__(self, data, buffer_size=None, data_len=None):
		

		if buffer_size == None:
			self.data = [] #Arbitrary size
		else:
			self.data = deque(maxlen=buffer_size)


		# Create graph object
		self.graph = PyQtGraphStack() #TODO update argument list

		# Create the appropriate number of curves
		self.curve = self.graph.get_curve("curve", canvas="canvas")

		self.lock = threading.Lock()

		# We need a thread to listen to user calls.
		
		# Launch graph → launch process
		self.graph.launch()


	def read(self):

		from copy import deepcopy
		# Returns a list/dict [buffer] of the data points currently in store.
		self.lock.acquire()
		data = list(deepcopy(self.data))
		self.lock.release()
		return data


	def write(self, datum):
		"""
		Receives data points and updates the graph immediately.
		"""
		self.lock.acquire()
		self.data.append(datum)

		return
		if self.running_graph:
			self.output()


	def output(self):
		"""	
		Updates the graph.
		"""
		if self.scrolling:
			self.graph.set_scrolling_data(curve__, self.canvas, xData, yData)
		else:
			self.curve.setData(*self.data)
		

	def data_import(self):
		"""
		Imports data from a file and plots it.
		"""
		pass

	def data_export(self):
		"""
		Dumps buffer to a file.
		"""
		pass

	def graph_export(self):
		"""
		Dumps the current state of graph to an image.
		"""
		pass

Process0 [flux] 
	|
	data [PIPE]
	|
	---→ Process1 [pyqtgraph] → When to read the pipe for data, commands