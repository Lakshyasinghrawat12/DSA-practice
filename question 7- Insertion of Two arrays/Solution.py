from typing import List, Optional

def solution(nums1: List[int], nums2: List[int]):
    
    set1= set(nums1)
    result=[]

    for num in nums2:

        if num in set1:
            result.append(num)
            set1.remove(num)
    return result



num1= [4,9,5]
num2= [9,4,9,8,4]

print(solution(num1, num2))