import re

# ex 01
re.findall(r"python", "PYTHON python PyThOn", re.IGNORECASE)

# ex 02
re.findall(r"^\w+", "First\nSecond", re.MULTILINE)

# ex 03
re.findall(r"A.*B", "A\nB", re.DOTALL)

# ex 04
re.findall(r"\d+", "123\n456", re.VERBOSE)

# ex 05
re.findall(r"^apple", "APPLE\napple", re.IGNORECASE | re.MULTILINE)