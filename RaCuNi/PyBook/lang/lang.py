# -*- coding: ms949 -*-
#PyBook MultiLanguages
#2018-02-19
#CLI version

LANG = []

def lang():
    global LANG
    
    what_lang = input("What is your language? \n 1: Korean \n 2: English")
    what_lang = int(what_lang)
    if what_lang == 1:
        LANG.append(["로그 읽는중...", "logdata.txt 파일이 존재하지 않네요! :(", "새로 만드는 중...", "[---현재 돈---]\n", "[---끝---]\n", "무엇을 하실건가요? \n 1은 소득, 2는 지출: \n", "당신이 얻은 돈의 양을 작성해주세요 (원): \n", "당신은 : ", "원을 작성하셨네요", "간단한 원인이나 이유를 작성해주세요: \n", "이유: ", "당신이 사용한 돈의 양을 작성해주세요 (원): \n", "원을 사용하셨네요", "아무것도 달라지지 않았네요. 혹시 키를 잘못 누르신건가요? :)"])
    
    elif what_lang == 2:
        LANG.append(["Logging...", "logdata.txt is not exist!", "Making new file...", "[NOW]\n", "[END]\n", "What do you wanna do? \n Type that 1 or 2: \n", "enter the num of you've earned: \n", "You've entered: ", "Won", "Please enter the reason: \n", "reason: ", "enter the num of you've used: \n", "Won", "Nothing Changed! :)"])
    
    else:
        
        print("ERROR! Please enter the num 1 or 2!")
        
        lang()