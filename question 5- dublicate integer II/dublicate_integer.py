from typing import Optional, List





nums=[1,0,1,1]
k= 4
def solution(nums: List[int], k: int):

    last_position= {}

    for i, num in enumerate(nums):
        if num in last_position and i - last_position[num]<= k:
            return True
        last_position[num]= i
    return False

print(solution(nums, k))