class Student:
    def __init__ (self,id,major,credits,gpa,address):
        self._id=id
        self._major=major
        self._credits=credits
        self._gpa=gpa
        self.address=address

    @property
    def student_id(self):
        print(f'"{self._id}" was accessed.')
        return self._id
    
    @student_id.setter
    def student_id(self,value):
        print(f'"{self._id}"is now"{value}".')
        self._id=value

    @student_id.deleter
    def student_id(self):
        print(f'"{self._id}" was deleter.')
        del self._id

    @property
    def student_major(self):
        print(f'"{self._major}" was accessed.')
        return self._major
    
    @student_major.setter
    def student_major(self,value):
        print(f'"{self._major}"is now"{value}".')
        self._major=value

    @student_major.deleter
    def student_major(self):
        print(f'"{self._major}" was deleter.')
        del self._major

    @property
    def student_credits(self):
        print(f'"{self._credits}" was accessed.')
        return self._credits
    
    @student_credits.setter
    def student_credits(self,value):
        print(f'"{self._credits}"is now"{value}".')
        self._credits=value

    @student_credits.deleter
    def student_credits(self):
        print(f'"{self._credits}" was deleter.')
        del self._credits

    @property
    def student_gpa(self):
        print(f'"{self._gpa}" was accessed.')
        return self._gpa
    
    @student_gpa.setter
    def student_gpa(self,value):
        print(f'"{self._gpa}"is now"{value}".')
        self._gpa=value

    @student_gpa.deleter
    def student_gpa(self):
        print(f'"{self._gpa}" was deleter.')
        del self._gpa

    @property
    def student_address(self):
        print(f'"{self._address}" was accessed.')
        return self._address
    
    @student_address.setter
    def student_address(self,value):
        print(f'"{self._address}"is now"{value}".')
        self._address=value

    @student_address.deleter
    def student_address(self):
        print(f'"{self._address}" was deleter.')
        del self._address

if __name__=="__main__":
    p=Student("4b0g0046","資訊工程系","蔡佳元","10%","雲林縣")
    print(p.student_id)
    p.student_id="4B0G0046"
    del p.student_id