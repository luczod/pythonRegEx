# \d  [0-9]
# \D  [^0-9]
# \s  white space - [\r\n\f\n\t]]
# \w  [a-zA-Z0-9_] and more
# . Any character (except breakline), one character
# + 1 or n
#  Lookahead and lookbehind, only check, no return
import re
from pprint import pprint

text = '''
ONLINE  192.168.0.1 GHIJK active
OFFLINE  192.168.0.2 GHIJK inactive
OFFLINE  192.168.0.3 GHIJK active
ONLINE  192.168.0.4 GHIJK active
ONLINE  192.168.0.5 GHIJK inactive
OFFLINE  192.168.0.6 GHIJK active
'''

# ?= Positive lookahead - after \s+
# pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)', text))

# ?! Negative lookahead - after \s+
# pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)', text))
# pprint(re.findall(r'(?=.*[^in]active).+', text))

# ?<= Positive lookbehind - behind \s+
# pprint(re.findall(r'\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', text))

# ?<! Negative lookbehind - behind \s+
pprint(re.findall(r'\w+(?<!ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', text))
