# def read():
#     with open('Lekce_04_19.11.24/soubor.txt', mode='r', encoding='utf-8') as file:
#         # file.read() # - cely soubor
#         # file.readline() # - pouze prvni radek
#         # for line in file:
#         #     print(line)

def write():
    with open ('Lekce_04_19.11.24/test.txt', mode='w', encoding='utf-8') as file:
        file.write('Hello from python lection!')

def append_file():
    with open ('Lekce_04_19.11.24/test.txt', mode='a', encoding='utf-8') as file:
        file.write('\nWhat\'s crackin?')

write()
# append_file()
# read()