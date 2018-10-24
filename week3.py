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
