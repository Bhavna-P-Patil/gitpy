import os
from sys import *

def main():
    print("MArvellous INfosystem")
    print("Directory travel script")

    if(len(argv)!=2):
        print("Error: Invalid number of arguments")
        exit()

    if(argv[1]=="-u"):
        print("Use the script as Name.py parameters")

    if(argv[1]=="-h"):
        print("This is Demo automation script")
if __name__=="__main__":
    main()    
