# \d  [0-9]
# {10} 10
# re.X - comment in regex
# () group
# ?: no save in memory
# ^ start
# $ end
# \b  border white space
import re
# 0.0.0.0 255.255.255.255
# 025.258.963-10 02525896310

# https://regex101.com/r/lWVPOr/1
cpf = '025.258.963-10'
cpf_reg_exp = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', flags=0)

ip_rex_exp = re.compile(r"""
                        ^(?:
                            (?:
                                25[0-5] | # 250-255
                                2[0-4][0-9] | # 250-255
                                1[0-9]{2} | # 100-199
                                [1-9][0-9] | # 10-99
                                [0-9] # 0-9
                            )\.?
                        ){4}\b$
                        """,
                        flags=re.X)

ip_exp = re.compile(
    r'^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.?){4}\b$')

for i in range(301):
    ip = f'{i}.{i}.{i}.{i}'
    print(ip, ip_exp.findall(ip))
