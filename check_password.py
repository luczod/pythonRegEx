# https://regex101.com/r/W4kRV2/2/
# https://en.wikipedia.org/wiki/List_of_Unicode_characters

# * 0 or n
# . Any character (except breakline), one character
# ?= Positive lookahead
# () group
# re.M -> Multiline
import re

strong_pw_regexp = re.compile(
    r'^'
    r'(?=.*[a-z])'
    r'(?=.*[A-Z])'
    r'(?=.*[0-9])'
    r'(?=.*[ -\/:-@[-`{-~])'
    r'.{12,}'
    r'$',
    flags=re.M)
