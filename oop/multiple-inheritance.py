# note, multiple inheritance is rarely, if ever, useful
# this is just an example on how to use if in case
# we ever find a use case for it
class ClassA:
    def hi(self):
        print("Hello")


class ClassB:
    def hi(self):
        print("Hey")

    def another(self):
        print("From ClassB")


class ClassC(ClassA, ClassB):
    pass


class ClassD(ClassB, ClassA):
    pass


# in multiple inheritance, the child class finds the
# first defined method/variable in its list of inheritances
c = ClassC()
c.hi()  # "Hello"
c.another()  # "From class B"

d = ClassD()
d.hi()  # "Hey"
d.another()  # "From class B"
