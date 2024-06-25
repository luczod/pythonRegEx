import re
# Meta caracteres: ^ $
# ^ start
# $ end
# [^a-z] -> Any character except [a-z]
# + 1 or n

cpf = ' 147.852.963-12a'
# ?: no save in memory
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))
# output: []
print(re.findall(r'[^0-9]+', cpf))
