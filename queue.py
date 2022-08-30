from collections import deque

class solution:
    def func(self,arr):
        _temp = deque()

        for i in arr:
            _temp.append(i)
            print("queue after append ",_temp)

        while(_temp):
            _temp.popleft()
            print("Queue after popping ",_temp)
        
        return 

if __name__=="__main__":
    
    arr = [4,6,2,7,8]
    x = solution()
    x.func(arr)
