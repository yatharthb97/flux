

""""
A Data Subscriber that stores received data in a specified file format.

.txt (ascii), .pkl, .npy, .hd5 (HDF5)
"""

from os import path
import numpy as np
import pandas as pd

class Archive:

	"""
	Archive class for ASCII and binary filemodes that use generic file
	"""

	def __init__(self, filename, mode='w+', buffering=-1, **kwargs):
		
		self.filename = path.abspath(filename) 
		self.mode = mode
		self.file = open(filename, self.mode, buffering=buffering, **kwargs)

		self.start_pos = self.file.tell()

		# Archive must be writable atlease.
		if not self.file.writable():
			raise Exception(f"File Archive is not writable. Check file modes.")

		# If the file type is .hd5
		self.filetype = path.splitext(filename)
		if self.filetype[1] == '.hd5':
			return 'Use ArchiveHDF5 instead'

		
	def write(self, datum):
		"""
		Write a line to a file.
		"""
		if not self.file.closed:
			self.file.write(datum)


	def read(self, lines = None):
		if self.file.readable():
			self.file.flush()
			current_pos = self.file.tell()

			# TODO: Discuss if readable items should be in a list or just normal strings.
			# If normal then only the read() function will suffice.

			self.file.seek(self.start_pos) 
			if lines != None:
				rd = self.file.readlines(lines)
			else:
				rd = self.file.read()

			self.file.seek(current_pos)
			return rd


	def output(self, out = None):
		"""
		Returns the contents of the file as a string. Return all contents and be terminal friendly.
		TODO: Check with binary.
		"""
		import codecs
		output_str = codecs.decode(self.read(), 'unicode_escape')
		if out == None:
			return output_str
		else:
			out.write(output_str)

	def data_import(self, filename):
		"""
		Copies data from another file.
		"""
		other_file = open(filename, 'r')
		data = other_file.read()
		self.file.write(data)

	def data_export(self):
		"""
		Closes the file.
		"""
		#TODO: Discuss the purpose of this function

		self.file.flush()
		self.file.close()


	def __repr__(self):
		filename = (self.filename > 20 * (self.filename[-20:] + "...")) + (self.filename <= 20 * self.filename)
		return f"< DS-Archive [{self.mode}]@ {filename} # {self.file.tell() - self.start_pos} bytes>"

	def __str__(self):
		return self.__repr__()

	def __del__(self):
		self.file.close()

	# Factory Specializations

	@staticmethod
	def Binary(filename, **kwargs):
		arch = Archive(filename, mode = 'wb+', **kwargs)
		return arch
		
	# This function can be written in the __init__ without asking the user the type of the function 
	"""
	#Abstract factory interface
	def Type(string):
		string = string.lower()
		if string == 'hd5':
			return ArchiveHDF5 # In order for this to work, this class needs to be above the Archive class. 
	"""

class ArchiveCSV(Archive):

	def write(self, line_buffer_2d, channels):
		self.line_buffer_2d = line_buffer_2d
		self.channels = channels

		if not self.file.closed and self.filetype[1] == '.csv':
			dir = {}
			for channel in range(Linebuffer.no_of_channels()):
				dir[channels[channel]] = line_buffer_2d[channel]
			self.out = pd.DataFrame(data = dir)
			self.out.to_csv(self.filename, index = False)

	def read(self, info = False, nd_array = False):
		self.out.head()

		if info:
			self.out.info()
		if nd_array:
			data = self.out.iloc[:,:].values
			print(data)




class ArchiveNPY:
	
	def __init__(self, filename, buffer_size = None, data = None, dtype = None):
		self.filename = filename
		self.file = open(self.filename, 'w') #Open in write-only mode.

		if buffer_size == None:
			self.buff_size = 64
		else:
			self.buff_size = buffer_size

		if dtype == None:
			dtype = data.dtype
			self.object_type = isinstance(data, object)
		else:
			self.object_type = isinstance(data, object)
		self.dtype = dtype

		if data != None:
			self.data = np.ndarray(data, dtype = self.dtype)
		else:
			self.data = np.full(self.size, fill_value=np.nan, dtype=self.dtype)
			self.data.resize(self.buff_size, refcheck=self.object_type)

	def read(self, lines, back = True):
		
		
		# Reads `lines` number of lines/entries from the data buffer.
		
		pass

	def write(self, datum):
		datum = list(datum)
		length = len(datum)

		if self.size + length >= self.buff_size:
			self.buff_size = self.buff_size*2
			self.data.resize(self.buff_size)

		# Tried using numpy iterators
		with np.nditer(self.data[self.size:self.size+length], op_flags=['readwrite']) as it:
  	 		for i, element in enumerate(it):
       		element[...] = datum[i]

	def output(self):
		
		# Returns a deepcopy of the held data.
		
		return self.data.copy()

	def data_import(self, filename, overrides=True):
		
		# Import a numpy format file to the Archive.
		# overrides: True → Adopt the data formatting of the data being imported.
		

	def data_export(self, filename):
		
		# Save the held data into a numpy binary format file.
		
		np.save(filename, self.data[:self.size], allow_pickle=True)




class ArchiveHDF5:
	def __init__(self) -> None:
		print('For HDF5 files only')
	
	def read():
		pass
	


class ArchivePickle:
	pass



class LineBuffer:


	def RedTable():
		lb = LineBuffer()
		lb.formatters.append(lambda x : Fore.RED + x + Fore.WHITE)
		lb.formatters.append(lambda x : prettytable(x))
		return lb

	self.formatters = []