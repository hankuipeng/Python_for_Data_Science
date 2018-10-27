# %% Reading files with open
file1 = open('README.md', 'w')

file1.name

file1.mode

# the following closes the file
file1.close()

# a better practice is the following, which automatically closes the file
with open('README.md','r') as file1:
    filestuff = file1.read()
    print(filestuff)
    
