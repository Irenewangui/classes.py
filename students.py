class Student:
  name = "Jane Doe"
  def __init__(self,name):
    self.name= name
    
  def get_name(self):
    return self.name
    
  def welcome(self):
    return "Welcome {} to Akirachix".format(self.name)
fatma = Student("Fatma Mohamed")
print(fatma.welcome())
# constructor