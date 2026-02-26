import re

# ex 01
re.findall(r"\d+", "10 apples, 20 oranges, 30 bananas")

# ex 02
re.findall(r"[A-Z]\w+", "London is the capital of Great Britain")

# ex 03
re.findall(r"#[a-z]+", "Post with #python #regex #code")

# ex 04
re.findall(r"\b\w{3}\b", "The quick brown fox jumps")

# ex 05
re.findall(r"\d{2}:\d{2}", "Time: 12:30, 14:45, 18:00")