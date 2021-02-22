"""#Q:Given a linked list of characters.Write a python function to  return a new string that
    is created by appending all the characters given in the linked list as per the
    rules given below
    Rules-
    1: Replace * or / by a single space
    2: In case of two consecutive occurrence of * or / replace those two occurrence by
      a single space and convert the next charater to upper case
    Assume that-
      -There will no be more than two consecutive occurence of * or /
      -The linked list will always end with an alphabet

    eg-
    input-A,n,*,/,a,p,p,l,e,*,a,/,d,a,y,*,*,k,e,e,p,s,/,*,a,/,/,d,o,c,t,o,r,*,A,w,a,y
    output-An Apple a day Keeps A Doctor Away
"""



##########create node class:#########################################################
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

##############create linklist class:##################################################
class LL:
    def __inti__(self):
        self.head=None

    ############# Traverse(Print linklist):###########################################
    def traverese(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next


    ############################### Insert from Head:##############################
    def add_head(self,value):
        new_node=Node(value)    #create a new node calling Node Class
        new_node.next=self.head
        self.head=new_node




     ################
    def change_sentence(self):
        temp=self.head
        while temp is not None:
            if temp.data=='*' or temp.data=='/':
                temp.data=''
                if temp.next.data=='*' or temp.next.data=='/':
                    temp.next.next.data=temp.next.data.upper()
                    temp.next=temp.next.next
            temp=temp.next

word_list=LL()
sample=input("Enter sample input")
print("You enter:",sample)
for i in sample:
    word_list.add_head(i)
word_list.change_sentence()
word_list.traverese()

