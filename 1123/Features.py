class duel:
    def __init__(sefl,name,age,attack,shield,HP,MP):
        sefl.name=name
        sefl.age=age
        sefl.attack=attack
        sefl.shield=shield
        sefl.HP=HP
        sefl.MP=MP
        print(name,age,attack,HP,MP)

class PK(duel):
        def __init__(sefl, name, age, attack, shield, HP, MP):
            super().__init__(name, age, attack, shield, HP, MP) 
            while(HP>0 or x.HP>0):
                # print("第{}回合".format(i))
                HP=HP-x.attack
                print(name,age,attack,HP,MP)
                x.HP=x.HP-attack
                print(x.name,x.age,x.attack,x.HP,x.MP)
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

x=duel("苦力怕",10,50,10,100,5)
p=PK("女巫",20,10,10,200,20)




    