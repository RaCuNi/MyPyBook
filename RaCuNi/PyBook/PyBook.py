#PyBook Project
#2018-02-15
#CLI Ver.
from builtins import int
from datetime import datetime
from test.test_zipimport import NOW

COME = 0
USE = 0
NOW = 0


def dataLogger():
    try:
        print("Logging...")
    
        logdata = open("logdata.txt", 'r')
        logdata.close
    except FileNotFoundError as e:
        print("logdata.txt is not exist!")
        
        print("Making new file...")
        
        logdata = open("logdata.txt", 'w')
        
        logdata.write("now:"+' '+str(NOW))
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
                    NOW = COME-USE
                    
                    
                with open("logdata.txt", 'r+') as ld:
                    lines = []
                    new_line = "now:"+" "+str(NOW)
                    for line in ld:
                        if(line.startswith('now:')):
                            lines = lines +[new_line]
                        else:
                            lines = lines + [line]
                            
                        ld.seek(0)
                        ld.writelines(lines)
                        ld.truncate() 
                
                       
                    
            elif a == 2:
                USE = int(input("enter the num of you've used: \n"))
                
                print("You've entered: ", USE, "Won")
                
            else:
                dataLogger().logdata.close
                print("Nothing Changed! :)")
            
dataLogger()
accBook()