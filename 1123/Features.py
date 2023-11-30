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
            while(HP!=0):
                HP=HP-sefl.attack
                print(name,age,attack,HP,MP)
x=duel("騎士",10,20,15,100,5)
p=PK("女巫",20,10,10,200,20)


    