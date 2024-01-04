class chicken:
    def __init__(self,name,ID,money,hot,size):
        self.name=name
        self.ID=ID
        self.money=money
        self.hot=hot
        self.size=size
        self.client=[]
        self.client_money={}
          
    def buy(self,name,client_money):
        if name in self.name:
            self.client.append(name)
            self.client_money=client_money-self.money
            print("你買了{}你剩{}".format(name,self.client_money))

            

    def retreat(self,name):
        if name in self.name:
            self.client.remove(name)
            print("已經幫退了{},需要給你{}".format(name,self.money))


    def change_hot(self,name,hot):
        if name in self.name:
            print("你要把{}改成{}".format(name,hot))
            self.hot=hot

   
text=chicken("leg",1,20,"小辣","小")
text1=chicken("chest",2,35,"不辣","小")
text2=chicken("heart",3,5,"不辣","大")
text.buy("leg",100)
text1.buy("chest",50)
text2.buy("heart",10)
text.retreat("leg")
text1.retreat("chest")
text2.retreat("heart")
text.change_hot("leg","大辣")
text1.change_hot("chest","大辣")
text2.change_hot("heart","大辣")

