class staff:
    def __init__(self,name,year,working_hours):
        self.name=name
        self.year=year
        self.workiong_hours=working_hours
    
   
    @property
    def staff_name(self):
        return self.name
class drinks:
    def __init__(self,name,money,size):
        self.name=name
        self.money=money
        self.size=size

    def Changr_size(self,size):
        if size not in self.size:
            self.size=size
 
 
    

class ice(drinks):
    def __init__(self,name,money,size,sugur,temperature):
        super().__init__(name,money,size)
        self.temperature=temperature
        self.sugur=sugur
        print("你要的是冰的:{}".format(temperature))

    def Changr_size(self,size):
        if size not in self.size:
            super().Changr_size(size)
            print("已幫你更換大小:{}".format(size))
        else :
            print("已經是{}".format(size))
       


    def Print(self):
           print("你的飲料是{} {} {} {} {}".format(self.name,self.money,self.size,self.sugur,self.temperature))
        

class hot(drinks):
    def __init__(self,name,money,size,sugur,temperature):
        super().__init__(name,money,size)
        self.temperature=temperature
        self.sugur=sugur
        print("你要的是熱的:{}".format(temperature))
    
    def Changr_size(self,size):
        if size not in self.size:
            super().Changr_size(size)
            print("已幫你更換大小:{}".format(size))
        else :
            print("已經是{}".format(size))
       

    def Print(self):
        print("你的飲料是{} {} {} {} {}".format(self.name,self.money,self.size,self.sugur,self.temperature))  


        


text=ice("紅茶",10,"小",3,"微冰")
text.Changr_size("小")
text.Print()
text=hot("奶茶",20,"大",1,"溫",)
text.Changr_size("小")
text.Print()
user=staff("mike",2,40)
print(user.staff_name)
