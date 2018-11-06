import pandas
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
csv_path = '/home/hankui/Dropbox/Clustering/WorkLog/WorkLog.xlsx'
#df = pd.csv_read(csv_path)
df = pd.read_excel(csv_path)
df.head()

# a dataframe can be created out of a dictionary
songs={"album":['album_a','album_b'],"released":[1993,1994]}

song_frame = pd.DataFrame(songs)

song_frame.head()

song_frame[['album']]

# access 1st row 2nd column of the data frame
song_frame.ix[0,1]

# data frame slicing
new_df = song_frame.ix[0:1,0:1]
new_df

# find the unique values in a column of a data frame
song_frame['released'].unique()


# %% 1-dimensional array
import numpy as np
a = np.array([0,1,2,3,4,5])
a
type(a)

a[0]=100
a
a.mean()

np.pi

# output evenly spaces values between an interval
x = np.linspace(0,2*np.pi,num=500)
y = np.sin(x)

import matplotlib.pyplot as plt

% matplotlib inline
plt.plot(x,y)


# %% 2-dimensional array
# create a list
a = [[1,2,3],[4,5,6]]

# cast the list into an array
np_a = np.array(a)

np_a.shape

np_a.ndim

np_a.size


X=np.array([[1,0],[0,1]])
Y=np.array([[2,2],[2,2]])
Z=np.dot(X,Y)
Z
