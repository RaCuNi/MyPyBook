#PyBook Project
#2018-02-15
#CLI Version
from builtins import int
from datetime import datetime

COME = 0 #GLOBAL
USE = 0 #GLOBAL
NOW = 0 #GLOBAL


#DEF Logging function
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

#DEF Variable NOW function
def varNOW():
    with open("logdata.txt", 'r') as ldread:
                ldlines = ldread.readlines()

                #print(ldlines) test line
                #print(ldlines[0]) test line    
                
                NOW_DATA = ldlines[1]   
                NOW = int(NOW_DATA)
                
                #print(int(NOW_DATA)) test line      
                NOW = (NOW+COME)-USE
                
                ldlines[1] = str(NOW)+"\n"
                
                with open("logdata.txt", 'w') as ldwrite:
                    ldwrite.writelines(ldlines)
                    
                #print(ldlines) test line
                #print(ldlines[0]) test line




#DEF MAIN function
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
                _COME_Reason = input("Please enter the reason: \n")
                
                
                with open("logdata.txt", 'a') as ldc:
                    calcDate = datetime.now()
                    nowDate = calcDate.strftime('%Y-%m-%d')
                    ldc.write("\n")
                    ldc.write("["+nowDate+"]"+" "+"+"+" "+str(COME)+" "+"r: "+_COME_Reason)
                    #NOW = NOW+COME-USE #Don't use
                
                varNOW() #use varNOW
                COME = 0 #Reset
                
            elif a == 2:
                USE = int(input("enter the num of you've used: \n"))
                
                print("You've entered: ", USE, "Won")
                
                _USE_Reason = input("Please enter the reason: \n")
                
                with open("logdata.txt", 'a') as ldu:
                    calcDate = datetime.now()
                    nowDate = calcDate.strftime('%Y-%m-%d')
                    ldu.write("\n")
                    ldu.write("["+nowDate+"]"+" "+"-"+" "+str(USE)+" "+"r: "+_USE_Reason)
                
                varNOW()
                USE = 0 #Reset
            else:
                dataLogger().logdata.close
                print("Nothing Changed! :)")
            
dataLogger()
accBook()