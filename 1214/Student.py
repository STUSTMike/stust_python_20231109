class Student:
    def __init__(self,name,ID,major):
        self.name=name
        self.ID=ID
        self.major=major
        self.book=[]
    
    def borrow_book(self,book):
        if len(self.book)<5:
            self.book.append(book)
            print("已借書[{}]".format(book))
        else:
            print("上限為五本，無法再借書[{}]".format(book))

    def return_book(self, book):
        if book in self.book:
            self.book.remove(book)
            print("已還書[{}]".format(book))
        else:
            print("你沒有借這本書{}".format(book))

    def lnquire(self,ID):
        if(self.ID==ID):
            print("你借得書{}".format(self.book))

    # def select(self,course):
    #     self.course=course
    #     print("已加選[{}]。".format(self.course))
    
   
    # def retreat(self,course):
    #     if(self.course==course):
    #         self.course=None
    #         print("已幫你退選")
    #     else:
    #         print("沒有查詢到[{}]這門課".format(course))
    
    # def lnquire_major(self,ID):
    #     if(self.ID==ID):
    #         print("你借得書[{}]".format(self.book))
        


op=Student("小明",124,"財金")

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
#如何投資,理財,郭台銘,選舉,電競,韓國瑜
