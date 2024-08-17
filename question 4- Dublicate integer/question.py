from typing import List

nums= [1,2,3,3]

def find_dublicate(nums: List[int])->bool:

    '''This is also correct but it takes too much time'''
    # store= []

    # for i in nums:
    #     if i in store:
    #         return True
    #     store.append(i)

    # return False

    hash= set()

    for i in nums:
        if i in hash:
            return True
        hash.add(i)

    return False



print(find_dublicate(nums))