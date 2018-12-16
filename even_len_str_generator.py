from string import *
from random import randint

word = ""

for n in range(randint(1, 18) * 2):
    word += ascii_letters[randint(0, len(ascii_letters)-1)]

print(word)
print(len(word))