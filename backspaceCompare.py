class Solution:
    def backspaceCompare(self, s, t):
        l1,l2=[],[]
        def listString(l,string):
            for i in string:
                if(i=='#' and l):
                    l.pop()
                elif(i!='#'):
                    l.append(i)
            return l
        l1=listString(l1,s)
        l2=listString(l2,t)
        print(l1, l2)
        if(l1==l2):
            return True
        return False

      
      
# Time complexity - O(N)
# Space complexity - O(N)
