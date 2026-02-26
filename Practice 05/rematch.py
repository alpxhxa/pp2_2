import re

# ex 01
re.match(r"Start", "Start of the line")

# ex 02
re.match(r"\d{3}", "123-456-789")

# ex 03
re.match(r"http", "https://example.com")

# ex 04
re.match(r"[A-Z]", "Python")

# ex 05
re.match(r"User_\d", "User_1 logged in")