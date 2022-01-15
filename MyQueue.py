class MyQueue:

    def __init__(self):
        self.l=[]
        self.count=0

    def push(self, x: int):
        self.l.append(x)
        self.count+=1

    def pop(self) -> int:
        if(self.count):
            ele=self.l[0]
            self.l=self.l[1:]
            self.count-=1
            return ele

    def peek(self) -> int:
        return self.l[0]
        

    def empty(self) -> bool:
        return self.count==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
