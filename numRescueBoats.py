class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        leftPointer,rightPointer = 0,len(people)-1
        count=0
        while(leftPointer<=rightPointer):
            value = people[leftPointer] + people[rightPointer]
            if(value>limit):
                count+=1
                rightPointer -=1
            else:
                count+=1
                leftPointer +=1
                rightPointer -=1
        return count
