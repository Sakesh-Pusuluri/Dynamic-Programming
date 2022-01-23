class Solution:
    def partition(self, s):
        result=[]
        def backtrack(string,curr_list=[]):
            if not string:
                result.append(curr_list)
                return
            for i in range(1,len(string)+1):
                _str = string[:i]
                if(_str==_str[::-1]):
                    backtrack(string[i:],curr_list+[string[:i]])
        backtrack(s)
        return result
        
       
