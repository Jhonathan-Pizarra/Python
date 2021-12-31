
#Escribir Archivo
file = open("newfile.txt", "w")
file.write("This has been written to a file")
file.close()

#Leer Archivo
file = open("newfile.txt", "r")
print(file.read())
file.close()

#Sobreescribir Archivo
file = open("newfile.txt", "w")
file.write("Some new text")
file.close()

file = open("newfile.txt", "r")
print("Reading new contents")
print(file.read())
print("Finished")
file.close()

#El método write: eturns the number of bytes written to a file, if successful.
msg = "Hello world!"
file = open("newfile.txt", "w")
amount_written = file.write(msg)
print(amount_written)
file.close()
