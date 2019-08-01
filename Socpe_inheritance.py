#inheritance  with self.xyz could be used in the main function with classname.xyz
# as in example - class differnce can directly use d.maximunDifference as it is vaild in the scope
#Source-https://www.hackerrank.com/challenges/30-scope/problem

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maxDifference=0
    
    def computeDifference(self):
        smallest = 101
        largest = 0
        for element in self.__elements:
            if element>largest:
                largest=element
            if element<smallest:
                smallest=element
        self.maximumDifference=largest-smallest

	# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
