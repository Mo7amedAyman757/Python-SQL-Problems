class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        arr1, arr2 = [], []
        
        # ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
        for log in logs:
            if (log.split()[1]).isdigit():
                arr1.append(log) # ["dig1 8 1 5 1","dig2 3 6"]
            else:
                arr2.append(log) #  ["let1 art can","let2 own kit dig","let3 art zero"]
        
        arr2.sort(key = lambda x: (x.split()[1:], x.strip().split()[0]))
        
        return arr2 + arr1
                
                
               