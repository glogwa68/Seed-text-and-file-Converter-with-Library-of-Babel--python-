import pybel as babel
import base64
import numpy as np

global ha, sh, wa, vo, on
global count1, count2, count3, count4
global tab1, tab2, tab3, tab4
global numberof, it, reberyfit, rebery_comp, memory
global search, bypass, listchar, triggerdit, reberylist_strings, reberyrange_strings, countchar, strining
global ranging_word, element_wording, elemint, passing_wordone, elements_trigger, roberylist, roberyrange, roberylist_a, roberyrange_a
global list_on, iti, add, string_on, itit, add2, string_on2, tab_on2

add = 0
add2 = 0
tab_on = []
tab_on2 = []
bypass = 0
ha = 1
sh = 1
wa = 1
vo = 1
count1 = 0
count2 = 0
count3 = 0
count4 = 0
#tab4 = [range(1, 32)]
#tab3 = [range(1, 4)]
#tab2 = [range(1, 5)]
#tab1 = [range(0, 10)]

tab4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
tab3 = [32, 33, 34, 35]
tab2 = [35, 36, 37, 38, 39]
tab1 = [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]

string = b"A"

bytesstring = base64.b64encode(string)
#print(str(bytesstring.decode()))

strining = input("Quel est le mots que vous voulez transformé : ")
#print(strining)
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
        #print(columns)

        if not add == 0:
            if elements_trigger == add:
                print("Fin du fichier..")
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
        #print(listing[0])

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
        #print(f"{reberyrange_strings}")
        try:
            passing_counting_word_[f"{listit}"] = numberofchar[countchar]
            passing_word_length_[f"{listit}"] = numberofchar[countchar]
            passing_wording_[f"{listit}"] = charposition(columns, listing[countchar])
            for word in range(len(columns)):
                #print(elements_trigger, triggerdit)
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
                    #print(reberyrange_strings)

                numberof = len(strining)
                reberyfit = f"{' '.join(reberyrange_strings).replace(' ', '', 1).replace(' ', ', ')}"
                rebery_out = reberyfit.split(', ')
                rebery_comp = [rebery_out[i:i + numberof] for i in range(0, len(rebery_out), numberof)]
                #print(rebery_comp)
                #print(f"{roberylist_a} : {roberyrange_a}")
                #print(f"[{columns[listchar + elements_trigger]}]" + " : " + f"{listchar + elements_trigger}")
                pimp = ' '.join(str(rebery_comp)).replace(' ', '').replace(' ', ', ').replace('[', '').replace(']', '').replace("'", '').replace(',', ', ')
                #if elements_trigger == [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000, 1100000, 1200000, 1300000, 1400000]:
                #print(f"{' '.join(reberylist_strings).replace('[', '').replace(']', '').replace(' ', '')}" + "  :  " + f"{pimp}")
                #print(f"[{columns[listchar]}, {element_wording}]")
                if ' '.join(reberylist_strings).replace('[', '').replace(']', '').replace(' ', '') == strining:
                    for indice in range(len(strining)):
                        with open(f"encoding/{strining}.txt", 'a+', newline='\n', encoding='utf-8', buffering=2 ** 10) as filehandle2:
                            filehandle2.write(f"{listing[passing_wordone]}, " + f"[{ha},{sh},{wa},{vo}], " + f"[{pimp}]" + "\n")
                            filehandle2.close()
                        passing_wordone += 1
                        passing_counting_word_[f"{listit}"] += 1
                    print(f"Writing on : 'encoding/{strining}.txt'")
                    break
                else:
                    #print(' '.join(reberylist_strings).replace('[', '').replace(']', '').replace(' ', ''))
                    roberylist = np.delete(roberylist, roberylist, None)
                    roberylist_a = np.delete(roberylist_a, roberylist, None)
                    roberyrange = np.delete(roberyrange, roberyrange, None)
                    roberyrange_a = np.delete(roberyrange_a, roberyrange, None)
                    reberylist_strings = ""
                    reberyrange_strings = ""

            #print(f"{element_wording}")
            countchar += 1
            listchar += 1
            passing_word_length_[ranging_word] += 1
            pass
        except IndexError:
            print(f"arreté a partire de : {elements_trigger}")
            bypass += 1
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
    #print("bypass : " + f"{bypass}" + " || " + "element_trigger : " + f"{elements_trigger}" + " || " + "trigger : " + f"{triggerdit}" + " || " + f"{reberylist_strings}" + " || " + f"{reberyrange_strings}")
    print("bypass : " + f"{bypass}" + " || " + "element_trigger : " + f"{elements_trigger}" + " || " + "trigger : " + f"{triggerdit}")