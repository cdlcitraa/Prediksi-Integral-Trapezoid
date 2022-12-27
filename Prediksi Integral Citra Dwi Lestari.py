import numpy as np
import csv
import time

from sklearn import svm
import pandas as pd

#Database: Gerbang LOgika AND
#Membaca data dari file
FileDB = 'DatabaseIntegral.txt'
Database = pd.read_csv(FileDB, sep=",", header=0)
print(Database)

#x = Data, y=Target
X = Database[[u'a', u'b']]
y = Database.Target

#Training and Classify
clf = svm.SVC()
clf.fit(X.values,y)
print (clf.predict( [[1,2]] ))
print (clf.predict( [[2,3]] ))
print (clf.predict( [[3,4]] ))
print (clf.predict( [[4,5]] ))
print (clf.predict( [[5,6]] ))
print (clf.predict( [[6,7]] ))
print (clf.predict( [[7,8]] ))
print (clf.predict( [[8,9]] ))
print (clf.predict( [[9,10]] ))
print (clf.predict( [[10,11]] ))
