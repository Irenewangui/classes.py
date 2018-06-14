class Triangle:
  base=0
  height=0
  hypotenuse=0
  # def(self,base,height,hypotenuse):
  #   self.base=base
  #   self.height=height
  #   self.hypotenuse=hypotenuse
    
  def area(self):
    return 0.5* float(self.base*self.height)
    
  def perimeter(self):
    return self.base + self.height + self.hypotenuse
    
base =int(input("What is the base")) 
height =int(input("What is the Height"))
hypotenuse=int(input("What is the Hypotenuse"))
triangle= Triangle(base,height,hypotenuse)
print ("Area of the right angle", triangle.area())
print("Perimeter of the triangle",triangle.perimeter())