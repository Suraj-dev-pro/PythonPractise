class person:
    #init method or constructor
    def __init__(self,name):
        self.name = name

    #sample method
    def say_hi(self):
        print("Hello my name",self.name)

    #creating different objects
p1 = person("Nikhil")
p2 = person("Abhinav")
p3 = person("Anshul")

p1.say_hi()
p2.say_hi()
p3.say_hi()