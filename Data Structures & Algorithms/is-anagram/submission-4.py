class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        f1 = {}
        f2 = {}

        for sc, tc in zip(s,t):
            f1[sc] = f1.get(sc, 0) + 1
            f2[tc] = f2.get(tc, 0) + 1
        for key in f1:
            if key not in f2 or f1[key] != f2[key]:
                return False
        return True
        



        