class Solution:
    def simplifyPath(self, path: str) -> str:
        result=[]
        for portion in path.split('/'):
            if(portion=='..'):
                if result:
                    result.pop()
            elif(portion=='.' or not portion):
                continue
            else:
                result.append(portion)
        return '/'+'/'.join(result)
                
        
