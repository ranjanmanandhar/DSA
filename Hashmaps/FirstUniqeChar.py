class Solution:
    def firstUniqChar(self, s: str) -> int:
        charList = {}
        for i, str in enumerate(s):
            if str not in charList:
                charList[str] = 1
            else:
                charList[str] += 1
            
        for i, char in enumerate(s):
            if charList[char] == 1:
                return i
            
        return -1
            
s = Solution()
print(s.firstUniqChar("dddccdbba")) 