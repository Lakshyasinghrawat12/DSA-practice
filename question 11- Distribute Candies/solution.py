from typing import List

def distribute(candyType: List[int]):

    l= len(candyType)
    eat= l//2
    dis_candyType= set(candyType)

    if eat<= len(dis_candyType):
        return eat
    
    elif eat> len(dis_candyType):
        return len(dis_candyType)
    

candy= [1,1,2,4,4,3,3,3]
print(distribute(candy))