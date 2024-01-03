class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        curr = []
        prev = self.countAndSay(n - 1)
        count = 0
        
        for i in range(len(prev)):
            count += 1
            if i == len(prev) - 1 or prev[i] != prev[i + 1]:
                curr.append(str(count)) 
                curr.append(str(prev[i]))
                count = 0
                
        return "".join(curr)