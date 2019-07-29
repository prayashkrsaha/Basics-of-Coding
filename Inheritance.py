#Inheritance Example. here the class Student is inherited from the class Person. 
#This makes programming easier if we have lot of similar things to be inherited 
#Source- https://www.hackerrank.com/challenges/30-inheritance/problem

class Person:
  def __init__(self, firstName, lastName, idNumber):
    self.firstName=firstName
    self.lastName=lastName
    self.idNumber=idNumber
    #self.scores=scores

  def printPerson(self):
    print('Name : {} {}'.format(self.firstName,self.lastName))
    print('ID : {}'.format(idNumber))
    #print('Scores: {}'.format(self.scores))

#class student here is an inherited class of Person
class Student(Person):
  def  __init__(self, firstName, lastName, idNumber, scores):
    Person.__init__(self,firstName,lastName,idNumber)
    self.scores=scores
  
  def calculate(self):
    sum=0
    for score in scores:
      sum+=score
    avg=sum/len(scores)
    if avg<40:
        return 'X'
    elif avg<40:
        return 'T'
    elif avg<55:
        return 'D'
    elif avg<70:
        return 'P'
    elif avg<80:
        return 'A'
    elif avg<90:
        return 'E'
    else:         
        return 'O'        


n=int(input('Enter the number of students: '))
for i in range(n):
  print('Enter your firstName, lastName and ID number with spaces')
  line = input().split(' ')
  firstName =line[0]
  lastName =line[1]
  idNumber= line[2]
 # s= int(input('Enter the number of score to be entered'))
  scores = list( map(int, input().split()) )
  S=Student(firstName,lastName,idNumber,scores)
  S.printPerson()
  print("Grade:", S.calculate())
