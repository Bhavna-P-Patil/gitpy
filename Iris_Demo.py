import pandas as pd



def main():
    data = pd.read_csv("Iris.csv")
    print(len(data))
    print(data.head())


if __name__=="__main__":
    main()
