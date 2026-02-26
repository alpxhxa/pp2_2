import re

# ex 01
re.findall(r"к.т", "кот кит кат крт")

# ex 02
re.findall(r"^Apple", "Apple Pie")

# ex 03
re.findall(r"end$", "This is the end")

# ex 04
re.findall(r"пицца|суши", "Я люблю пицца и суши")

# ex 05
re.findall(r"\.", "Сайт google.com")