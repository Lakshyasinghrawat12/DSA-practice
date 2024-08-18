# Correct Approach

There are multiple ways to solve this problem efficiently. Below is one approach using a mathematical formula.

# Mathematical Approach (Sum Formula)

The idea is to calculate the sum of the first n natural numbers (using the formula sum= n*(n+1)/2) and then subtract the sum of all the elements in the array from this sum. The difference will be the missing number.

##### But even this method has its flaws as it can perform when there ar multiple values missing for example an array with [1,2,5,6,8] values in that case we can use this code

### code Snippet
```python
class Solution:
    def findMissingNumbers(self, nums: List[int]) -> List[int]:
        min_num = min(nums)
        max_num = max(nums)
        
        full_set = set(range(min_num, max_num + 1))
        nums_set = set(nums)
        
        missing_numbers = sorted(list(full_set - nums_set))
        
        return missing_numbers
```