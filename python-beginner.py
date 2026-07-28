a=3
b=4
print(a+b)  #7
print(a-b)  #-1
print(a*b)  #12
print(a/b)  #0.75
print(a%b)  #3
print(a//b) #0
print(a**b) #81
--------------------------------------------
a=10
b=5
print(a==b)   # False
print(a!=b)   # True
print(a>b)    # True
print(a<b)    # False
print(a>=b)   # True
print(a<=b)   # False
-------------------------------------------
print(type(10)) #int
print(type(9.8)) #float
print(type(4 - 4j)) #complex
print(type(['Atl', 'Python', 'tm'])) #list
print(type('aj')) #str
print(type('value')) #str
print(type('india')) #str
-------------------------------------------
x1=2
y1=3
x2=10
y2=8
distance=(((x1-x2)**2)+((y1-y2)**2))**0.5
print(distance)
--------------------------------------------
x1=2
y1=3
x2=10
y2=8
distance=(((x1-x2)**2)+((y1-y2)**2))**0.5
print(distance)
-------------------------------------------
x=True
y=False
print(x and y)   # False
print(x or y)    # True
print(not x)     # False
-------------------------------------------
name=input("Enter your name:")
age=int(input("Enter your age:"))
print(name)      # output eg:aj
print(age)       # age eg: 21
-------------------------------------------
num=int(input("Enter a number:"))
if num>0:
    print("Positive")   # Example: 5 -- Positive
elif num<0:
    print("Negative")   # Example: -3 -- Negative
else:
    print("Zero")       # Example: 0 -- Zero

