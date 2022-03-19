class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterLogs,digitLogs = [],[]
        for log in logs:
            splitLog = log.split()
            if(splitLog[1].isdigit()):
                digitLogs.append(log)
            else:
                letterLogs.append(log)
        letterLogs.sort(key=lambda x:((' '.join(x.split()[1:])),x.split()[0]))
        return letterLogs + digitLogs
    
        
