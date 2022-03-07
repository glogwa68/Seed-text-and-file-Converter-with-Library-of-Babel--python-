import pybel as babel
import base64

global ha, sh, wa, vo, on
global count1, count2, count3, count4
global tab1, tab2, tab3, tab4
global search, bypass, listchar, triggerdit, reberylist_strings, reberyrange_strings, countchar
global ranging_word, element_wording, elemint, passing_wordone, elements_trigger, roberylist, roberyrange

bypass = 0
ha = 1
sh = 1
wa = 1
vo = 1
count1 = 0
count2 = 0
count3 = 0
count4 = 0
tab4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
tab3 = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
tab2 = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]
tab1 = [150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200]

string = b"A"

bytesstring = base64.b64encode(string)
#print(str(bytesstring.decode()))

strining = "numero"
#print(strining)
on = 0
passing_wordone = 0
elements_trigger = 0
triggerdit = 0
reberyrange_strings = 0
reberyrange_strings = 0
countchar = 0
listchar = 0
roberylist = []
roberyrange = []

while True:
    search = babel.check(strining, babel.getbook(hexagon=str(ha), shelf=str(sh), wall=str(wa), volume=str(vo)))
    if search == True:
        if on == 0:
            print("Found on:" + " -> " + f"hexagon: {ha} || shelf: {sh} || wall: {wa} || volume: {vo}")
        on += 1

        columns = babel.getbook(hexagon=str(ha), shelf=str(sh), wall=str(wa), volume=str(vo))
        #print(columns)

        with open(f"stockage/{ha}-{sh}-{wa}-{vo}.txt", 'w+', newline='\n', encoding='utf-8', buffering=2 ** 10) as filehandle:
            filehandle.write(f"{columns}")
            filehandle.close()


        def charposition(string, char):
            pos = []  # list to store positions for each 'char' in 'string'
            for n in range(len(string)):
                if string[n] == char:
                    pos.append(n)
            return pos

        numberofchar = list(range(len(strining)))

        listing = list(strining)
        #print(listing[0])

        listchar += int(reberyrange_strings)

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

        reberyrange_strings = int(reberyrange_strings) + int(reberyrange_strings)
        listit = int(ranging_word)
        countchar += int(reberyrange_strings)
        #print(f"{reberyrange_strings}")

        try:
            passing_counting_word_[f"{listit}"] = numberofchar[countchar]
            passing_word_length_[f"{listit}"] = numberofchar[countchar]
            passing_wording_[f"{listit}"] = charposition(columns, listing[countchar])

            #print(passing_wording_[listit])

            try:
                for word in range(len(columns)):
                    for element_wording in columns[listchar]:
                            if element_wording == columns[listchar]:
                                for repeat_work in range(len(listing)):
                                    try:
                                        roberylist.append(f"[{columns[listchar + elements_trigger]}]")
                                        roberyrange.append(f"{listchar + elements_trigger}")
                                        elements_trigger += 1
                                        triggerdit += 1
                                    except IndexError:
                                        bypass += 1
                                reberylist_strings = str(' '.join(roberylist).replace("[", "").replace("]", "").replace(" ", ""))
                                reberyrange_strings = str(' '.join(roberyrange).replace(" ", ","))
                                # print(' '.join(roberylist).replace("[", "").replace("]", "").replace(" ", ""))
                                # print(' '.join(roberyrange).replace(" ", ","))
                                #print(f"[{columns[listchar]}, {element_wording}]")
                                if ' '.join(roberylist).replace("[", "").replace("]", "").replace(" ", "") == strining:
                                    elemint = f"[{' '.join(roberyrange).replace(' ', ',')}]"
                                    for indice in range(len(strining)):
                                        with open(f"encoding/{strining}.txt", 'a+', newline='\n', encoding='utf-8', buffering=2 ** 10) as filehandle2:
                                            filehandle2.write(f"{listing[passing_wordone]}, " + f"[{ha},{sh},{wa},{vo}], " + f"[{elemint}]" + "\n")
                                            filehandle2.close()
                                        passing_wordone += 1
                                        passing_counting_word_[f"{listit}"] += 1
                                    print(f"Writing on : 'encoding/{strining}.txt'")
                                    break
                                else:
                                    roberyrange.clear()
                                    roberylist.clear()

                            #print(f"{element_wording}")
                    countchar += 1
                    listchar += 1
                    elements_trigger = 0
                    passing_word_length_[ranging_word] += 1
                    pass
            except IndexError:
                bypass += 1
        except IndexError:
            bypass += 1

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


    print("bypass : " + f"{bypass}" + " || " + "trigger : " + f"{triggerdit}" + " || " + f"{reberylist_strings}" + " || " + f"{reberyrange_strings}")
