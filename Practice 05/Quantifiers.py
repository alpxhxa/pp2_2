import re

# ex 01
re.findall(r"lo*", "l lo loo looo")

# ex 02
re.findall(r"\d+", "Номер 123 и 45")

# ex 03
re.findall(r"apples?", "I have one apple and two apples")

# ex 04
re.findall(r"\d{4}", "Год 2024, день 15")

# ex 05
re.findall(r"a{2,4}", "a aa aaa aaaa aaaaa")