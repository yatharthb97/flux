

def welcome_message():
	s = "Welcome to the console."
	return s


def emptyline_gen():
	while true:
		yield '\n'

def blankkine_gen():
	w_size = os.get_window_size()
	cols = w_size[0]
	while true:
		yield (' ' * cols) + '\n'

def repeatline_gen():
	char = '•'
	w_size = os.get_window_size()
	while true:
		yield char * w_size[0]