#Container
#fullness:float [0;1]
#content:string
#def __str__(): "container is almost full" || "container is almost empty"


class Container():
    def __init__(self,full,cont):
        self.fullness = full
        self.content = cont

    def __str__(self):
        if self.fullness>.5:
            return "container is almost full"
        else:
            return "conainer is almost empty"




c1 = Container(0.6,"oil")

print(c1)