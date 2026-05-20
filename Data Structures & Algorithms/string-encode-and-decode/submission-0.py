class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for stri in strs:
            n = len(stri)
            res += f"{n}#{stri}"
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s): 
            j = i + 1
            while s[j] != '#':
                j += 1
            strlen = int(s[i:j])
            res.append(s[j+1 : j+strlen+1])
            i = j + strlen + 1

        return res