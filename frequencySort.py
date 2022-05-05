class Solution:
    def frequencySort(self, s: str) -> str:
        resultString,countDict='',Counter(s)
        sortedKeys = sorted(countDict,key=countDict.get,reverse=True)
        for key in sortedKeys:
            resultString+=key*countDict[key]
        return resultString
