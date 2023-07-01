'''Do a program that ask for a aleatory number
and after that the out must be "The number informed is:x"'''


#more infos about the function random in: https://docs.python.org/3/library/random.html

import random                               #the function "random" was imported"
a = random.randint(0,9)                     #inside random there ins randint(x,y) that means a random integer number 
print("The number informed is", a)          #that means a random integer number from x to y


#other way to do...
print("the number infomed is:", random.randint(0,9))