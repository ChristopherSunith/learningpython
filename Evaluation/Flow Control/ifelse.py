#program that prints Hello if 1 is stored in spam, Howdy if 2 is stored in spam and Greetings if anything else is stored in spam
print('Enter 1, 2 or any other number')
spam = int(input())
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings')

#if you use spam = input() without defining the datatype, then this program will by default print Greetings. As during execution, python will interpret
#your input value as a string and the if else condition checks for an integer number 1, 2 or any other number.