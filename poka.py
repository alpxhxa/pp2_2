import re

def pars():

    days = []

    with open("raw.txt","r") as file:

        source = file.read()
        print(source)

        days.append(re.findall(r"1,000",source))

    for i in days:
        print(i)

pars()