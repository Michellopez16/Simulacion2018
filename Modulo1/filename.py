# %load welcome.py
# programa de bienvenida.
# Created by Lázaro Alonso.
from time import sleep
def print_words(sentence):
    for word in sentence.split():
        for l in word:
            sleep(.05)
            print(l, end = '')
        print(end = ' ')
sentence1 = 'Hola, bienvenida o bienvenido a simulación matemática.'
print_words(sentence1)
