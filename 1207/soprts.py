class soprts:
    def __init__(self,name):
        self._name=name

    def practice(self):
        print("Doing soprrs pracitce")
    @property
    def soprts_name(self):
        return self._name
    
    @soprts_name.setter
    def soprts_name(self,value):
        print(f'"{self._name}"is now"{value}".')
        self._name=value

    @soprts_name.deleter
    def soprts_name(self):
        print(f'"{self._name}" was deleter.')
        del self._name

####################################################################
class land(soprts):
    def __init__(self,name,field):
     super().__init__(name)
     self.field=field

    # def ball(self):
    #     print("sports is: ball ")

    # def notball(self):
    #     print("sports is: notball ")

    def practice(self):
        print("Doing land soprrs pracitce")
    @property
    def soprtsland_field(self):
        return self.field

    @soprtsland_field.setter
    def soprtsland_field(self,value):
        print(f'"{self.field}"is now"{value}".')
        self.field=value
    
################################################################    
class water(soprts):
    def __init__(self,name,activity):
     super().__init__(name)
     self.activity=activity

    # def pool(self):
    #     print("sports is: pool")

    # def ocean(self):
    #     print("sports is: ocean")

    def practice(self):
        print("Doing water soprrs pracitce")

    @property
    def soprtswater_activity(self):
        return self.activity

    @soprtswater_activity.setter
    def soprtswater_activity(self,value):
        print(f'"{self.activity}"is now"{value}".')
        self.activity=value
#####################################################################

if __name__=="__main__":

    baseball=land("baseball","baseball field")
    print(baseball.soprts_name)
    print(baseball.soprtsland_field)
    baseball.practice()
    print("#################################################")

    water_skiing=water("water skiing","strap on your skis and fly across the water")
    print(water_skiing.soprts_name)
    print(water_skiing.soprtswater_activity)
    water_skiing.practice()
    print("##################################################")

    Soprts=soprts("ball")
    Soprts.practice()