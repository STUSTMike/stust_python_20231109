class library():

    def __init__(self,name,id,year,author,location) :
        self.name=name
        self.id=id
        self.year=year
        self.author=author
        self.lend=False
        self.time=None
        self.location=location

    def borrow(self,book,time):
        book.lend=True
        book.time=time
        print("已借出的書\n書名:{},編號:{},年分:{},作者:{},位址:{},借出時間:{}".format(book.name,book.id,book.year,book.author,book.location,book.time))


    def return_book(self, book):
        if book.lend==True:
            book.lend=False
            book.time=None
    
    def Overview(self,id):
        if id== self.id:
            print(self.name)
            if self.lend:
                print("這本書已被借,出借時間為{}".format(self.time))
        else:
            
            print("這本書還沒借出")

class Student(library):
    
    def __init__(self,name,id) :
        self.student_name=name
        self.student_id=id
        self.books=[]

    def borrow(self, book, time):
        super().borrow(book, time)
        self.books.append(book)
    
    def return_book(self, book):
        if book in self.books:
            super().return_book(book)
            self.books.remove(book)
        else:
            print("你沒有借這本書")

    def lnquire(self, student_id):
        if self.student_id == student_id:
            print("你借的書")
            for book in self.books:
                print("書名:{}, 編號:{}, 年分:{}, 作者:{}, 位址:{}".format(book.name, book.id, book.year, book.author, book.location))


text=library("博奕遊戲",1,1998,"mike","c301")
text1=library("桌遊",2,1998,"mike","c301")
text2=library("遊戲",3,1998,"mike","c301")

user=Student("mike","1A")
user.borrow(text,"10:20")
user.borrow(text1,"10:25")
text.Overview(1)
user.lnquire("1A")
user.return_book(text1)
user.lnquire("1A")

