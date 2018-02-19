#PyBook Project
#2018-02-15
#CLI Version
from builtins import int
from datetime import datetime
import RaCuNi.PyBook.lang.lang
from RaCuNi.PyBook.lang.lang import LANG

COME = 0 #GLOBAL
USE = 0 #GLOBAL
NOW = 0 #GLOBAL

lang_py = RaCuNi.PyBook.lang.lang
lang = LANG


#DEF Logging function
def dataLogger():
    try:
        print(lang[0][0])
    
        logdata = open("logdata.txt", 'r')
        logdata.close
    except FileNotFoundError:
        print(lang[0][1])
        
        print(lang[0][2])
        
        logdata = open("logdata.txt", 'w')
        
        logdata.write(lang[0][3])
        logdata.write(str(NOW)+"\n")
        logdata.write(lang[0][4])
        logdata.close
    
    finally:
        with open("logdata.txt", 'r') as log:
            readLog = log.readline()
            print(readLog)

#DEF Variable NOW function
def varNOW():
    with open("logdata.txt", 'r') as ldread:
                ldlines = ldread.readlines()  
                
                NOW_DATA = ldlines[1]   
                NOW = int(NOW_DATA)
                   
                NOW = (NOW+COME)-USE
                
                ldlines[1] = str(NOW)+"\n"
                
                with open("logdata.txt", 'w') as ldwrite:
                    ldwrite.writelines(ldlines)

#DEF MAIN function
def accBook():
    global NOW
    global COME
    global USE
    
    while True:
        a = int(input(lang[0][5]))
        if type(a) == int:
            if a == 1:
                COME = int(input(lang[0][6])) #Earn
                
                print(lang[0][7], COME, lang[0][8])
                _COME_Reason = input(lang[0][9])
                
                
                with open("logdata.txt", 'a') as ldc:
                    calcDate = datetime.now()
                    nowDate = calcDate.strftime('%Y-%m-%d')
                    ldc.write("\n")
                    ldc.write("["+nowDate+"]"+" "+"+"+" "+str(COME)+" "+lang[0][10]+_COME_Reason)
                
                varNOW() #use varNOW
                COME = 0 #Reset
                
            elif a == 2:
                USE = int(input(lang[0][11])) #Use
                
                print(lang[0][7], USE, lang[0][12])
                
                _USE_Reason = input(lang[0][9])
                
                with open("logdata.txt", 'a') as ldu:
                    calcDate = datetime.now()
                    nowDate = calcDate.strftime('%Y-%m-%d')
                    ldu.write("\n")
                    ldu.write("["+nowDate+"]"+" "+"-"+" "+str(USE)+" "+lang[0][10]+_USE_Reason)
                
                varNOW()
                USE = 0 #Reset
            else:
                dataLogger().logdata.close
                print(lang[0][13])
            
lang_py.lang() #Language settings
dataLogger() #Log data
accBook() #Main function