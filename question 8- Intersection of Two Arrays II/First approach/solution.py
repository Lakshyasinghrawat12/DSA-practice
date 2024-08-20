from typing import List, Optional

def solution(nums1: List[int], nums2: List[int]):
    
    result= []

    for num in nums1:
        if num in nums2:
            result.append(num)
            nums2.remove(num)

    return result

# nums1 = [1,2,2,1]
# nums2 = [2,2]

nums1 = [4,9,5] 
nums2 = [9,4,9,8,4]


print(solution(nums1, nums2))