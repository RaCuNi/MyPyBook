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
        LANG.append(["�α� �д���...", "logdata.txt ������ �������� �ʳ׿�! :(", "���� ����� ��...", "[---���� ��---]\n", "[---��---]\n", "������ �Ͻǰǰ���? \n 1�� �ҵ�, 2�� ����: \n", "����� ���� ���� ���� �ۼ����ּ��� (��): \n", "����� : ", "���� �ۼ��ϼ̳׿�", "������ �����̳� ������ �ۼ����ּ���: \n", "����: ", "����� ����� ���� ���� �ۼ����ּ��� (��): \n", "���� ����ϼ̳׿�", "�ƹ��͵� �޶����� �ʾҳ׿�. Ȥ�� Ű�� �߸� �����Űǰ���? :)"])
    
    elif what_lang == 2:
        LANG.append(["Logging...", "logdata.txt is not exist!", "Making new file...", "[NOW]\n", "[END]\n", "What do you wanna do? \n Type that 1 or 2: \n", "enter the num of you've earned: \n", "You've entered: ", "Won", "Please enter the reason: \n", "reason: ", "enter the num of you've used: \n", "Won", "Nothing Changed! :)"])
    
    else:
        
        print("ERROR! Please enter the num 1 or 2!")
        
        lang()