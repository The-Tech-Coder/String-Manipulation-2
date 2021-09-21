class stringManipulation():
    def toCapital(string):
        a = string.capitalize()
        return a

    def toCount(string):
        b = string.count("a")
        return b

    def toCheck(string):
        c = string.isalpha()
        return c

    def toend(string):
        z = string.endswith("World")
        return z

print(stringManipulation.toCapital("diego garcia"))
print(stringManipulation.toCount("alexandra daddario"))
print(stringManipulation.toCheck("Absdbhk"))
print(stringManipulation.toCheck("Abs156k"))
print(stringManipulation.toend("Green World, Clean World"))
print(stringManipulation.toend("Green World, Clean World ."))
