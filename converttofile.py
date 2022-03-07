import base64
import pybel as babel

global typo, tab
typo = 0
tab = []

inputing = input("[file name].seed name in seed/ : ")

with open(f"seed/{inputing}.seed", 'r', newline='\n', encoding='utf-8', buffering=2 ** 10) as filehandle0:
    base64_str = filehandle0.read()

printing = base64.b64decode(base64_str)
with open(f"decoding/{base64_str}.txt", 'w', newline='\n', encoding='utf-8', buffering=2 ** 10) as filehandle1:
    filehandle1.write(printing.decode())
    filehandle1.close()


with open(f"decoding/{base64_str}.txt", 'r', newline='\n', encoding='utf-8', buffering=2 ** 10) as filehandle2:
    contenu = filehandle2.read()
    contenu = contenu.split('\n')
    for i in range(len(contenu)):
        with open(f"decoding/{base64_str}.txt", 'r', newline='\n', encoding='utf-8', buffering=2 ** 10) as filehandle3:
            contenu = filehandle3.readlines(typo)
            tab.append(contenu)
            typo += 1
    filehandle2.close()

print(str(', '.join(str(' '.join(str(tab).replace("n", ""))).replace("[", "").replace("]", "").replace(" ", "").replace(",", "").replace("'", "")).replace(" ", " [")).replace(",", "],").replace(", [\], ", " - "))
tab.clear()