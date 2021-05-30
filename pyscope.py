#Create Global variable

x = "global"

def foo():
    print("x inside:", x)


foo()
print("x outside:", x)


#Accessing local variable outside the scope
def foo():
    y = "local"

foo()
print(y)

#Create a Local Variable

def foo():
    y = "local"
    print(y)

foo()


 #Using Global and Local variables in the same code
x = "global "

def foo():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)

foo()

#Global variable and Local variable with same name
x = 5

def foo():
    x = 10
    print("local x:", x)


foo()
print("global x:", x)

