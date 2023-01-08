print("Tharidu")
print(34+45)
x=6
y=7
print(x==y)
print("Tharidu")
x=28
y=76
z=x+y
print(z)
print(type(1234566265366))
a = 123
print(type(a))
st = {5,2,4,1}
print(type(st))
c = 2+3j
d = {1:'a', 2:'b', 3:'c'}
print(d)
print(type(d))
a = "Tharidu"
print(a.upper())
a = "Hello"
b = "world"
c = a + b
print(c)
a = "Hello"
b = "world"
c = a + "" + b
print(c)
age = 36
txt = "My name is john, and I am {}"
print(txt.format(age))
x = 6
y = 5
z = x+y
print(z)
x = 8.5
print(type(x))
y = 8+4j
print(type(y))
a = "Tharidu"
print(a[1])
for x in "banana":
    print(x)
p = "Tharidu"
print(len(p))
txt = "The best things in life are free"
print("free" in txt)
b = "Hello world"
print(b[2:5])
a = 200
b = 33
q = b*a
print(q)
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
list1 = ["apple", "banana", "cherry"]
print(list1)
list2 =[1, 5, 6, 9]
print(list2)
list3 = [True, False, False]
print(list3)
print("Tharidu")
#print("hello, world!")
print("cheers, Matel!")
x = 5
print(x)
y = "Tharidu"
print(y)
x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)
x = str(3) # x will be '3'
y = int(3) # y will be 3
z = float(3) # z will be 3.0
print(x)
print(y)
print(z)
b = "Hello, world"
print(b)
print(b[2:5])
print(b[:5])
print(b[2:])
a = "Hello world"
print(a.upper())
print(a.upper())
print(a.strip()) # returns "Hello world"
print(a.replace("H", "J"))
print(a.split(","))
a = "Hello"
b = "world"
c = a + b
print(c)
c = a + " " + b
print(c)
age = 21
txt = "My name is Tharidu, and I am {}"
print(txt)
print(10 + 3)
mylist = ["apple", "banana", "cherry"]
print(mylist)
print(len(mylist))
print(10 > 9)
print(10 == 9)
print(10 < 9)
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is greater than a")
print(bool("Hello"))
print(bool(15))
x = "Hello"
y = 15  
print(bool(x))
print(bool(y))
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
class myclass():
    def _len_(self):
        return 0
myobj = myclass()
print(bool(myobj))  


def myFunction() :
  return True

print(myFunction())      

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

  x = 200
print(isinstance(x, int))

x = lambda a : a + 10
print(x(5))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))