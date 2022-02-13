# name = 'meekz'
from colorama import Fore, Back, Style, init
init()


print( Back.GREEN )
print( Fore.BLACK )
operation = input('what are we do? ')

print( Back.CYAN)
a =float( input("write first  number: "))
b =float(input("write second number: "))

print( Back.YELLOW)
if operation == "+":
    c = a+b
    print('c +: ', str(c))
elif operation == "-":
    c = a-b
    print('c -: ',str(c) )
else:
    print("chose operation")
    

 
