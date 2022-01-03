class Solution:
    def checkString(self, s: str) -> bool:
        if 'a' not in s or 'b' not in s:
            return True
        else:
            for c in range(len(s) - 1):
                if s[c] == 'b':
                    if s[c + 1] == 'a':
                        return False
            return True
