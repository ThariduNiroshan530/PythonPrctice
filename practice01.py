print('Tharidu')
print('ss')
print('123')
print(True)
print(type(True))
print('Tharidu \n niroshan') #escape character
print('Tharidu said "good morning !" ')
name = 'Tharidu'
print(name)

#math operation
a=2
b=3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)

#concatination

a="Hello"
b=" World"

d=a+b
print(d)

a>b
print(a==b)
a=True
b=False

c= not b
print(c)

#exo operater

a=True
b=False

# name=input('Enter your name:')
# print("Hello",name)

# print('Enter your name :',end='')
# name=input()
# print("Hello",name)


#Data structure
# list
x=[1,2,3,4]
print(x)
y=x[0]
print(y)

x[3]=700
print(x)

x.append(100)
x.insert(3,600)
print(x)

x.remove(600)
print(x)

x.pop(2)

a=[1,2,3,4]
b=[5,6,7,8]

z=a+b
print(z)
m=3 in z
print(m)

m=3 not in  z
print(m)
 
# Dictanary
x={'1000':'colombo','9000':'badulla'}
x['1200']='moratuwa'
print(x)

y=x['1000']
print(y)

print(x.keys())

del x['1000']
print(x)

x={
    "a":['Hello','Hi','Good morning'],
    "b":['Bye','Good morning'],
    "c":['Good afternoon']
}

y=x['a']
print(y)
y.append('Aayubowan')
print(y)
z=x["c"]
print(z)

def greeting(name):
    print("Hello, " + name)

print("Tharidu")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        def myfunc(self):
            print("Hello my name is " + self.name)
 
 #python string formatting

price = 49
txt = "The price is {} dollars"
print(txt.format(price))


quantity = 3
itemo = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemo, price))

quantity = 3
itemo = 567
price = 49
myorder = "iI want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemo, price))

age = 36
name = "John"
txt = "Hos name is {1}. {1} is {0} yours old."
price(txt.format(age, name))

myorder = "I have a {carname}, it is a {model}."
price(myorder.format(carname = "Ford", model = "Mustang"))

print("Tharidu")

thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)


print("Tharidu")

username = input("Enter username:")
print("Username is: " + username)


price = 49
txt = "The price is {} dollars"
print(txt.format(price))

quantity = 3
itemo = 675
price = 49
myorder = "I want {} pieces of item number {} for{:.2f} dollars."





def calculate():
    # Get the input form the user
    operation = input("enter the sum (+, -, *, /): ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    #Perform the calculation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    else:
        result = "Invalid operator"

    # Print the result
    print("The result is:", result)

# Call the calculate function
calculate()

