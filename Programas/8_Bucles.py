#Bucle While
i = 1
while i <=5:
    print(i)
    i = i + 1

print("Finished!")

#Bucle While con sentencias If
x = 1
while x < 10:
    if x%2 == 0:
        print(str(x) + " is even")# str(x) is used to convert the number x to a string, so that it can be used for concatenation.
    else:
        print(str(x) + " is odd")

    x += 1

#La sentencia "Break"
i = 0
while 1==1:
    print(i)
    i = i + 1
    if i >= 5:
        print("Breaking")
        break

print("Finished")


#La sentencia "Continue"
i = 1
while i<=5:
  print(i)
  i += 1
  if i==3:
    print("Skipping 3")
    continue

#Bucle For
words = ["hello", "world", "spam", "eggs"]
for word in words:
    print(word + "!")

#Bucle for con centencias "if"
str = "testing for loops"
count = 0

for x in str:
   if(x == 't'):
    count += 1

print(count)

#Similar to while loops, the break and continue statements can be used in for loops, to stop the loop or jump to the next iteration.


#Range
numbers = list(range(10))
print(numbers)

#Range with 2 arguments
numbers = list(range(3, 8))
print(numbers)

print(range(20) == range(0, 20))
#Remember, the second argument is not included in the range, so range(3, 8) will not include the number 8.


#Range whit 3 arguments
numbers = list(range(5, 20, 2))
print(numbers)
#We can also create list of decreasing numbers, using a negative number as the third argument, for example list(range(20, 5, -2)).

#For Each
for i in range(5):
    print("hello!")
