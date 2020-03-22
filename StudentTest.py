import numpy as np, pandas as pd

students = pd.io.parsers.read_csv(r'.\Data\students.csv')
print(students)

#print(students.ix[:,['name','sex']])
print(students[(students['age']>30) & (students['sex']=='F')])

