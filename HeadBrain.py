import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def MeanData(arr):
    size = len(arr)
    sum = 0

    for i in range(size):
        sum = sum + arr[i]

    return (sum/size)

def MarvellousHeadBrain(Name):
    dataset = pd.read_csv(Name)
    print("Size of our data set is",dataset.shape)

    X = dataset["Head size(cm^3)"].values
    Y = dataset["Brain weight(grams) "].values

    print("lenght of X",len(X))
    print("lenght of y ",len(Y))

    Mean_X = MeanData(X)
    Mean_Y = MeanData(Y)

    print("Mean od independent variable is",Mean_X)
    print("Mean of dependent variable is",Mean_Y)

    # m = (sum(x-xb)*(y-yb)/sum(x-xb)^2/Sum(X-Xb)^2

    numerator = 0
    denomenator = 0


    for i in range(len(X)):
        numerator = numerator +(X[i] - Mean_X)*(Y[i] - Mean_Y)
        denomenator = denomenator + (X[i] - Mean_X)**2

    m = numerator/denomenator
    print("value of slope is",m)

  # Y = mX + c
    # c = y - mX
    #c = Mean_Y -(m*Mean_X)
    c= Mean_Y - (m * Mean_X)
    print("value of intercept is",c)

    X_Start = np.min(X) - 200
    X_End = np.max(X) + 200

    x = np.linspace(X_Start,X_End)
    y = m*x + c

    plt.plot(x,y, color = 'r',label = "Line of Regression")
    plt.scatter(X,Y, color = 'b', label = "Data plot")

    plt.xlabel("Head size")
    plt.ylabel("brain weight")

    plt.legend()
    plt.show()



def main():
    #print("Enter file name of datasets")
    #name = input()

    MarvellousHeadBrain("MarvellousHeadBrain.csv")


if __name__=="__main__":
    main()