# The functions associated with stack are:

# empty() – Returns whether the stack is empty – Time Complexity: O(1)
# size() – Returns the size of the stack – Time Complexity: O(1)
# top() / peek() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
# push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
# pop() – Deletes the topmost element of the stack – Time Complexity: O(1)



# class solution:
#     def funct(self,arr):

#         arr.append(1)
#         print("New array is :", arr)

#         arr.pop()
#         print("new array after popping :",arr)
#         return

# if __name__=="__main__":
#     arr = [0,9,8,7]

#     x = solution()
#     x.funct(arr)


# ----------------- Generally not used 

# Better appraoch is to use deque()

from collections import deque

class solution:
    def func(self,arr):
        
        st = deque()

        for a in arr:
            st.append(a)
            print("stack after append is ",st)
        
        for i in range(len(st)):
            st.pop()
            print("stack after pop is ", st)
        

        return



if __name__=="__main__":
    arr = [0,9,8,7]

    x = solution()
    x.func(arr)

