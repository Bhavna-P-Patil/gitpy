import os
from sys import *

def DirectoryTraversal(path):
    print("Contents of the directory are")

    for Folder,Subfolder,Filename in os.walk(path):
        print("Directory name is :" +Folder)
        for sub in Subfolder:
            print("Subfolder of " +Folder + "is" +sub)
        for file in Filename:
            print("File name is:" +file)
            
            


def main():
    print("MArvellous INfosystem")
    print("Directory travel script")

    if(len(argv)!=2):
        print("Error: Invalid number of arguments")
        exit()

    if(argv[1]=="-u")or (argv[1]=="U"):
        print("Usage: provide the absolute path of the target director")
        exit()

    if(argv[1]=="-h")or (argv[1]=="H"):
        print("It is directory cleaner script")
        exit()

       
    DirectoryTraversal(argv[1])
        
if __name__=="__main__":
    main()    
