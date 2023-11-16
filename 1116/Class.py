class round:
  def __init__(self,side,length,width,radius):
    self.side=side
    self.length=length
    self.width=width
    self.radius=radius
  #!Calculate the area of ​​a square and print
  def getSquareArea(self):
    print("square =" ,self.side*self.side)
  #!Calculate the area of ​​a rectangle and print
  def getRectangleArea(self):
    print("rectangle =",self.length*self.width)
  #!Calculate the area of ​​a circle and print
  def getCircleArea(self):
    print("circle =",pow(self.radius,2)*3.14)
  #!Another way to write
  # def __str__(self):
  #   return f"square ={self.side*self.side}\nrectangle={self.length*self.width}\ncircle={pow(self.radius,2)*3.14}"

    
p1=round(5,5,5,5)
p1.getSquareArea()
p1.getRectangleArea()
p1.getCircleArea()
# print(p1)
