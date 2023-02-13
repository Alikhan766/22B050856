class myClass():
    def __init__(self, string):
        self.str1 = string

    def print_String(self):
        print("Befor:", self.str1)
        print("After:", self.str1.upper())


str1 = myClass("string")
str1.print_String()
