import base64
import pybel as babel

global typo, tab
typo = 0
tab = []

inputing = input("seed : ")
printing = base64.b64decode(inputing)
with open(f"decoding/{inputing}.txt", 'w', newline='\n', encoding='utf-8', buffering=2 ** 10) as filehandle:
    filehandle.write(printing.decode())
    filehandle.close()


with open(f"decoding/{inputing}.txt", 'r', newline='\n', encoding='utf-8', buffering=2 ** 10) as filehandle2:
    contenu = filehandle2.read()
    contenu = contenu.split('\n')
    #print(contenu)
    for i in range(len(contenu)):
        with open(f"decoding/{inputing}.txt", 'r', newline='\n', encoding='utf-8', buffering=2 ** 10) as filehandle3:
            contenu = filehandle3.readlines(typo)
            tab.append(contenu)
            typo += 1
    filehandle2.close()

print(tab)
tab.clear()