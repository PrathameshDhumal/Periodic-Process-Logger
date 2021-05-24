import os
import time
import psutil
from sys import *

def ProcessDisplay(FolderName = "Project"):
    print("list of running processes")
    
    Data = []
    
    if not os.path.exists(FolderName):  #makes new folder if not mentioned
        os.mkdir(FolderName)
    else: 
        print("Destination directory is already present")
        exit()
    
    File_Path = os.path.join(FolderName,"Legion%s.log")
    fd = open(File_Path,"w")
    
    for proc in psutil.process_iter():
        value = proc.as_dict(attrs = ['pid','name','username'])
        Data.append(value)
        
    for element in Data:
        fd.write("%s\n"%element)
        
        
def main():
    print("-------Periodic Process Logger-------")
    print("Script title:"+argv[0])
	
    if(len(argv)!=2):
        print("Insufficient Argument to the script")
        exit()
    if(argv[1] == "-u") or(argv[1] == "-U"):
        print("Use the script as Name.py Parameters")
        exit()
    if(argv[1] == "-h") or(argv[1] == "-H"):
        print("Help:It is used to create log file of running process")
        exit()
    
    ProcessDisplay(argv[1]) 
if __name__ == "__main__":
    main()