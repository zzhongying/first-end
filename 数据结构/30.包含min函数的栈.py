
#------------方法一：不限定时间复杂度-----------------------------------------
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A=[]

    def push(self, x: int) -> None:
        self.A.append(x)

    def pop(self) -> None:
        self.A.pop()

    def top(self) -> int:
        while self.A:
            return self.A[len(self.A)-1]  #输出栈顶元素，即list中最后一个元素

    def min(self) -> int:
        print(self.A)
        while self.A:
            return min(self.A)           #返回栈中最小元素，时间复杂度为O(n)


#---------------方法二：限定时间复杂度为O(1)---------------------------------------

class MinStack2:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A=[]
        self.B=[]

    def push(self, x: int) -> None:
        self.A.append(x)
        if len(self.B)==0:  #若为空，则首次添加x元素
            self.B.append(x)
        elif x <= self.B[-1]:  #若不为空，则比较栈顶元素与当前元素
            self.B.append(x)


    def pop(self) -> None:
        if self.A.pop() == self.B[-1]:  #比较的同时进行移除动作
            self.B.pop()


    def top(self) -> int:
        while self.A:
            return self.A[-1]  #输出栈顶元素，即list中最后一个元素

    def min(self) -> int:
            return self.B[-1]          #返回栈中最小元素，时间复杂度为O(1)

