import numpy as np
import csv as csv
import pandas as pd

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

readdata = csv.reader(open('train.csv', 'r'))

data = []

for row in readdata:
    data.append(row)

Header = data[0]
data.pop(0)

frame = pd.DataFrame(data, columns=Header)
print(frame)

male = frame.loc[frame['Sex'] == 'male']
male_survivors = frame.loc[(frame['Sex'] == 'male') & (frame['Survived'] == '1')]
female = frame.loc[frame['Sex'] == 'female']
female_survivors = frame.loc[(frame['Sex'] == 'female') & (frame['Survived'] == '1')]

print("{0} out of {1} males survived".format(len(male_survivors), len(male)))
print("{0} out of {1} females survived".format(len(female_survivors), len(female)))
