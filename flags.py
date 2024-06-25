# re.A -> ASCII
# re.I -> IGNORECASE
# re.M -> Multiline -> ^ $
# re.S -> . include breakline
# * 0 or n
# . Any character (except breakline), one character
import re

text = '''
131.768.460-53
055.123.060-50
955.123.060-90
'''

text2 = '''to touch or grasp by extending a part of the body
(such as a hand) or an object'''

# print(re.findall(r'''^\d{3}\.\d{3}\.\d{3}\-\d{2}$', text, flags=re.M))

print(re.findall(r'^t.*t$', text2, flags=re.I | re.S))
