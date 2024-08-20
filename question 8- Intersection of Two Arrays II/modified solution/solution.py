from typing import List, Optional

def solution(nums1: List[int], nums2: List[int]):
    result= []
    count_dict= {}

    for num in nums2:
        if num in count_dict:
            count_dict[num]+= 1
        else:
            count_dict[num]= 1

    for num in nums1:
        if num in count_dict and count_dict[num]> 0:
            result.append(num)
            count_dict[num]-= 1 

    return result


nums1 = [4,9,5] 
nums2 = [9,4,9,8,4]


print(solution(nums1, nums2))