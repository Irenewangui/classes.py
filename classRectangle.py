class Rectangle:
  length=0
  width=0
  def __init__(self,length,width):
    self.length=length
    self.width=width
    
  def area(self):
    return self.length * self.width
    
  def perimeter(self):
    return 2 * (self.length + self.width)

small = Rectangle(2,3)
large = Rectangle(675,342)
length=int(input("What is the length"))
width=int(input("What is the width"))
custom=Rectangle(length,width)
print("Length and width of smaller {} and {}".format(small.length,small.width))
print("Smaller area ",small.area())
print("Larger area ",large.perimeter())
print("Custom rectangle",custom.area())
