class FreqStack:

    def __init__(self):
        self.frequency = collections.Counter()
        self.group = collections.defaultdict(list)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.frequency[val] = self.frequency.get(val,0)+1
        if(self.maxFreq<self.frequency[val]):
            self.maxFreq = self.frequency[val]
        self.group[self.frequency[val]].append(val)
            

    def pop(self) -> int:
        popped = self.group[self.maxFreq].pop()
        self.frequency[popped] -= 1
        if not self.group[self.maxFreq]:
            self.maxFreq -= 1
        return popped
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
