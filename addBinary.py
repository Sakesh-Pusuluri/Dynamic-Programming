class Solution(object):
    def addBinary(self, a, b):
        _carry,_sum=0,0
        result=''
        if(len(b)<=len(a)):
            b='0'*(len(a)-len(b))+b
        else:
            a='0'*(len(b)-len(a))+a     
        for i in range(len(b)-1,-1,-1):
            _sum=_carry+int(a[i])+int(b[i])
            print(_sum)
            if(_sum==2):
                _carry=1
                result='0'+result
            elif(_sum==1):
                _carry=0
                result='1'+result
            elif(_sum==3):
                _carry=1
                result='1'+result
            else:
                _carry=0
                result='0'+result
        if(_carry==1):
            return '1'+result
        return result
                
        
# Time complexity - O(max(m,n))
# Space complexity - O(max(m,n))
        
        
        
