# nums = [1,2,3,4,5,6]

# iterate = iter(nums)

# print(iterate.__next__())
# print(iterate.__next__())
# string = "suraj karki"
# iterate = iter(string)

# print(iterate.__next__())
# print(iterate.__next__())
# print(iterate.__next__())
# print(iterate.__next__())
# print(iterate.__next__())
# print(iterate.__next__())
# print(iterate.__next__())
class Fantastic_Five:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 5:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration

ff = Fantastic_Five()

for i in ff:
    print (i)