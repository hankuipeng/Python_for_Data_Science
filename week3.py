#%% If statement
age = 19

if (age>18):
    print("you can enter.")
print("move on.")

#%% else statement
age = 15
if (age>18):
    print("you can enter.")
else:
    print("let's do something different")
print("move on.")

#%% elif statement
# If the 'if' statement is true, then the 'elif' statement would be checked
age = 18
if (age>18):
    print("you can enter.")
elif(age==18):
    print("congrats!")
else:
    print("let's do something different")
print("move on.")

#%% logic operators
not(True)

album_year = 1994
if (album_year > 1989) and (album_year < 2000):
    print("This album is produced in the 1990s.")

#%% Loops
range(10)
range(10,15)

# example 1
squares = ['red', 'yellow', 'green', 'cyan']
for i in range(0,4):
    squares[i] = 'white'

squares

# example 2
squares = ['red', 'yellow', 'green', 'cyan']
for square in squares:
    print(square)

# enumerate through index and variable
for i,square in enumerate(squares):
    print(i,square)


#%% While Loops

squares = ['red', 'red', 'red', 'yellow']
Newsquares = []
i = 0
while squares[i] == 'red':
    Newsquares.append(squares[i])
    i = i + 1

Newsquares


#%% Functions
len(squares)

# sorted is a function that returns a new list,
# it does not change the original object
ratings = [3,4,2,1,5]
sorted(ratings)
ratings

# on the other hand, sort changes the order of the
# original object
ratings.sort()
ratings


#%% Making Functions
def add1(a):
    b = a + 1
    return(b)

x = 5
add1(x)

# multiple parameters
def mult(a,b):
    m = a*b
    return(m)

mult(3,5)

mult(3,'Euan')

def printstuff(stuff):
    for i,s in enumerate(stuff):
        print('Album:',i,'Rating',s)

printstuff(ratings)


# global and local variables
def pinkfloyd():
    global claimedsales
    claimedsales = '45'
    return(claimedsales)


pinkfloyd()


def add(x):
    return(x+x)

add('1')


#%% Objects and Classes

# built-in types in python:
# dictionary, lists, bool, int, float, string

ratings
ratings.reverse()

ratings

#%% Creating a class

# define your class
class Circles(object):
    # initialize each data instance of the class
    # with data attributes. The function 'init' is
    # a constructor that is used to initialize data
    # attributes
    def __init__(self, radius, color):
        # the self parameter refers to the newly
        # created instance of the class
        self.radius = radius;
        self.color = color;

    def add_radius(self,r):
        self.radius = self.radius + r
        return(self.radius)

# create a Circle object
RedCircle = Circles(10,'red')
RedCircle.radius

# change color attribute
RedCircle.color = 'blue'
RedCircle.color

RedCircle.add_radius(1)

# obtaining the list of data attributes or methods
# associated with a class 
dir(RedCircle)
