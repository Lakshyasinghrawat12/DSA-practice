from typing import List, Optional

def solution(nums: List[int]):
    n= len(nums)
    correct_sum= n*(n+1)//2
    actual_sum= sum(nums)


    return correct_sum - actual_sum

nums= [3,0,1]
print(solution(nums))