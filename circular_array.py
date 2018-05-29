# Circular Array (GLM 7.9 pm 128):
# Implement a CircularArray class that supprots an array-like data structure
# which can be efficiently rotated. If possible, the class should use a generic type and 
# should support iteration via the standard notation:
#   for o in circularArray 

class CircularArray:    
    def __init__(self):
        self.__cursor = 0
        self.a = []

    def get_array(self):
        return self.a[self.__cursor:] + self.a[0:self.__cursor]

    """
    [1, 2, 3] + [4, 5] = [3, 1, 2, 4, 5] = OR = [4, 5, 3, 1, 2]
           ^              ^                            ^
    """
    def extend(self, elts):
        self.a = self.get_array()
        self.__cursor = 0
        return self.a.extend(elts)

    def rotate(self, N):
        self.__cursor = (self.__cursor - N) % len(self.a)
        self.__cursor =  (self.__cursor + len(self.a)) % len(self.a)

    def __str__(self):
        return str(self.get_array())
    
def test():
    a = CircularArray()

    print("empty case: %s" % ( [] == a.get_array() ))

    a.extend([1, 2, 3])    
    print("123 case: %s" % ( [1, 2, 3] == a.get_array() ))

    a.rotate(2)
    print("rotate by 2 case: %s" % ( [2, 3, 1] == a.get_array() ))
    print("a.rotate(2) = %s" % (a))

    a.extend([4, 5])
    a.rotate(-1)
    print("rotate by -1 after adding 4,5  case: %s" % ( [3, 1, 4, 5, 2] == a.get_array() ))
    print("a.rotate(-1) = %s" % (a))    

test()
    
