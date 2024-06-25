import re
from base import baseText
# r'' to use one escape character \
# Meta characters: . ^ $ * + ? { } [ ] \ | ( )
# | OR
# . Any character (except breakline), one character
# [] character set

# regexp = re.compile(r'Hansel|Gretel|adults')
# print(regexp.search(baseText))
print(re.findall(r'Hansel|Gretel|adults', baseText))
print(re.findall(r'Hansel|hansel|Gretel', baseText))
print(re.findall(r'[Hh]ansel|[Ggabc]retel', baseText))
print(re.findall(r'[a-z]retel', baseText))
print(re.findall(r'[a-zA-Z0-9_.]retel|[a-zA-Z0-9]ansel', baseText))
# flags=re.I = case-insensitive
print(re.findall(r'Hansel|Gretel', baseText, flags=re.I))
