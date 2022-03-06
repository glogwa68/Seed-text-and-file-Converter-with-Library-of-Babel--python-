global list_on, iti, add, string_on

add = 0
tab_on = []

with open('1-1-1-1.txt', 'r', newline='\n', encoding='utf-8', buffering=2 ** 10) as filehandle3:
    list_on = filehandle3.read()
    for iti in range(len(list_on)):
        string_on = tab_on.append(list_on[add])
        add += 1

print(add)