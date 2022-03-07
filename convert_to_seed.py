import pybel as babel
import base64
import numpy as np
import os

global ha, sh, wa, vo, on
global count1, count2, count3, count4
global tab1, tab2, tab3, tab4
global numberof, it, reberyfit, rebery_comp, memory
global search, bypass, listchar, triggerdit, reberylist_strings, reberyrange_strings, countchar, strining
global ranging_word, element_wording, elemint, passing_wordone, elements_trigger, roberylist, roberyrange, roberylist_a, roberyrange_a
global list_on, iti, add, string_on, itit, add2, string_on2, tab_on2, pimped, adding

add = 0
add2 = 0
pimped = []
tab_on = []
tab_on2 = []
bypass = 0
adding = 0
ha = 1
sh = 1
wa = 1
vo = 1
count1 = 0
count2 = 0
count3 = 0
count4 = 0

tab4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
tab3 = [32, 33, 34, 35]
tab2 = [35, 36, 37, 38, 39]
tab1 = [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]

string = b"A"
bytesstring = base64.b64encode(string)

choice = input("(1)='Convert Text' (2)='convert file' : ")

if choice == "1":
    strining = input("text to convert : ")
if choice == "2":
    file = input("file to convert (emplcamement) : ")
if not choice == "1" or choice == "2":
    print("mauvaise reponse !")
    pass

on = 0
passing_wordone = 0
elements_trigger = 0
triggerdit = 0
reberylist_strings = ""
reberyrange_strings = ""
countchar = 0
listchar = 0
roberylist = np.array([] * len(strining), dtype=np.int64)
roberylist_a = np.array([] * len(strining), dtype=np.int64)
roberyrange = np.array([] * len(strining), dtype=np.int64)
roberyrange_a = np.array([] * len(strining), dtype=np.int64)

