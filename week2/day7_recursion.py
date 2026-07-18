def sum_list(nums:list)-> int:
    if len(nums)==0:
        return 0
    return nums[0]+sum_list(nums[1:])
nums=[1,2,3,4,5]
print(sum_list(nums))
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
def reverse_list_recursive(head):
    
    if head is None or head.next is None:
        return head

    new_head = reverse_list_recursive(head.next)

    head.next.next = head
    head.next = None

    return new_head
def to_list(head:Node) -> list:
    list1=[]
    temp=head
    while temp:
        list1.append(temp.val)
        temp=temp.next
    return list1
def count_nodes(head:Node):
    if head is None:
        return 0
    
    else:
        return 1+count_nodes(head.next)


if __name__=="__main__":
    nums=[1,2,3,4,5]
    print(sum_list(nums))
    print(count_nodes(None))



    a = Node(1); b = Node(2); c = Node(3)
    a.next = b; b.next = c

    print(to_list(a))                  
    new_head = reverse_list_recursive(a)
    
    print(to_list(new_head))  
    print(to_list(a))  
    print(to_list(reverse_list_recursive(None)))        
    solo = Node(7)
    print(to_list(reverse_list_recursive(solo)))            


