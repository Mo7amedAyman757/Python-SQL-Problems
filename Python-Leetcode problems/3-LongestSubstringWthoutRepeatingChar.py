class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        maxLength = start = 0
        
        for i in range(len(s)):
            # If the character is already in the map and 
            # the start index is less than or equal to the last index of the character,
            # update the start index to be one more than the last index of the character.
            if s[i] in map and start <= map[s[i]]:
                start = map[s[i]] + 1
            
            # If the character is not in the map or the start index is greater than the last index of the character,
            # update the maxLength to be the maximum of the current maxLength and the length of the current substring.
            else:
                maxLength = max(maxLength, i-start+1)
                
            # Update the last index of the character in the map.
            map[s[i]] = i
        return maxLength
    
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbbabcd"))