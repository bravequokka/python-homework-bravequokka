class Book:
    def set_info(self, name, writer):
        self.name = name
        self.writer = writer
        
    def print_info(self):
        print('책 제목 : {}' .format(self.name))
        print('책 저자 : {}' .format(self.writer))

book1 = Book()
book1.set_info('파이썬', '민경태')
book1.print_info()

book2 = Book()
book2.set_info('어린왕자' , '생택쥐페리')
book2.print_info()

book_list = []
book_list.append(book1)
book_list.append(book2)