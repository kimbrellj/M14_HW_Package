import unittest
import numpy as np
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        print(test_object.book_list)
        self.assertIn("War of the Worlds",list(test_object.book_list["book_name"]))
        
        

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("War of the Worlds", 4)
        
        self.assertEqual(1,len(test_object.book_list))
        
        
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("Harry Potter",3)
        
        self.assertTrue(test_object.has_read("War of the Worlds"))
        

    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("Harry Potter",3)
        
        self.assertFalse(test_object.has_read("Hunger Games"))

    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("Harry Potter",3)
        test_object.add_book("Hunger Games",5)
        
        self.assertEqual(3, test_object.num_books_read())

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        test_object.add_book("War of the Worlds", 4)
        test_object.add_book("Harry Potter",3)
        test_object.add_book("Hunger Games",5)
        test_object.add_book("Lord of the Rings",1)
        test_object.add_book("Marry Poppins",2)
        
        df = test_object.fav_books()
        
        self.assertTrue(np.all(df['book_rating'] > 3))

if __name__ == '__main__':

    unittest.main(verbosity=3)