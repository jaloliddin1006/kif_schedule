from typing import List , Optional
import time

# a = [2,3,5,8,9,4,8,5,7,9,4,7,5,9,8,7,8,7,8,2,2,3,5,8,9,4,8,5,7,9,4,7,5,9,8,7,8,7,8,2,2,3,5,8,9,4,8,5,7,9,4,7,5,9,8,7,8,7,8,2]*5

# start = time.time()
# # sum with recursion
# def summ(nums, index = 0): 
     
#     if len(nums) == index:
#         return 0
#     return nums[index] + summ(nums, index+1)
# print(summ(a))
# end = time.time()
# print(end-start)





#### algoritmlash
# # 3 ta sonni kattasini topish
# a = 3
# b = 5
# c = 6
# if a>b:
#     if a>c:
#         print(a)
#     else:
#         print(c)
# else:
#     if b>c:
#         print(b)
#     else:
#         print(c)
        
        
        
###### SEARCH
# ## Linear Search

# a = int(input("a [1,1000] = "))

# for i in range(1,1000):
#     if i==a:
#         print(f" {i} ta urinishda topildi")
#         break  
 
 
        
# ### Binary Search

# a = int(input("a [1,1000] = "))
# start = time.time()

# l = 1
# g = 1000
# T = (l+g)//2
# S = 1
# while a != T:
#     S += 1
#     if a > T:
#         l = T
#     else:
#         g = T
#     T =(l+g)//2
    
# print(f"{S} ta urinishda topdi")
# end = time.time()
# print(end-start)



"""
### LINKED LIST

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList():
    def __init__(self):
        self.head = None
        
        
    # barcha tugunlarni ko'rish
    def node_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    ## ro'yxat boshidan element qo'shish
    def push_node(self, new_data):
        
        # yangi Node element yaratamiz va next iga head ni bog'laymiz
        new_node = Node(new_data)
        new_node.next = self.head
        
        self.head = new_node
        
    ## ro'yxat orasiga element qo'shish
    def insert_node(self, prev_node, new_data):
        new_node = Node(new_data)
        new_node.next = prev_node.next
        
        prev_node.next = new_node
        
        
    ## ro'yxat oxiridan element qo'shish
    def append_node(self, new_data):
        new_node = Node(new_data)
        if not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        
        
    ## ro'yxatdan elementni o'chirib tashlash
    def delete_node(self, data):
        temp = self.head
        if temp and temp.data == data:
            self.head = temp.next
            temp = None
            return
        
        while temp:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
        
        if temp is None:
            print("Ma'lumot topilmadi\n----------")
            return
        
        prev.next = temp.next
        temp = None
        
        
        
# linked list object yaratamiz
obj = LinkedList()

# tugunlarni yaratamiz
first_node = Node("Dushanba")
second_node = Node("Seshanba")
thrid_node = Node("Chorshanba")

# linked list ning birinchi elementini ko'rsatib qo'yamiz
obj.head = first_node

# keyingi elementlarni bog'lab chiqaminz
first_node.next = second_node   # yoki obj.head.next = second_node  # chunki obj da faqat 1 chi elementni ma'lumoti bor
second_node.next = thrid_node


# # tugunlarni chiqarish
# print(obj.head.data)
# print(obj.head.next.data)
# print(obj.head.next.next.data)


# funksiya orqali korish
obj.node_list()

print("-------")


## ro'yxat boshidan element qo'shish
obj.push_node("Yakshanba")
obj.node_list()
print("-------")



## ro'yxat orasiga element qo'shish
# obj.insert_node(obj.head, "Yakshanba kechasi")
# obj.insert_node(obj.head.next, "Dushanba kechasi")
obj.insert_node(second_node, "Seshanba kechasi")
obj.node_list()
print("-------")





## ro'yxat oxiridan element qo'shish
obj.append_node("Pashanba")
obj.append_node("Juma")
obj.node_list()
print("-------")



## ro'yxatdan elementni o'chirib tashlash
obj.delete_node("chorshanba")
obj.node_list()
print("-------")
"""





class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def print_all_nodes(self, head: Optional[ListNode]):
        curr = head[0]
        
        while curr:
            print(curr.val)
            curr = curr.next
    
    
    def print_middle_num(self, head: Optional[ListNode]):
        faster = head
        slow = head
        while faster and faster.next:
            faster = faster.next.next
            slow = slow.next
        print(slow.val)
        
    def reversed_node(self, head: Optional[ListNode]):
        curr = head
        prev = None
        
        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        print(prev.val)
        
        # while prev:
        #     print(prev.val)
        #     prev = prev.next
            
            
        
    
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head[0]
        while temp:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            temp = temp.next
        
        temp = head[0]
        while temp:
            print(temp.val)
            temp = temp.next
            
# c = ListNode(3)
# b = ListNode(2, c)
# a = ListNode(1, b)
# # head = [a,b,c]
# head = a

# s = Solution()
# # s.print_all_nodes(head) ## print all node
# # s.print_middle_num(head) ## middle node
# s.reversed_node(head) ## middle node




class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        if len(nums) == nums[-1]+1:
            return len(nums)

        L = 0
        G = nums[-1]
        T = (L+G)//2
        while T in nums:
            print(T, L,G)
            if nums[T] == T:
                L = T + 1
            else:
                G = T
            T = (L+G)//2
        return T


d = [0,2,3,4,5,6,8,9,7]
d=[45,35,38,13,12,23,48,15,44,21,43,26,6,37,1,19,22,3,11,32,4,16,28,49,29,36,33,8,9,39,46,17,41,7,2,5,27,20,40,34,30,25,47,0,31,42,24,10,14]
# d = [0,2]
# # d=[0,1,2,3,4,5]
# a = Solution()
# res = a.missingNumber(d)
# print(res)






##### selection search
##### selection search

def selection_search(nums):
    sorted_nums = []
    while nums:
        max_num = nums[0]
        for num in nums:
            if max_num < num:
                max_num = num
        elem = nums.index(max_num)
        sorted_nums.append(nums.pop(elem))
    return sorted_nums

# mynums = [234,34,12,234,567,987,43,2434,678,543,1223,555]
# print(selection_search(mynums))




#### The Stack

class Stack():
    def __init__(self):
        self.stack = []
        
    def isEmpty(self):
        print( not self.stack)
        # return not self.stack
    
    def Peek(self):
        if self.stack:
            return self.stack[-1]
        return 'Stack is Empty'
    
    def Push(self, new):
        self.stack.append(new)
    
    def Pop(self):
        if self.stack:
            return self.stack.pop()
        return 'Stack is Empty'
             
obj = Stack()
# obj.isEmpty()
obj.Push(12)
obj.Push(13)

p_el = obj.Pop()
print(p_el)

last = obj.Peek()
print(last)
