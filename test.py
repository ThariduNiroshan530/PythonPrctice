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



print(10)
print(type(10))
print(type(-10))
print(type(0))
print(12.5)
print(type(12.5))
print(type(-12.5))
print(type(0.0))
print(2+3j)
print(type(2+3j))
print(type(-3j))
print(type(0+0j))
print(type(True))
print(type(False))
print(type('Tharidu'))
print(type('123'))
print(type('09/01/23'))
print(type([1,2,3]))
print(2+3)
print(10/5)
print(10//3)
print(2**5)
print(3**0.5)
print(2**-3)
print(435.667**-.334)
import math
print(math.e)
print(math.pi)
print(22/7)
print(331/113)
print(5643.33%24.5578)
print(2+5*3)
print(10/5 -2*3)
print(3*5 -12/4**2)
print(2**2**3)
print(2**4)
print(3**2**4)
print(77/98 -65*6)
print(8**3**2)
print("Tharidu")
print("Tharidu")
x = 6
y = 8
z = x+y
print(z)
thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(len(thistuple))
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
tuple8 = ("apple", "banana", "cherry")
tuple9 = (1,2,3,4,5,9)
tuple12 = (True, False, False)
print(tuple8)
print(len(tuple8))
print(tuple9)
print(len(tuple9))
print(tuple12)
print(len(tuple12))
tuple01 = ("abc", 34, True, 40, "male")
print(tuple01)
print(type(tuple01))
thistuple = tuple(("apple", "banana", "cherry")) #note the double round-brackets
print(thistuple)
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
print(thistuple[-1])
thistuple = ("apple", "banana", "cherry", "orange", "mango")
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[2:])
print(thistuple[-4:-1])


thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
  
  x = ("apple", "banana", "cherry")
  y = list(x)
  y[1] = "kiwi"
  x = tuple(y)

  print(x)

print(thistuple)

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
      print(thistuple[i])
      i = i + 1      

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

thistupl = ("apple", "banana", "cherry")
for x in thistupl:
  print(x)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#python set

myset = {"apple", "banana", "cherry"}
print(myset)

thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry", "apple",}
print(thisset)

thisset = {"apple", "banana", "cherry"}
print(len(thisset))

set1 = {"apple", "banana", "cherry"}
set2 ={1, 2, 3, 9, 7}
set3 ={True, False, False}
print(set1)
print(set2)
print(set3)

set1 = {"abc", 34, True, 40, "male"}
print(set1)

myset = {"apple", "banana", "cherry"}
print(type(myset))

thisset = set(("apple", "banana", "cherry")) #note the double round brackets
print(thisset)

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)


thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)


thisset = {"apple","banana", "cherry"}

thisset.discard("banana")

print(thisset)

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x) #removed item

print(thisset)


thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)


thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


set1 = {"a", "b", 'c'}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update()

print(x)




