import math

class Circle:
  radius=0
  def __init__(self,radius):
    self.radius=radius


  def validateDimension(self):
      try:
          self.width = float(self.radius)
      except ValueError:
        raise ValueError ("Radius provided is invalid")

  def area(self):
    return self.radius * self.radius * math.pi


# radius=int(input("What is the radius"))
# circle= Circle(radius)
# print("Area of the Circle is",circle.area())
# print("Perimeter of the Circle is",circle.perimeter())