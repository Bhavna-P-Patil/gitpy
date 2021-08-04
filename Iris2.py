from sklearn.datasets import load_iris

def main():
    dataset = load_iris()

    print("Features of Dataset")
    print(dataset.feature_names)

    print("Target names of dataset")
    print(dataset.target_names)

    print("Iris data set is:")

    for icnt in range(len(dataset.target)):
        print("ID: %Feature : %Label : %s" %(icnt, dataset.data[icnt], dataset.target[icnt]))

if __name__=="__main__":
    main()