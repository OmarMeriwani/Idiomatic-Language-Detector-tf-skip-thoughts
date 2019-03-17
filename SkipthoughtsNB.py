import pandas as pd
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
import seaborn
from sklearn.model_selection import train_test_split
from ast import literal_eval
from sklearn.metrics import accuracy_score, classification_report, cohen_kappa_score


df  =pd.read_csv('Dataset-Skip-Thoughts.csv', header=0, sep=',')
le = LabelEncoder()
df = df[df.usage != 'Q']
df = df[['vector', 'usage']]
le = LabelEncoder()
df['vector'] = df['vector'].apply(literal_eval)
df['usage'] = le.fit_transform(df['usage'])
train, test = train_test_split(df, test_size=0.2)
x_train = list(train['vector'])
y_train = train['usage']
x_test = list(test['vector'])
y_test = test['usage']
nb = GaussianNB()
nb.fit(x_train,y_train)
y_pred = nb.predict(x_test)

print("\n====================Kappa Statistic====================\n", cohen_kappa_score(y_test, y_pred) )
print("\n====================Confusion Matrix====================\n", pd.crosstab(y_test, y_pred))
print("\n====================Precision table====================\n", classification_report(y_test, y_pred))
print("\n====================Accuracy====================\n ", accuracy_score(y_test, y_pred))