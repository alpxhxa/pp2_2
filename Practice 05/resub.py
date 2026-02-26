import re

# ex 01
re.sub(r"red", "blue", "The red car and red house")

# ex 02
re.sub(r"\d+", "NUMBER", "ID: 123, Code: 456")

# ex 03
re.sub(r"\s+", "_", "Text with many spaces")

# ex 04
re.sub(r"[^a-zA-Z]", "", "Phone: +1(234)-567")

# ex 05
re.sub(r"bad", "good", "This is a bad day", count=1)