while True:
    search = babel.check(strining, babel.getbook(hexagon=str(ha), shelf=str(sh), wall=str(wa), volume=str(vo)))
    if search == True:
        with open(f"stockage/{ha}-{sh}-{wa}-{vo}.txt", 'w+', newline='\n', encoding='utf-8', buffering=2 ** 10) as filehandle:
            columns = babel.getbook(hexagon=str(ha), shelf=str(sh), wall=str(wa), volume=str(vo))
            filehandle.write(f"{columns}")
            filehandle.close()

        if strining in columns:
            if on == 0:
                print("Found on:" + " -> " + f"hexagon: {ha} || shelf: {sh} || wall: {wa} || volume: {vo}")
                on += 1
        else:
            print("Not Found on:" + " -> " + f"hexagon: {ha} || shelf: {sh} || wall: {wa} || volume: {vo}")
            continue
        columns = babel.getbook(hexagon=str(ha), shelf=str(sh), wall=str(wa), volume=str(vo))
        if not add == 0:
            if elements_trigger == add:
                print("Fin du fichier.. (press CTRL+C to exit)")
                break
        with open(f"stockage/{ha}-{sh}-{wa}-{vo}.txt", 'r', newline='\n', encoding='utf-8', buffering=2 ** 10) as filehandle3:
            list_on = filehandle3.read()
            for iti in range(len(list_on)):
                if not len(list_on) == add:
                    string_on = tab_on.append(list_on[add])
                    add += 1
                else:
                    if len(list_on) == add:
                        print("Fin du fichier..")
                        break
        def charposition(string, char):
            pos = []  # list to store positions for each 'char' in 'string'
            for n in range(len(string)):
                if string[n] == char:
                    pos.append(n)
            return pos
        numberofchar = list(range(len(strining)))
        listing = list(strining)
        listchar += elements_trigger
        passing_counting_word_ = {}
        passing_word_length_ = {}
        passing_wording_ = {}
        for ranging_word in range(len(strining)):
            if ranging_word in passing_counting_word_:
                passing_counting_word_[ranging_word] += 1
                passing_wording_[ranging_word] += 1
                passing_word_length_[ranging_word] += 1
            else:
                passing_counting_word_[ranging_word] = 1
                passing_word_length_[ranging_word] = 1
                passing_wording_[ranging_word] = 1

        listit = countchar
        countchar += 1
        try:
            passing_counting_word_[f"{listit}"] = numberofchar[countchar]
            passing_word_length_[f"{listit}"] = numberofchar[countchar]
            passing_wording_[f"{listit}"] = charposition(columns, listing[countchar])
            for word in range(len(columns)):
                elements_trigger -= int(len(strining) - 1)
                for repeat_work in range(len(listing)):
                    roberylist_a = np.append(roberylist, f"[{columns[listchar + elements_trigger]}]", None)
                    roberyrange_a = np.append(roberyrange, f"{listchar + elements_trigger}", None)
                    elements_trigger += 1
                    if elements_trigger == add:
                        print("Fin du fichier..")
                        break
                    triggerdit += 1
                    reberylist_strings = np.append(reberylist_strings, str(' '.join(roberylist_a).replace("[", "").replace("]", "").replace(" ", "")), None)
                    reberyrange_strings = np.append(reberyrange_strings, str(' '.join(roberyrange_a).replace(" ", ",")), None)
                numberof = len(strining)
                reberyfit = f"{' '.join(reberyrange_strings).replace(' ', '', 1).replace(' ', ', ')}"
                rebery_out = reberyfit.split(', ')
                rebery_comp = [rebery_out[i:i + numberof] for i in range(0, len(rebery_out), numberof)]
                pimp = ' '.join(str(rebery_comp)).replace(' ', '').replace(' ', ', ').replace('[', '').replace(']', '').replace("'", '').replace(',', ', ')
                if ' '.join(reberylist_strings).replace('[', '').replace(']', '').replace(' ', '') == strining:
                    fileName = rf"encoding/{strining}.txt"
                    isExist = os.path.exists(fileName)
                    if isExist != True:
                        for indice in range(len(strining)):
                            with open(f"encoding/{strining}.txt", 'a+', newline='\n', encoding='utf-8', buffering=2 ** 10) as filehandle2:
                                pimped = pimp.split(", ")
                                filehandle2.write(f"[{ha},{sh},{wa},{vo}], " + f"[{pimped[adding]}]" + "\n")
                                print(pimped)
                                print(f"Writing on : 'encoding/{strining}.txt' with line number : {pimped[adding]}")
                                filehandle2.close()
                                adding += 1
                            passing_wordone += 1
                            passing_counting_word_[f"{listit}"] += 1
                            if adding == len(strining):
                                with open(f"encoding/{strining}.txt", 'r', newline='\n', encoding='utf-8', buffering=2 ** 10) as filehandle4:
                                    pimper = filehandle4.read()
                                    strining_fait = base64.b64encode(pimper.encode('utf-8'))
                                    with open(f"seed/{strining}.seed", 'w', newline='\n', encoding='utf-8', buffering=2 ** 10) as filehandle5:
                                        filehandle5.write(f"{strining_fait.decode()}")
                                        print(f"file saved as : 'seed/{strining}.seed'")
                                        filehandle5.close()
                                    filehandle2.close()
                                print("max char obtained quit!!")
                                break
                    else :
                        print("file exist !")
                    break
                else:
                    roberylist = np.delete(roberylist, roberylist, None)
                    roberylist_a = np.delete(roberylist_a, roberylist, None)
                    roberyrange = np.delete(roberyrange, roberyrange, None)
                    roberyrange_a = np.delete(roberyrange_a, roberyrange, None)
                    reberylist_strings = ""
                    reberyrange_strings = ""
            countchar += 1
            listchar += 1
            passing_word_length_[ranging_word] += 1
            pass
        except IndexError:
            print(f"arreté a partire de : {elements_trigger}")
            bypass += 1
            break
        else:
            search = False
            continue
    if search == False:
        if count1 in tab1:
            ha += 1
        if count2 in tab2:
            sh += 1
        if count3 in tab3:
            wa += 1
        if count4 in tab4:
            vo += 1
        print("Not Found on:" + " -> " + f"hexagon: {ha} || shelf: {sh} || wall: {wa} || volume: {vo}")
        pass

    elements_trigger = elements_trigger + int(len(strining) - 1)
    print("bypass : " + f"{bypass}" + " || " + "element_trigger : " + f"{elements_trigger}" + " || " + "trigger : " + f"{triggerdit}")