import pandas as pd
import numpy as np


data = pd.read_csv(r"D:\AIML\python_practic\iris.csv") # reading data
#print(data.head())

#data.fillna(1.2) # fill the value with some num,txt
data.dropna(inplace=True)# removing the spaces


# dividing the data  into indipendent and target

x=np.array(data.iloc[:,:-1])# by numpy  DataFrame to arrays
y=data.iloc[:,-1].values    # by pandas DataFrame to arrays
#print(x)
 


# dividing the data  into training and testing    
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.20,random_state=9)


#import the model of knn from the sklearn
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=3)

# training the model with data
model.fit(xtrain,ytrain)

ypred=model.predict(xtest)
 
from sklearn.metrics import accuracy_score
print(accuracy_score(ytest,ypred)*100)
