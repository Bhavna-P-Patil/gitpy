from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from scipy.spatial import distance
from sklearn.metrics import accuracy_score

def CalculateDistance(X,Y):
    return distance.euclidean(X,Y)

class Marvellous():
    def fit(self,TrainingData,TrainingTarget):
        self.TrainingData = TrainingData
        self.TainingTarget = TrainingTarget

    def predict(self,TestData):
        predictions = []
        for row in TestData:
            label = self.Shortest(row)
            predictions.append(label)
        return predictions

    def Shortest(self,row):
        Minindex= 0
        MinDistance = CalculateDistance(row,self.TrainingData[0])

        for i in range(1,len(self.TrainingData)):
            Distance = CalculateDistance(row,self.TrainingData[i])
            if Distance < MinDistance:
                MinDistance = Distance
                Minindex = i
        return self.TrainingTarget[Minindex]

def MarvellousKNN():
    Line ="@"*50
    iris = load_iris()

    data = iris.data
    target = iris.target
    print(Line)
    print("Actual Dataset")
    print(Line)
    for i in range(len(iris.target)):
        print("ID :%d Lable : %s, Feature : %s" %(i,iris.data[i], iris.target[i]))

    data_train, data_test, target_train, target_test = train_test_split(data,target,test_size=0.5)

    print(Line)
    print("Training Dataset ")
    print(Line)
    for i in range(len(data_train)):
        print("ID :%d Data : %s, Feature : %s" % (i, data_train[i], target_train[i]))

    print(Line)
    print("Testing dataset ")
    print(Line)
    for i in range(len(data_test)):
        print("ID :%d Data : %s, Feature : %s" % (i, data_test[i], target_test[i]))

    print(Line)
    mobj =Marvellous()
    mobj.fit(data_train,target_train)
    ret = mobj.predict(data_test)

    print("Result of ML Model")
    print(Line)
    for i in range(len(data_test)):
        print("ID :%d Expectation : %s, Prediction : %s" % (i, target_test[i], ret[i]))
    print(Line)


    icnt =0
    for i in range(len(data_test)):
        if target_test[i]!=ret[i]:
            icnt = icnt + 1
    print("Number of wrong answer by the ML model:",icnt)
    print(Line)

    Accuracy = accuracy_score(target_test,ret)
    return Accuracy

def main():
    ret = MarvellousKNN()
    print("Accuracy of KNN is: ",ret*100,"%")
    print("@"*50)


if __name__=="__main__":
    main()