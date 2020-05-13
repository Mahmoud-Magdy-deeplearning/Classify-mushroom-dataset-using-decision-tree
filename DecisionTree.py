import pandas as pd
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import f1_score 

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

import math

missing_val='?'
df = pd.read_csv('agaricus-lepiota.csv'
                             na_values=missing_val) 
df.rename(columns="e.1":"a")
df['a'] = df['a'].fillna(df['a'].mode()[0])

df = pand.get_dummies(df, prefix_sep='_', drop_first=True)

x=df.iloc[:, 1:]
y=df.iloc[:, 0]
X, X_test, Y, Y_test = train_test_split(x, y, test_size=.3)  

classifier = DecisionTreeClassifier(max_depth=3)

classifier.fit(X, Y)

Y_predicted = classifier.predict(X_test)

print(Y_predicted)
confmatrix = con(Y_test, Y_predicted)
print(f1_score (Y_test, Y_predicted))
print(' accuracy_score(Y_test, Y_predicted))
