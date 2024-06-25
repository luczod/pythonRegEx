import re
from base import baseText
# r'' to use one escape character \
# Meta characters: ^ $ ( )

# Quantifiers - Apply to the left
# * 0 or n
# + 1 or n
# ? 0 or 1
# {n}
# {min,max}
# {10,} 10 to n
# {,10} 0 to 10
# {5,10} 5 to 10
# {10} 10

# regexp = re.compile(r'Hansel')
# flags=re.I = case-insensitive

print(re.findall(r'Ha+nsel+', baseText, flags=re.I))
print(re.findall(r'Ha{1,}nsel{1,}', baseText, flags=re.I))
print(re.findall(r'Ha{1,}nsel', baseText, flags=re.I))
print(re.findall(r'co{3}m{1,2}e', baseText, flags=re.I))

text2 = "love and loved"
print(re.findall(r'lov[ed]{2}', baseText))
print(re.findall(r'lov[ed]*', baseText))
