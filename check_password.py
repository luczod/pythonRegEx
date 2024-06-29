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


def add_li_tags(file_path):
    # Read the file and get all lines
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Add <li> tags to each line
    tagged_lines = [f'<li>{line.strip()}</li>' for line in lines]
    """ for line in lines:
        if len(line.strip()) < 1:
            tagged_lines.append(f'{line.strip()}')
        else:
            tagged_lines.append(f'<li>{line.strip()}</li>') """

    # Join the tagged lines into a single string
    result = '\n'.join(tagged_lines)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(result)

    return True  # result


file_path = 'example.txt'
tagged_text = add_li_tags(file_path)
print(tagged_text)
