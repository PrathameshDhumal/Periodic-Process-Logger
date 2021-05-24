
#used to describe the running process pid and name
import psutil
from sys import *

def ProcessDisplay():
    print("list of running processes")
    
    Data = []
    for proc in psutil.process_iter():
        value = proc.as_dict(attrs = ['pid','name'])
        Data.append(value)
        
    return Data
def main():
    print("-------Periodic Process Logger-------")
    print("Script title:"+argv[0])

        
    arr = ProcessDisplay()
    for element in arr:
        print(element)
if __name__ == "__main__":
    main()