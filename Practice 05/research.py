import re

# ex 01
re.search(r"\d+", "Заказ №123 и №456")

# ex 02
re.search(r"cat", "A category of cats")

# ex 03
re.search(r"^Hello", "Hello, world!")

# ex 04
re.search(r"price: \d+", "The price: 500 dollars")

# ex 05
re.search(r"\w+@\w+\.\w+", "Email: info@example.com")