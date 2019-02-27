#Diego Quinones
#2/23/2019


#Node Functions
import random
import time
class Node(object):
    # Constructor
    def __init__(self, item, next=None):  
        self.item = item
        self.next = next 
    
def PrintNodes(N):
    if N != None:
        print(N.item, end=' ')
        PrintNodes(N.next)
        
def PrintNodesReverse(N):
    if N != None:
        PrintNodesReverse(N.next)
        print(N.item, end=' ')
        
#List Functions
class List(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None
        
def IsEmpty(L):  
    return L.head == None   

def replace(L):
    temp=L.head
    Listing=[]
    while temp is not None:
        value=temp.item
        Listing.append(value)
        temp=temp.next
    return Listing        
        
def AppendRandom(L): 
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(listFiller())
        L.tail = L.head
    else:
        L.tail.next = Node(listFiller())
        L.tail = L.tail.next

def Append(l1,x): 
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next

def GetLength(L):
    counter=0
    temp = L.head
    while temp is not None:
        counter=counter+1
        temp=temp.next
    return counter     
        
def Print(L):
    # Prints list L's items in order using a loop
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line 
        
def listFiller():
    y=random.randint(1,101)   
    return y

def mergeLists(l1, l2):
    temp = None
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.item <= l2.item:
        temp = l1
        temp.next = mergeLists(l1.next, l2)
    else:
        temp = l2
        temp.next = mergeLists(l1, l2.next)
    return temp
#combines al of the lists
def mergeSort(head):
    if head is None or head.next is None:
        return head
    l1, l2 = divideLists(head)
    l1 = mergeSort(l1)
    l2 = mergeSort(l2)
    #makes a head based on the combination of the two lists
    head = mergeLists(l1, l2)
    return head
#divides lists between halfs
def divideLists(head):
    b = head                     
    a = head                     
    if b:
        b = b.next            
    while b:
        b = b.next            
        if b:
            b = b.next
            a = a.next
    mid = a.next
    a.next = None
    return mid,head

def quickSortPros(List1):
    more=[]
    same=[]
    less=[]
    if len(List1)>1:
        pivot=List1[0]
        for i in List1:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                same.append(i) 
            elif i > pivot:
                more.append(i)
        return quickSortPros(less)+same+quickSortPros(more)
    else:
        return List1
        
def quickSort(L):
    ListFormat=replace(L)
    Length=GetLength(L)
    ListFormat2=quickSortPros(ListFormat)
    L.head=L.tail
    L.head=None
    for i in range(Length):
        Append(L,ListFormat2[i])
    
    
def bubble(L):
    Length=GetLength(L)
    ListFormat=replace(L)
    for i in range(0,Length-1):
        for j in range(0,Length-1):
            if ListFormat[i]>ListFormat[i+1]:
                stor=ListFormat[i]
                ListFormat[i]=ListFormat[i+1]
                ListFormat[i+1]=stor
    L.head=L.tail
    L.head=None 
    for i in range(Length):
        Append(L,ListFormat[i])
                
def Median(L):
    temp=L.head
    Length=round(GetLength(L)/2)
    for i in range(Length+1):
        value=temp.item
        temp=temp.next
    return value            
            

print('List')         

#create list
L = List()
for i in range(5):
    AppendRandom(L)
    
    
Print(L)
#sorting method
print('Quicksort')
#running time
start = time.time()
quickSort(L)
end = time.time()
#print running time
print(end - start)
Print(L)
print(Median(L))

#reset list
L.head=L.tail
L.head=None

for i in range(5):
    AppendRandom(L)
print('List')       
Print(L)
#sorting method
print('MergeSort')
start = time.time()
mergeSort(L.head)
end = time.time()
print(end - start)
#print running time
Print(L)
print(Median(L))
#reset list
L.head=L.tail
L.head=None

for i in range(5):
    AppendRandom(L)
print('List')       
Print(L)
#sorting method
print('BubbleSort')
start = time.time()
bubble(L)
end = time.time()
print(end - start)
#print running time
Print(L)
print(Median(L))









