# define dataframe
# convert to dictionary
# 
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 

myDict = dict(df.values)
# error in logic
print(myDict)