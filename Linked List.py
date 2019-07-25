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






my_list=linked_list()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.display()
