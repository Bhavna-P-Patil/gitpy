import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def MarvellousHeadBrain(Name):
    dataset = pd.read_csv(Name)
    print("size of our data set is",dataset.shape)

    X = dataset["Head size(cm^3)"].values
    Y = dataset["Brain weight(grams)"].values
    X = X.reshape((-1,1))

    obj = LinearRegression()
    obj.fit(X,Y)

    output = obj.predict(X)


    rsquare = obj.score(X,Y)

    print("value of R square is:",rsquare)

def main():
    #print("enter file name of datset")
    #name = input()
    MarvellousHeadBrain("MarvellousHeadBrain.csv")

if __name__=="__main__":
    main()