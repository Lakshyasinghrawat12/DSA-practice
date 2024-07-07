nums= [2,7,11,15]

seen={} #keep track of numbers (as key) and indexes (as value)


target= int(input('enter the target vlaue: ')) #take the target value as input


for i, vlaue in enumerate(nums):
    '''you go over your array using enumerate that 
    gives you both index and value of elements in array'''

    remaning= target - nums[i]  #store the remaning value 

    if remaning in seen:  

        '''checks weather the remaining value is already in the directory or not if yes then it returns 
        the indexes of the value and if not it adds it to the directory so that it can be seen in the future 
        assuming there is a possible solution to the problem''' 

        print( [i, seen[remaning]])
    else:
        seen[vlaue]= i

#https://leetcode.com/problems/two-sum/description/
