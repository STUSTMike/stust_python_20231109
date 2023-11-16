class round:
  def __init__(self,side,length,width,radius):
    self.side=side
    self.length=length
    self.width=width
    self.radius=radius
  def square(self):
    print("square = " ,self.side*self.side)
  def rectangle(self):
    print("rectangle = ",self.length*self.width)
  def circle(self):
    print("round =" ,pow(self.radius,2)*3.14)
    
p1=round(5,5,5,5)
p1.square()
p1.rectangle()
p1.circle()
