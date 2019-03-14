import numpy
import pandas as pd

df = pd.read_csv('Dataset-Skip-Thoughts.csv')
length = {}
for i in range(0, len(df)):

    sentenceVector = df.loc[i].values[1]
    sentenceVector = str(sentenceVector)
    sentenceVector = sentenceVector.split(',')
    x = length.get(str(len(sentenceVector)))
    if (x != None):
        length[str(len(sentenceVector))] = int(x) + 1
    else:
        length[str(len(sentenceVector))] =  1
print(length)
