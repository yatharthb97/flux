"""
This is a program to demonstrate a multithreading operation which is done using two virtual ports using 
VSPD and a python module called pySerial 

"""
import time
import threading 
from serial import Serial

def send():
    write_port = Serial(port = "COM1", timeout = 0, baudrate = 9600)
    sender = write_port.write(b'hello')

    print(sender)
    print(write_port.is_open)
    print(write_port.baudrate)
    print(write_port.port)
    print(write_port.in_waiting)
    print(write_port.out_waiting)

    # write_port.close()

    return sender


def recieve():
    read_port = Serial(port = "COM2", timeout = 5, baudrate = 9600)
    reciever = read_port.read()

    print(reciever)
    print(read_port.is_open)
    print(read_port.baudrate)
    print(read_port.port)
    print(read_port.in_waiting)
    print(read_port.out_waiting)


    # read_port.close()

    return reciever


thread_1 = threading.Thread(target = send)
thread_2 = threading.Thread(target = recieve)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()
