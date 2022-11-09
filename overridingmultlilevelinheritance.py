class parent1():
    def show(self):
        print("Inside Parent1")

class parent2():
    def display(self):
        print("Inside parent2")

class Child(parent1,parent2):

    def show(self):
        print("Inside Child")

obj = Child()
obj.show()
obj.display()