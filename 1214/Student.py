class Student:
    def __init__(self,name,ID,major):
        self.name=name
        self.ID=ID
        self.major=major
    
    def borrow_book(self,book):
        self.book=book
        print("已借[{}]。".format(book))
    
    def return_book(self,book):
        if(self.book==book):
            self.book=None
            print("已還書")
        else:
            print("沒有查詢到[{}]這本書。".format(book))


    def lnquire(self,ID):
        if(self.ID==ID):
            print("你借得書[{}]".format(self.book))
        

    def select(self,course):
        self.course=course
        print("已加選[{}]。".format(self.course))
    
    def retreat(self,course):
        if(self.course==course):
            self.course=None
            print("已幫你退選")
        else:
            print("沒有查詢到[{}]這門課".format(course))
    
    def lnquire_major(self,ID):
        if(self.ID==ID):
            print("你借得書[{}]".format(self.book))
        


op=Student("小明",124,"財金")
op.borrow_book("如何投資")
op.return_book("教你投資")
op.lnquire(124)
op.return_book("如何投資")