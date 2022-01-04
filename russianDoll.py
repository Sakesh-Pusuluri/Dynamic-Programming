class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        sub = []
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        for num in envelopes:
            i = bisect_left(sub, num[1])
            #print(i,num)
            if i == len(sub):
                sub.append(num[1])
            else:
                sub[i] = num[1]
        #print(sub)
        return len(sub)
