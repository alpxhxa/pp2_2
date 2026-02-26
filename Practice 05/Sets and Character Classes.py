import re

# ex 01
re.findall(r"[аеёиоуыэюя]", "молоко")

# ex 02
re.findall(r"[a-c]", "apple bear cat dog")

# ex 03
re.findall(r"[^0-9]", "ID: 42")

# ex 04
re.findall(r"[0-5][0-9]", "Время 15:65")

# ex 05
re.findall(r"[a-zA-Z]", "Python 3")