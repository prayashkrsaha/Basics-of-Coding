#Difference of abstract class and inheritance is that abstract class cannot be diretly invoked by the the main function. 
#It always need to havea child class and main function needs to call the child function
#In inheritance both the classses(1&2) can create an instance.
#Source : https://www.hackerrank.com/challenges/30-abstract-classes/problem

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
    def __init__(self,title,author,price):
        Book.__init__(self,title,author)
        self.price=price
    
    def display(self):
        print('Title: ' + self.title)
        print('Author: ' + self.author)
        print('Price: '+ str(self.price))

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()
