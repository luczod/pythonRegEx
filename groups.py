import re
from pprint import pprint
# Meta caracteres: ^ $
# group
# (abc|def) save in memory
# (?:.+?) - ?: no save in memory
# group - variable - retrovisor
# ()     \1
# () ()  \1 \2
# (())()   \1 \2 \3
# (())()   \1( \2(( \3(((

text2 = """
<p>phrase 1</p> <p>slogan</p> <p>any phrase</p> <div>1</div>
"""
# print(re.findall(r'<([dpiv]{1,3})>.+?<\/\1>', text2))
# tags = re.findall(r'(<([dpiv]{1,3})>.+?<\/\2>)', text2)

# (())()   \1 \2 \3
# tags = re.findall(r'(<([dpiv]{1,3})>(.+?)<\/\2>)', text2)
group_name = re.findall(r'<(?P<tag>[dpiv]{1,3})>(.+?)<\/(?P=tag)>', text2)

# \2 raise exception
group_unsave = re.findall(r'<([dpiv]{1,3})>(?:.+?)<\/\1>', text2)

cpf = 'a147.852.963-12a'
# ?: no save in memory
print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))

# r'' to use one escape character \
# replace
print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1 other \3 word \4', text2))

# for tag in tags:
#     one, two, three = tag  # tuple
#     print(three)

pprint(group_name)
