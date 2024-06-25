# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto
import re

# findall search sub
# compile
# Case sensitivy

string = 'This is a regular test expression test.'
# r'' to use one escape characters
print(re.search(r'This', string))
print(re.findall(r'test', string))
print(re.sub(r'test', 'abcd', string))  # replace

# There is a cost in compiling several regular expressions
# use compile
regexp = re.compile(r'test')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('abcd', string))
