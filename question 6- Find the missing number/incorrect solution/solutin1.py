from typing import List, Optional

def solution(nums: List[int]):
    nums.sort()
    for i in nums:
        num= i+1
        if num not in nums:
            return num
        

nums= [3,0,1]

print(solution(nums))