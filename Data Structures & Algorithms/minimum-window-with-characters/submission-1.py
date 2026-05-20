class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        s_counts = dict()
        t_counts = dict()

        for char in t:
            t_counts[char] = t_counts.get(char, 0) + 1
            s_counts[char] = 0

        l, r = 0, 0
        have, shortest = 0, ""
        curr_str = ""

        while r < len(s):
            while l < len(s) and s[l] not in t_counts:
                l += 1
                r = l

            if l == len(s):
                break

            curr = s[r]

            if curr in t_counts:
                if t_counts[curr] != s_counts[curr]:
                    s_counts[curr] += 1
                    have += 1
            
            curr_str += curr

            if have == len(t):
                if shortest == "" or len(curr_str) < len(shortest):
                    shortest = curr_str
                
                curr_str = ""
                have = 0
                l += 1
                r = l

                for char in s_counts:
                    s_counts[char] = 0

            else:
                r += 1

        return shortest
            
            


            

