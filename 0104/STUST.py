class staff:
    def __init__(self,name,year,working_hours):
        self.name=name
        self.year=year
        self.workiong_hours=working_hours
    
   
   #顯示
    @property
    def staff_name(self):
        return self.name
    @property
    def staff_year(self):
        return self.year
    @property
    def staff_working_hours(self):
        return self.workiong_hours


#飲料屬性
class drinks:
    def __init__(self,name,money,size):
        self.name=name
        self.money=money
        self.size=size

    #如果大小不一樣更改size
    def Changr_size(self,size):
        if size not in self.size:
            self.size=size
 
 
    
#冰的繼承drinks
class ice(drinks):
    def __init__(self,name,money,size,sugur,temperature):
        #呼叫drinks的init
        super().__init__(name,money,size)
        self.temperature=temperature
        self.sugur=sugur
        print("你要的是冰的:{}".format(temperature))
    #更換大小被
    def Changr_size(self,size):
        if size not in self.size:
            #這邊呼叫母的函式
            super().Changr_size(size)
            print("已幫你更換大小:{}".format(size))
        else :
            print("已經是{}".format(size))
       

    #顯示
    def Print(self):
           print("你的飲料是{} {} {} {} {}".format(self.name,self.money,self.size,self.sugur,self.temperature))
        
#溫的繼承drinks
class hot(drinks):
    def __init__(self,name,money,size,sugur,temperature):
         #呼叫drinks的init
        super().__init__(name,money,size)
        self.temperature=temperature
        self.sugur=sugur
        print("你要的是熱的:{}".format(temperature))
     #更換大小被
    def Changr_size(self,size):
        if size not in self.size:
             #這邊呼叫母的函式
            super().Changr_size(size)
            print("已幫你更換大小:{}".format(size))
        else :
            print("已經是{}".format(size))
       
    #顯示
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
