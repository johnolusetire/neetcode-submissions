class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        chars = [0] * 26

        for sc, tc in zip(s,t):
            chars[ord(sc) - ord('a')] += 1
            chars[ord(tc) - ord('a')] -= 1
        
        return all(x == 0 for x in chars)