#Learning Linked List 
#Source - https://www.youtube.com/watch?v=JlMyYuY1aXU&t=666s
class node:
  def __init__(self,data=None):
    self.data=data
    self.next=None

class linked_list:
  def __init__(self):
    self.head=node() #This is the placeholder to the first element in the linked list

  def append(self,data):#Apped an element to the linked list(to the last element in the linked_list)
    new_node=node(data)
    cur = self.head
    while cur.next!=None:
      cur=cur.next
    cur.next=new_node

  def length(self):
    cur=self.head
    total=0
    while cur.next!=None:
      total+=1
      cur=cur.next
    return total
  
  def display(self):
    elems=[]
    cur_node = self.head
    while cur_node.next!=None:
      cur_node=cur_node.next
      elems.append(cur_node.data)
      
    print(elems)

  def get(self,index):
    if index>self.length() or index<0:
      print('ERROR: "GET" Index out of range')
      return None

    cur_idx=0
    cur_node=self.head
    while True:
      cur_node=cur_node.next
      if cur_idx==index: return cur_node.data
      cur_idx+=1

  def erase(self,index):
      if index>self.length() or index<0:
        print('ERROR: "GET" Index out of range')
        return None
      
      cur_idx=0
      cur_node=self.head
      while True:
        last_node=cur_node
        cur_node=cur_node.next
        if cur_idx==index:
          last_node.next=cur_node.next
          return
        cur_idx+=1
      



    

my_list=linked_list()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.display()
print('The element at the 2nd index is: {}'.format(my_list.get(2)))
my_list.erase(2)
my_list.display()
