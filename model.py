import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# import pickle


def health_pred(arr):
 data = pd.read_csv("projectcombdataset.csv")
 data = np.array(data)

 X = data[:,0:6]
 y = data[:,6:]
 y = y.astype('int')
 X = X.astype('int')

 X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
 log_reg = LogisticRegression()
 log_reg.fit(X_train, y_train)

#  arr = np.array([[ 1,1,1,0,10,150]])
#  print(arr)
 b = log_reg.predict(arr)
#  print(b)
 return b
#pickle.dump(log_reg,open('modelpickle.pkl','wb'))
# model=pickle.load(open('modelpickle.pkl','rb'))