import os
from sys import *
import hashlib

def CalculateChecksum(path,blocksize = 1024):
    fd = open(path,'rb')
    hobj = hashlib.md5()

    buffer = fd.read(blocksize)
    while len(buffer)>0:
        hobj.update(buffer)
        buffer = fd.read(blocksize)

    fd.close()
    return hobj.hexdigest()

def DirectoryTraversal(path):
    print("Contents of the directory are")


    duplicate = {}                   # dictionary to hold checksum and file name
    for Folder,Subfolder,Filename in os.walk(path):
        print("Directory name is :" +Folder)
        for sub in Subfolder:
            print("Subfolder of " +Folder + "is" +sub)
        for file in Filename:
            print("File name is:" +file)
            actualpath = os.path.join(Folder,file)
            hash = CalculateChecksum(actualpath)

            if hash in duplicate:        # that checksum is already present
                duplicate[hash].append(actualpath)
            else:
                duplicate[hash] = [actualpath]

    return duplicate    
            
def DisplayDuplicate(duplicate):
    output = list(filter(lambda x : len(x)>1, duplicate.values()))

    if(len(output)>0):
        print(" There are duplicate files")
    else:
        print("There are no duplicate files")
        return
    
    print("List of duplicate files are")
    icnt = 0
    for result in output:
         icnt = 0 
        print(result)
        for path in result:
            icnt+=1
            if icnt>=2:
                print("%s"%path)
                
              


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

    arr = {}   
    arr = DirectoryTraversal(argv[1])

    DisplayDuplicate(arr)    

if __name__=="__main__":
    main()    
