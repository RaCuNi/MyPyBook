#PyBook Project
#2018-02-15
#CLI Ver.
from builtins import int
from datetime import datetime

COME = 0
USE = 0
NOW = 0


def dataLogger():
    try:
        print("Logging...")
    
        logdata = open("logdata.txt", 'r')
        logdata.close
    except FileNotFoundError:
        print("logdata.txt is not exist!")
        
        print("Making new file...")
        
        logdata = open("logdata.txt", 'w')
        
        logdata.write("[NOW]\n")
        logdata.write(str(NOW)+"\n")
        logdata.write("[END]\n")
        logdata.close
    
    finally:
        with open("logdata.txt", 'r') as log:
            readLog = log.readline()
            print(readLog)

def accBook():
    global NOW
    global COME
    global USE
    
    while True:
        a = int(input("What do you wanna do? \n Type that 1 or 2: \n"))
        if type(a) == int:
            if a == 1:
                COME = int(input("enter the num of you've earned: \n"))
                
                print("You've entered: ", COME, "Won")
                comeReason = input("Please enter the reason: \n")
                
                
                with open("logdata.txt", 'a') as ld:
                    cacDate = datetime.now()
                    nowDate = cacDate.strftime('%Y-%m-%d')
                    ld.write("\n")
                    ld.write("["+nowDate+"]"+" "+"+"+" "+str(COME)+" "+"r: "+comeReason)
                    #NOW = NOW+COME-USE
                    
                with open("logdata.txt", 'r') as ldread:
                    ldlines = ldread.readlines()

                #print(ldlines) test line
                #print(ldlines[0]) test line    
                
                NOW_DATA = ldlines[1]   
                NOW = int(NOW_DATA)
                
                #print(int(NOW_DATA)) test line      
                NOW = NOW+COME-USE
                
                ldlines[1] = str(NOW)+"\n"
                
                with open("logdata.txt", 'w') as ldwrite:
                    ldwrite.writelines(ldlines)
                    
                #print(ldlines) test line
                #print(ldlines[0]) test line
                
            elif a == 2:
                USE = int(input("enter the num of you've used: \n"))
                
                print("You've entered: ", USE, "Won")
                
            else:
                dataLogger().logdata.close
                print("Nothing Changed! :)")
            
dataLogger()
accBook()