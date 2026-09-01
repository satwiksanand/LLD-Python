# The ability of different objects to be treated as instances of the same class through a common interface,
# allowing them to respond to the exact same action or command in their own unique way.
# The word literally translates to "many forms."

# here showing method overriding and the diamond problem.

class Base:
    def process(self):
        print("process function of the Base Class")

class ChildA(Base):
    def process(self):
        print("process function of the ChildA class")

class ChildB(Base):
    def process(self):
        print("process function of the ChildB class")

class GrandChild(ChildA, ChildB):
    def process(self):
        print("process function of the grand child class")

if __name__ == "__main__":
    obj = GrandChild()
    obj.process()
    print(GrandChild.__mro__)