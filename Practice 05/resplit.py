import re

# ex 01
re.split(r"\s+", "Word1    Word2 Word3")

# ex 02
re.split(r"[,;.]\s*", "apple, banana; orange. cherry")

# ex 03
re.split(r"-", "12-34-56-78")

# ex 04
re.split(r"[0-9]+", "Page1Section2Item3")

# ex 05
re.split(r"[:/]", "https://google.com/search")