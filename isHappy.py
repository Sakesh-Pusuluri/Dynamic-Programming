class Solution:
    def isHappy(self, n: int) -> bool:
        def findSquare(temp):
            _sum=0
            while(temp):
                rem=temp%10
                _sum+=(rem**2)
                temp=temp//10
            return _sum
        slow,fast=n,n
        while True:
            slow=findSquare(slow)
            fast=findSquare(findSquare(fast))
            if(slow==fast):
                break
        return slow==1
      
# Time complexity - O(logN)
# Space complexity - O(1)
