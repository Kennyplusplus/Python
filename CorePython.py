#*****************************CorePython********************************
'''Document owner: Kaushik Raj'''
#*******Topic-1: Strings 
# A string is a series/group of characters

'''#This is a multi line comment
name = "Kaushik"; # A "name" is a variable of type string.  
print(name);#prints the data held by the name variable, and btw ; is not required.
print("Hello"+ name);# The '+' operator concatenates "Hello" string with name variable.
'''

#We can concatenate variables as long as they are of the same data type.
'''
first_name = "Kaushik";
last_name = "Raj";
full_name = first_name +" "+last_name;#concatenating a whitespace as well
print(full_name);#prints the string held by the variable full_name.
'''
#******Topic-2 integer data types
'''
age = 21;
age = age+1;#We can also write age +=1;
print(type(age));#It allows us to know what kind of data type age is.
'''

#******Topic-3 Float data types
#A float data type allows us to store floating point numbers.
'''
flop = 240.9999
print(flop)
print(type(flop))
#type conversion to string
print("Your height is:"+" "+str(flop)+"cm")
'''
#******Topic-4 Bool data type
# A bool data type stores basically "True" or "False"
'''
human = True
print(human)
print("Are you a human?:"+" "+str(human))#Type conversion of bool data type to string data type
'''

#Multiple assignment
'''
#It allows us to assign variables while writing only a single line of code
name,age,engineer = "Kaushik",21,True;
print(name,age,engineer)#So the print fucntion allows us to print multiple values of variables as well, we just need a comma for that XD!!!!
'''
#******Important string methods
'''
name = "Kaushik"
print(len(name))#Fetches us the total length of the string.
print(name.find("K"))#Fetches us the index where the character is located.
print(name.upper())#Converts every character to upper case
print(name.lower())#Converts every character to lower case
print(name.isdigit())#Returns bool values i.e. True or False if the variable is a digit.
print(name.isalpha())#Checks if there are any alphabetical letters
print(name.count("K"))#Returns the count of the argument passed
print(name.replace("a", "o"))#Replaces "a" with "o".
print(name*4)#prints the name variable 4 times
'''
#*****Typecasting
#It allows us to convert a value from one data type to another data type
'''
x,y,z  = 1,2.0,"3"
print(x,y,z)#prints original values
y = int(y)#In order to permanently convert the y integer from float to int we need to reassign the variable by typecasrting it
z = int(z)
print(x,y,z*3)#prints modified values
'''
#*****User Input******
#The input() function allows us to accept user input 
#input("What is your name?:")#Whenever we need to ask the user for input, it's better to clarify what exactly we need;
#It's better to assign the user input to a particular variable
'''
name = input("What is your name?:")
print("Hello!!"+name)
#By default the input() accepts only string values
#To bypass this problem we need to type cast the input() to our desired data type
age  = int(input("What's your age?"))
age+=1#age = age+1
print(age)
'''

#********Some important math functions********
'''
#In order to utlize math fucntions we need to import a library called "math".
import math
pi = 3.14#pi is a float type variable
print(round(pi))#The round() fetches us the round of value for a given variable or value.
print(math.ceil(pi))#Returns a ceiling value
print(math.floor(pi))#Returns the floor value of a given variable or constant value
print(abs(pi))#Returns the absolute value.
print(pow(2,2))#Returns the power of a given number, here 2 to the power 2 is the correct way o reading it.
print(math.sqrt(pi))#Returns the square root of a given number or variable
print(int(math.sqrt(pi)))#Type casting the return value from float to int. 
x,y,z = 4,3,7
print(max(x,y,z))#Returns the max value 
print(min(x,y,z))#Returns the min value
'''
#if-else statements in Python
#if statement: A block of code in an if statement will execute if a certain condition is met.

age = int(input("Specify your age!"))

#In Python we don't need to provide parentheses for condition checking
#Also beware of indentation errors
if age == 100:
 print("You're a century old")
#In Ptython the "else if" changes to "elif" 
elif age >= 18:
 print("You're an adult!!!!")
elif age < 18:
 print("You're a teenager!!!!")
else:
 print("You're still a child")
 




