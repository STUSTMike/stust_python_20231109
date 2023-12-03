class duel:
    def __init__(sefl,name,age,attack,shield,HP,MP):
        sefl.name=name
        sefl.age=int(age)
        sefl.attack=int(attack)
        sefl.shield=int(shield)
        sefl.HP=int(HP)
        sefl.MP=int(MP)
        print(name,age,attack,HP,MP)

class PK(duel):
        def __init__(sefl, name, age, attack, shield, HP, MP):
            super().__init__(name, age, attack, shield, HP, MP) 
            i=1
            while(HP>0 or x.HP>0):
                print("第{}回合".format(i))  
                HP=HP-x.attack
                print(name,age,attack,HP,MP)
                x.HP=x.HP-attack
                print(x.name,x.age,x.attack,x.HP,x.MP)
                i+=1
                if(HP<=0 or x.HP<=0):
                    break
              
            if(x.HP<=0):
                print("{}死了".format(x.name))
            else:
                print("{}死了".format(name))

class P1(duel):
     pass

class P2(duel):
     pass

text=input("請輸入挑戰者資料:")
text_splut=text.split(",")
a=[]
for i in text_splut:
   a.append(i)
   
# for i in a:
#   print(i)
# 苦力怕,10,50,5,100,10
# a= list(map(int, a))
x=duel(a[0],a[1],a[2],a[3],a[4],a[5])
p=PK("女巫",20,10,10,200,20)




    