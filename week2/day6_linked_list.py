class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
def reverse_list(head:Node) -> Node:
    prev = None
    curr=head
    while curr:
        next_node=curr.next
        curr.next=prev
        prev=curr
        curr=next_node
    return prev
def to_list(head:Node) -> list:
    list1=[]
    temp=head
    while temp:
        list1.append(temp.val)
        temp=temp.next
    return list1
if __name__=="__main__":
    a = Node(1); b = Node(2); c = Node(3)
    a.next = b; b.next = c

    print(to_list(a))                  
    new_head = reverse_list(a)
    
    print(to_list(new_head))  
    print(to_list(a))  
    print(to_list(reverse_list(None)))        
    solo = Node(7)
    print(to_list(reverse_list(solo)))            


