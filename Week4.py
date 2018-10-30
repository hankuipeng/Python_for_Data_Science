# %% Reading files with open
file1 = open('README.md', 'w')

file1.name

file1.mode

# the following closes the file
file1.close()

# a better practice is the following, which automatically
# closes the file
with open('README.md','r') as file1:
    filestuff = file1.read()
    print(filestuff)

# print the first line
with open('README.md','r') as file1:
    filestuff = file1.readlines()
    print(filestuff)

type(filestuff)
filestuff[1]


# print all the lines
with open('README.md','r') as file1:
    for line in file1:
        print(line)


# print the first 4 letters of the first line
with open('README.md','r') as file1:
    filestuff = file1.readline(4)
    print(filestuff)


# %% Writing files with open
with open('practice.txt', 'w') as file2:
    file2.write("This is the first line.")

lines = ['this is line 1\n', 'this is line 2\n']
with open('practice.txt', 'w') as file2:
    for line in lines:
        file2.write(line)


# %% Pandas
import pandas as pd
csv_path = 'test.csv'
