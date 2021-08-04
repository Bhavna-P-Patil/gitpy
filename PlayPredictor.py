import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing

def Predictor(path):
    # step 1
    data = pd.read_csv(path)
    print("Dataset loaded succesfully with the size:",len(data))

    # step 2
    Feature = ["whether","Temperature"]
    print("Feature names are",Feature)

    Whether = data.Whether
    Temperature = data.Temperature
    Play = data.Play

    lobj = preprocessing.LabelEncoder()

    WhetherX = lobj.fit_transform(Whether)
    TemperatureX = lobj.fit_transform(Temperature)
    Label = lobj.fit_transform(Play)

    print("Encoded whether is")
    print(WhetherX)

    print("Encoded temperature is")
    print(TemperatureX)

    Feature = list(zip(WhetherX,TemperatureX))

    # step3
    obj = KNeighborsClassifier(n_neighbors=3)
    obj.fit(Feature,Label)

    #step 4
    output = obj.predict([[0,2]])

    if output == 1:
        print("U can play")
    else:
        print("Dont play")

def main():
    print("______Marvellous Play predictor_______")
    print("Enter the path of the file which contains dataset")
    path = input()
    
    Predictor(path)


if __name__=="__main__":
    main()