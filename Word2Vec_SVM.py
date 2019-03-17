from gensim.models import Word2Vec
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, cohen_kappa_score
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import numpy as np

data = pd.read_csv('Pre-processed.csv')
data = data.drop([0, 0])
X = data.iloc[0:, 0:7].values
Y = data.iloc[0:, 7].values
X = X.tolist()
model = Word2Vec(X, min_count=1)
# summarize the loaded model
# summarize vocabulary
words = list(model.wv.vocab)
# access vector for one word
jj = []
for i in X:
    jj.append(model[i])
# save model
model.save('model.bin')
# load model
new_model = Word2Vec.load('model.bin')
jj = np.asarray(jj)
nsamples, nx, ny = jj.shape
jj = jj.reshape((nsamples, nx * ny))

x_train, x_test, y_train, y_test = train_test_split(jj, Y, test_size=0.50, random_state=0)

parameter_grid = {'kernel': ('linear', 'rbf'), 'C': (600, 800, 1000, 1200),
                  'gamma': (0.05, 0.08, 0.1, 0.15, 'scale'), 'decision_function_shape': ('ovo', 'ovr'),
                  'shrinking': (True, False)}

SVM = GridSearchCV(SVC(), parameter_grid, cv=5)

print("====================Grid Search================\n", SVM.fit(x_train, y_train))
print("\n====================Best Parameter====================\n", SVM.best_params_)
print("\n====================Kappa Statistic====================\n", cohen_kappa_score(y_test, SVM.predict(x_test)))
print("\n====================Confusion Matrix====================\n", pd.crosstab(y_test, SVM.predict(x_test),
                                                                                  rownames=['True'],
                                                                                  colnames=['Predicted'], margins=True))
print("\n====================Precision table====================\n", classification_report(y_test, SVM.predict(x_test)))
print("\n====================Accuracy====================\n ", accuracy_score(y_test, SVM.predict(x_test)))
