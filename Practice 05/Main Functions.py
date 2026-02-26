import re

# ex 01
match = re.search(r"\d+", "Заказ №123 и №456")

# ex 02
re.findall(r"\w+", "Hello, world!")

# ex 03
re.split(r"\s*,\s*", "apple,  banana,orange")

# ex 04
re.sub(r"скрыто", "***", "Ваш пароль: скрыто")

# ex 05
re.match(r"Python", "Python - круто")