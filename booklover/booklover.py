import pandas as pd
class BookLover():
    
    num_books = 0
    book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
    
    def __init__(self,name,email,fav_genre):
        if type(name) != str:
            print("Please enter a string")
        else:
            self.name = name
        if type(email) != str:
            print("Please enter a string")
        else:
            self.email = email
        if type(fav_genre) != str:
            print("Please enter a string")
        else:
            self.fav_genre = fav_genre
            
    def add_book(self,book_name, rating):
        
        if book_name in list(self.book_list["book_name"]):
            print('Book already exsits in book list')
        elif type(rating) != int or rating >5 or rating <1:
            print('Please enter a rating between 1 (bad) and 5 (great)')
        else:
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [rating]})
    
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        
    def has_read(self,book_name):
        
        if book_name in list(self.book_list["book_name"]):
            return True
        else:
            return False
            
    def num_books_read(self):
        return len(self.book_list)
    
    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]
        