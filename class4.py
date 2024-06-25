import re
# Meta characters: ^ $ ( )

# Greedy non-greedy/lazy
# * 0 or n
# + 1 or n
# ? 0 or 1
# . Any character (except breakline), one character

text2 = """
<p>phrase 1</p> <p>slogan</p> <p>any phrase</p> <div></div>
"""
print(re.findall(r'<[dpiv]{1,3}>', text2))
print(re.findall(r'<[dpiv]{1,3}>.*', text2))
# r'' to use one escape character \
print(re.findall(r'<[dpiv]{1,3}>.*<\/[dpiv]{1,3}>', text2))  # Greedy
print(re.findall(r'<[dpiv]{1,3}>.*?<\/[dpiv]{1,3}>', text2))  # non-greedy
print(re.findall(r'<[dpiv]{1,3}>.+?<\/[dpiv]{1,3}>', text2))
