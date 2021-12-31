'''
You have been asked to make a special book categorization program, which assigns each book a special code based on its title.
The code is equal to the first letter of the book, followed by the number of characters in the title.
For example, for the book "Harry Potter", the code would be: H12, as it contains 12 characters (including the space).

You are provided a books.txt file, which includes the book titles, each one written on a separate line.
Read the title one by one and output the code for each book on a separate line.

For example, if the books.txt file contains:
Some book
Another book
'''

#C:\Users\hp\Desktop\Jueves\Python\Ejercicios
path = "C:/Users/hp/Desktop/Jueves/Python/Ejercicios/books.txt"
file = open("/Users/hp/Desktop/Jueves/Python/Ejercicios/books.txt", "r")

for line in file:
	title=line.replace('\n','')
	count=len(title)
	print(f'{title[0]}{count}')
file.close()