import pandas as pd
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.preprocessing import LabelEncoder
import seaborn

#0,1.Sentence,2.Usage,3.Idiom,4.BetweenPOS,5.NumOfWordsBetween,6.PrePOS,7.prePOS2,8.postPOS,9.postPOS2,10.CountOfSameNounInContext,11.SentenceLength,12.SentimentsAVG
#2.Usage, 5.NumOfWordsBetween, 10.CountOfSameNounInContext,  11.SentenceLength,  12.SentimentsAVG
df  =pd.read_csv('Dataset5.csv', header=0, sep=',')
Y = df.values[:,2]
X = df.values[:,[5,10,11,12]]
plt.figure(figsize = (30,30))
le = LabelEncoder()
df = df[df.Usage != 'Q']
mask = abs(df.SentimentsAVG) > 0.5
mask2 = abs(df.SentimentsAVG) < 0.5

df.loc[mask, 'SentimentsAVG'] = 1
df.loc[mask2, 'SentimentsAVG'] = 0
print(df.values[:,12])
#df['SentimentsAVG'] = np.where(df['SentimentsAVG'] > 0.5 or df['SentimentsAVG'] < -0.5, 1, 0).astype(int)
df['Usage'] =le.fit_transform(df['Usage'])
df = df[['Usage', 'NumOfWordsBetween', 'CountOfSameNounInContext',  'SentenceLength',  'SentimentsAVG']]


features=list(X)
s=seaborn.heatmap(df.corr(),cmap='coolwarm',annot=True, linewidths=.5)
s.set_yticklabels(s.get_yticklabels(),rotation=30,fontsize=30)
s.set_xticklabels(s.get_xticklabels(),rotation=30,fontsize=30)
plt.savefig('heatmap2.png')
