import os

# Узнаем, где мы
print(f"Я тут: {os.getcwd()}")

# Создаем цепочку папок
os.makedirs("test_folder/sub_folder", exist_ok=True) 

# Посмотрим, что внутри текущей папки
print(os.listdir("."))