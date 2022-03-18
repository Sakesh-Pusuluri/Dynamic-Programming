class Solution:
    def intToRoman(self, num: int) -> str:
        roman=[(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),
              (40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
        finalResult=[]
        for val,symbol in roman:
            if(num==0):
                break
            qu0,num = divmod(num,val)
            finalResult.append(qu0*symbol)
        return ''.join(finalResult)
