from archive import Archive

#WRITE function

arc = Archive('test.txt')
arc.write('hello \nMy name is \nVaibhav \nNice to meet you\n')

#READ function

hello_read = arc.read(10) 
print(hello_read)

#OUTPUT function

print(arc.output())

#DATA_IMPORT function

arc.data_import('data_import.txt')

#BINARY function

bin = arc.Binary('data_import.txt')
bin.write(b'This is a binary file')




