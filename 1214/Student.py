class Student:
    def __init__(self,name,ID,major):
        self.name=name
        self.ID=ID
        self.major=major
        self.book=[]
    
    def borrow_book(self,book):
        self.book.append(book)

    def return_book(self,book):
        for i in self.book:
            if(i==book):
                self.book.remove(i)
                print("已還書[{}]".format(i))
            


    def lnquire(self,ID):
        if(self.ID==ID):
            print("你借得書{}".format(self.book))

    def lnquire_book(self,ID,book):
        if(self.ID==ID):
            for i in self.book:
                if(i==book):
                    print("你有借這書{}".format(i))      

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
<<<<<<< Updated upstream
text=input("你要借的書:")
text_splut=text.split(",")
for i in text_splut:
    op.borrow_book(i)
    
# op.borrow_book("如何投資")
# op.borrow_book("教你投資")
# op.borrow_book("理財")
# op.borrow_book("郭台銘")
# op.borrow_book("台積電")
op.return_book("教你投資")
op.lnquire(124)
op.return_book("如何投資")
op.lnquire(124)
=======
op.borrow_book("如何投資")
op.borrow_book("教你投資")
op.borrow_book("理財")
op.borrow_book("郭台銘")
op.borrow_book("台積電")
# op.return_book("教你投資")
op.lnquire_book(124,"台積電")
# op.return_book("如何投資")
>>>>>>> Stashed changes
