from __future__ import division
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
import numpy as np
import pandas as pd
import csv

input_file = "../data/where_train1.csv"
#test_file = "test_who.csv"
#f = open("who_train.csv",'r')
#data = np.loadtxt(fname = f, delimiter = ',')


df = pd.read_csv(input_file, header = 0,encoding='utf-8')

#tf = pd.read_csv(test_file, header = 0,encoding='utf-8')
# put the original column names in a python list


original_headers = list(df.columns.values)

print(original_headers)

# remove the non-numeric columns
df1 = df._get_numeric_data()
#tf1 = tf._get_numeric_data()
#allVars = tf.as_matrix()
#names = allVars[:,1]
#print(df1)

# put the numeric column names in a python list
numeric_headers = list(df1.columns.values)

print("numeric headers")
print(numeric_headers)


# create a numpy array with the numeric values for input into scikit-learn
numpy_array = df1.as_matrix()
#test_array = tf1.as_matrix()

clf = tree.DecisionTreeClassifier()
#X1 = vals[:,2:6]
#Y1 = vals[:,6]
X = numpy_array[:, 1:7]


x1 = X[100]#to get a particular row
print(x1)

#testX = test_array[:,1:7]
#print(testX)

Y = numpy_array[:,8]
#testY = test_array[:,7]
gnb  = GaussianNB()
mnb = MultinomialNB()
#print(Y)
#y_pred = gnb.fit(X,Y)

clf = clf.fit(X, Y)
gnb = clf.fit(X,Y)
pred = []

for i in X:
    pred.append(gnb.predict(i.reshape(1,-1))[0])
    #print(gnb.predict(i.reshape(1,-1))[0])    
  

count = 0
for j in range(0,len(pred)):
    print(numpy_array[j][0],pred[j],Y[j])
    if pred[j] == Y[j]:
        count+=1
print("accuracy = ",count*100 /len(pred) , "%")      
#print(Y1)


import pickle
# save the classifier
with open('../data/my_where_classifier.pkl', 'wb') as fid:
    pickle.dump(gnb, fid)
    
    
# load it again
#with open('my_dumped_classifier.pkl', 'rb') as fid:
 #   gnb_loaded = cPickle.load(fid)    
     
#file('a.csv')
