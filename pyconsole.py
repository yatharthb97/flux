
class Computation:
	"""
	Represents a unit of Computation and contains just one representation of the same.
	"""

	def __init__(self, session_dict):
		self.sdict = session_dict

	def __str__(self):
		sd = self.sdict

		err = len(sd["stderr"] > 0) * f"err: {err}" 
		string =	\
		f"""[ {sd['session']} ] → returned  {sd['ret']}
			
			>> {sd['command']}

			out: {sd['stdout']}

			{err}
			"""
		return string


class LineBuffer():
	

	def add_formatter(self, fn):
		pass


import os
import platform
import time

class Console:


	def __init__(self, name=None, branch=False):
		"""
		Console constructor

		Arguemnts:
		__________

		+ name : Name of the console application.
		+ branch : Start a seperate python interpreter and run the console application on it.
				   (Not to distrurb the original interpreter environment.)
		"""

		#TODO
		# 1. Change input and output to "in" and "out".

		# Record time for starting the application
		self.start_time = time.time_ns()


		# START OF INPUT VALIDATION

		self.name = name
		if self.name == None:
			self.name = "pyConsole"

		from socket import gethostname
		self.host = gethostname()
		self.platform = platform.system()
		self.release = platform.release()

		# END OF INPUT VALIDATION



		# Console options
		self.echo = True
		self.logging = True
		self.enable_sys = True
		self.page_refresh = False


		# List/Dictionary of valid commands
		self.sys_list = {}
		self.envlist = {}
		self.envlist["default"] = CreateDefaultEnv()


		# User input
		self.user_input = None
		self.tokens = None
		self.seperator = " " #Single or double space


		# LineBuffers
		self.stdout = LineBuffer()
		self.stderr = LineBuffer()
		#self.stderr.add_formatter(lambda string : Fore.RED + string + Fore.WHITE)

		# Meta information about the io session
		self.end_io = True
		self.io_sessions = {}
		self.io_session_cnt = 0



	def io(self, recursive=True):
		"""
		Main function that handles the IO process.
		"""

		# Set resources for a new input session.
		self.end_io = False
		o_count = 0
		i_count = 0

		start_time = time.time_ns()
		while(not self.end_io and (recursive and i_count < 1)):

			self.user_input = self.input()
			i_count = i_count + 1
			if self.echo:
				print(self.user_input)

			ret, out, err = self.processor(self.user_input)
			self.output()


			# Collect session metadata.
			self.io_sessions_cnt = self.io_sessions_cnt + 1
			self.io_sessions[self.io_sessions_cnt] = {"session": self.io_sessions_cnt, "ret": ret, \
										 	 		  "start_time": start_time, "end_time": end_time}
			
			if self.logging:
				self.io_sessions[self.io_sessions_cnt].extend({"stdout": out, "stderr": err})
			
			self.stdout.write(out)
			self.stderr.write(err)


		end_time = time.time_ns()
		self.end_io = True




	
	def header(self):
		from colorama import Fore
		string =  f"{Fore.GREEN}|| {Fore.BLUE}{self.host}{Fore.WHITE} @ {Fore.RED}{self.name} {Fore.GREEN}||{Fore.WHITE}\n"
		string += f"{Fore.GREEN}|| s[{self.io_session_cnt}] @ {os.getcwd()}{Fore.GREEN} >>{Fore.WHITE} "
		return string

	def input(self):
		"""
		Calls the Console input functionality.
		"""
		return input(self.header())

	def output(self):
		"""
		Used to print output.
		"""
		if self.page_refresh:
			out = self.stdout.read()
			err = self.stderr.read()
			zipped = zip(out, err)
			for out_, err_ in zipped:
				print(out_, '\n', err_)
		else:
			print(Computation(self.io_sessions_cnt))

	def processor(self, cmd, sep=" "):
		"""
		Proesses the given user input.
		"""

		# Tokenize
		self.tokens = cmd.split(sep)

		
		# Check if it is part of an internal environment
		if any(self.tokens[0] in env for env in self.envlist):
			# Process
			for env in self.envlist:
				if self.tokens[0] in env:
					ret = env.execute() #TODO pass args
					return ret

		elif self.enable_sys:
			self.sys_execute(cmd)

	def sys_execute(self, cmd):
		"""
		Execute command as a subprocess on the system.
		"""
		pass

	def exit_io(self):
		"""
		End IO Loop. TODO: thread-safe.
		"""
		self.end_io = True

	def sanatize_tokens(self):
		"""
		Clean tokens for spaces and other junk.
		"""
		pass


class Environment:

	"""
	A collection of keys and corresponding executables.
	"""

	class MergeError(Exception):
		pass

	def __init__(self, name="None"):

		self.name = name
		self.fns = {}
		self.obj_fns = {}
		self.preprocessors = {}


		# Environment options
		self.force_add = False

	def add_fn(self, key, func):
		self.fns[key] = func

	# Mostly useless
	def add_obj_fn(self, key, obj, fn):
		self.obj_fn[key] = [obj, fn]

	def execute(self, key, *args, **kwargs):

		if key in self.fns:
			ret = self.fns[key](*args, **kwargs)
			return ret

		elif key in self.obj_fns:
			ret = self.obj_fns[key][0].self.obj_fns[key][1](args, kwargs)
			return ret

		else:
			return KeyError(f"[EXECUTOR - {self.name}] Key not found - {key}.")

	def __contains__(self, key):
		"""
		Operator overloading for "in" operator / keyword.
		"""
		return (key in self.fns) or (key in self.obj_fns)

	def __add__(self, other_env, force=False):
		"""
		Addition of 
		"""
		from copy import deepcopy

		vec1list = [deepcopy(self.fns), deepcopy(self.obj_fns)]
		vec2list = [deepcopy(other_env.fns), deepcopy(other_env.obj_fns)]

		for vec in vec2:
			for key in vec.keys():
				
				if key in vec1: #Conflicts

					# Conflicts but same defination #TODO - Implement completeness
					if vec1[key].__code__.co_code == vec2[key].__code__.co_code:
						pass # Environment variable is already present.

					# Conficts that are not trivial
					else:
						# Conflict is non-trivial
						if self.force_add:
							new_key = key + "2"
							if not new_key.__contains__(): # Check if `new_key` is available.
								print(f"Addition of Environments {self.name} & {other_env.name}: Duplicate key - `{key}` changed to `{new_key}`.")
								vec1[new_key] = vec2[key] #Add key directly
							else:
								raise MergeError(f"Addition failed due to non-trivial conflicts: key={key}.")
								return None

						else:
							raise MergeError(f"Addition failed due to non-trivial conflicts: key={key}.")
							return None

				else: # No conflicts
					vec1[key] = vec2[key] #Add key directly







import sys
def CreateDefaultEnv():
	env = Environment(name="default")
	env.add_fn("cd", os.chdir)
	env.add_fn("exit", sys.exit)
	env.add_fn("echo", print)
	env.add_fn("clear", lambda : os.system("cls"))
	env.add_fn("hello", lambda: print("Hello! How are you?"))
	return	env


if __name__ == "__main__":
	console = Console(name="yatharth")
	env = CreateDefaultEnv()
	#console.io()
	while 1:
		x = console.input("hi")
		x = x.split(" ")
		print(env.execute(x[0], *x[1:]))
		#print(x)
		




