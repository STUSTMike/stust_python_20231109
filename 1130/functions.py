class student:
    # 類別屬性
    # School="南台科技大學"
    # address="南台街一號"
    # def __ini__ (self,id,major,credits,gpa,address):
    #     self._id=id
    #     self._major=major
    #     self._credits=credits
    #     self._gpa=gpa
    #     self.address=address
    # def get_id(self)
    #     return self._id
    # def set_id(self,value)
    #     self._id=value
        
    def __init__(self,School,department,department_hair,name,ID,grade,credit,GPA,school_address,address) :
        self.School=School
        self.departmena=department
        self.departmena_hair=department_hair
        self.name=name
        self.ID=ID
        self.grade=grade
        self.credit=credit
        self.GPA=GPA
        self.school_address=school_address
        self.address=address

    def getSchool(self):
        return self.School
    def setSchool(self,value):
        self.School=value
    def getdepartment(self):
        return self.departmena
    def setdepartment(self,value):
        self.departmena=value
    def getdepartment_hair(self):
        return self.departmena_hair
    def setdepartment_hair(self,value):
        self.departmena_hair=value
    def getname(self):
        return self.name
    def setname(self,value):
        self.name=value
    def getID(self):
        return self.ID
    def setID(self,value):
        self.ID=value
    def getgrade(self):
        return self.grade
    def setgrade(self):
        self.grade(self)
    def getcredit(self):
        return self.credit
    def setcredit(self,value):
        self.credit=value
    def getGPA(self):
        return self.GPA
    def setGPA(self,value):
        self.GPA=value
    def getschool_address(self):
        return self.school_address
    def setschool_address(self,value):
        self.school_address=value
    def getaddress(self):
        return self.address
    def setaddress(self,value):
        self.address=value
p=student("南台科技大學","資訊工程系","我","蔡佳元","4b0g0046","3","128","10%","南台街一號","雲林縣")
print(p.getSchool())
p.setSchool("成功大學")
print(p.getSchool())
