class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if(digits==''):
            return
        letters='abcdefghijklmnopqrstuvwxyz'
        phone_dict=defaultdict(list)
        index=0
        for idx in range(2,7):
            phone_dict[str(idx)] = list(letters[index:index+3])
            index+=3
        phone_dict['7']=['p','q','r','s']
        phone_dict['8']=['t','u','v']
        phone_dict['9'] = list(letters[-4:])
        if(len(digits)==1):
            return phone_dict[digits]
        results=phone_dict[digits[0]]
        for num in digits[1:]:
            int_list=[]
            for val in results:
                for char in phone_dict[num]:
                    int_list.append(val+char)
            results=int_list
        return results
                
                
        
            
            
        
