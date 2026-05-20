class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = dict()
        result = []

        for stri in strs:
            asci = [0] * 26
            for i in range(len(stri)):
                asci[ord(stri[i]) - ord('a')] += 1

            asci = tuple(asci)

            if asci in seen:
                result[seen[asci]].append(stri)
            else:
                result.append([stri])
                seen[asci] = len(result) - 1

        return result

                