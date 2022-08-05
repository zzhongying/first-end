from typing import List

#---------------------方法一：暴力循环---------------------------------------------------
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums)== 0:
            return []
        else:
            test=[]
            for i in range(0,len(nums)-k+1):
                temp = []
                for j in range(i,i+k):
                    temp.append(nums[j])
                test.append(max(temp))
            return test
    maxSlidingWindow(maxSlidingWindow,[1,3,-1,-3,5,3,6,7],3)


#---------------------方法二：辅助队列求解---------------------------------------------------

class Solution1:
    def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
        if len(nums)== 0:
            return []
        else:
            for i in range(0,len(nums)-k+1):
                temp=[]



    maxSlidingWindow1(maxSlidingWindow1, [1, 3, -1, -3, 5, 3, 6, 7], 3)
