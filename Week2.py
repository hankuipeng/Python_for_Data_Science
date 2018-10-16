# %% tuples
Tuple = ('bean', 12, 12.1)

type(Tuple)

Tuple[-3]
Tuple[-1]


# concatenate tuples
tuple1 = Tuple + ("hard rock", '8')
tuple1

# tuple slicing
tuple1[0:3] # get the first 3 elements

# length of a tuple
len(tuple1)

# tuples are immutable
tuple = tuple1
tuple

tuple = sorted(tuple)
tuple

# tuples can contan tuples
tuple2 = (tuple, (1,2), tuple1)
tuple2[1][0]


# %% lists

# lists are mutable
L = ['bud', 12, 16.1]
L[0]
L.extend(['pop', 1, 'star'])
L
# unlike 'extend', 'append' only adds one element to the list
L.append(['pop', 1, 'star'])
L
# delete element of a list
del(L[0])
L

# convert string to list
"bean and bud".split()


A=((11,12),[21,22])
A[1]

'A,B,C,D'.split(',')


# %% Dictionaries
dict = {"key1":[0,1], "key2":("music","festival")}
dict

dict["key1"]

# add new value to the dictionary
dict["key3"] = 2018
dict

# delete a key and its value
del(dict["key1"])
dict

# obtain all the keys and values in the dictionary
dict.keys()
dict.values()


# %% Sets
set1 = {"pop","star","pop","test","summer","fall","autumn","fall"}

# all the duplicates are gone once the set is created
set1

# typecasting: convert a list to a set
list1 = ["this","is","a","test"]
del(set) # delete the previously overriding object
list2 = set(list1)

list2.add("new")

# verify if an element is in a set
"new" in list2
