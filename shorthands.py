# [a-z] - ascii table
# \w  include mandarin alphabet and _
# \w  re.A or re.ASCII = [a-zA-Z0-9_]
# \W  negative
# \d  [0-9]
# \D  [^0-9]
# \s  [\r\n\f\n\t]]
# \b  border white space
# \B  border some characater
import re
from base import baseText

# flags=re.I = ignore case
# print(re.findall(r'[a-z]+', baseText, flags=re.I))
# print(re.findall(r'[a-zA-Z0-9À-ú]+', baseText))
# print(re.findall(r'\w+', baseText))
# print(re.findall(r'\w+', baseText, flags=re.A))
# print(re.findall(r'\W+', baseText, flags=re.A))
print(re.findall(r'\bflo\w+', baseText, flags=re.A))
print(re.findall(r'flo\B', baseText, flags=re.A))
print(re.findall(r'\b\w{4}\b', baseText, flags=re.A))
