#======================
# Imports
#======================
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure,show
from seaborn import *
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


#=========================
# ML Operations
#=========================
def TitanicLogistic():
    # step 1- Load data
    Titanic_data = pd.read_csv("MarvellousTitanicDataset.csv")

    # step 2 - Data analysis
    print("1st five records of dataset")
    print(Titanic_data.head())
    print("Total no of records are:",len(Titanic_data))

    #step2 - Data analysis in detailed
    print("visualization of survived and non survived passangers")
    figure()
    countplot(data = Titanic_data, x = "Survived")
   # show()

    print("visualization according to gender")
    figure()
    countplot(data = Titanic_data, x = "Survived", hue = "Sex" )
   # print("visualization according to sex")
    #show()

    print("visualization according Pclass")
    figure()
    countplot(data = Titanic_data, x = "Pclass")
    #show()

    print("Survived v/s non survived based on age ")
    figure()
    Titanic_data["Age"].plot.hist().set_title("visulization according to age")
    #show()

    # step 3 - Data cleaning
    Titanic_data.drop("zero",axis = 1,inplace = True)
    print("Data after colounm removal")
    Titanic_data.head()

    Sex = pd.get_dummies(Titanic_data["Sex"])
    print(Sex)

    print("sex coloumn after updation")
    Sex = pd.get_dummies(Titanic_data["Sex"],drop_first = True)
    print(Sex)

    Pclass = pd.get_dummies(Titanic_data["Pclass"])
    print(Pclass.head)

    # concate sex and pclass failed in our dataset
    #Titanic_data = pd.concate([Titanic_data,Sex,Pclass],axis = 1)
    #print("Data after concatination")
    #print(Titanic_data.head())

    # Removing unneccesary fields
    Titanic_data.drop(["Sex","Pclass","Embarked","sibsp","Parch"],axis = 1,inplace = True)
    print(Titanic_data.head)

    # Divide the dataset x and y
    x = Titanic_data.drop("Survived",axis = 1)
    y = Titanic_data["Survived"]

    # Split the data for training and testing purpose
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.5)

    obj = LogisticRegression(max_iter = 1000)

    # step4 - train dataset
    obj.fit(x_train,y_train)

    # step 5 - Testing
    output = obj.predict(x_test)
    print("Accuracy of given dataset is :")
    print(accuracy_score(y_test,output))

    print("confusion metrix is:")
    print(confusion_matrix(y_test,output))
    
      
    
    
    
#=================
# Entry POint
#=================
    
def main():
    print("******LOgistic Case studies******")
    TitanicLogistic()
    
#==========================
# Starter
#==========================

if __name__=="__main__":
    main()
