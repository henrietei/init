class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age

  def myfunc(self):
    print("Čau, mani sauc ", self.name)

p1=Person("Jānis",36)
print(p1.name)
print(p1.age)
p1.myfunc()