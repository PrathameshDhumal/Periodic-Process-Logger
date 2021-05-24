from sys import *

def Function(value):
    print("Inside Function with Parameter:"+value) #+value:send parameter through command line
    
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
        print("This is a demo automation script")
        exit()
    Function(argv[1])
if __name__ == "__main__":
    main()