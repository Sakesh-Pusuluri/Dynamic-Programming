class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        leftPointer,rightPointer = 0,len(people)-1
        boat = 0
        while(leftPointer<=rightPointer):
            value = people[leftPointer] + people[rightPointer]
            if(value>limit):
                boat +=1
                rightPointer -=1
            else:
                boat +=1
                leftPointer +=1
                rightPointer -=1
        return boat
                
                
        
