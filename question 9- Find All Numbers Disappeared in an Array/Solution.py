def findDisappearedNumbers(nums):
        
    i= len(nums)
    max_num= i+1
    min_num= 1
    
    set1= set(range(min_num, max_num))
    set2= set(nums)
    missig_num= set1- set2


    return list(missig_num)      


nums = [4,3,2,7,8,2,3,1]

print(findDisappearedNumbers(nums))