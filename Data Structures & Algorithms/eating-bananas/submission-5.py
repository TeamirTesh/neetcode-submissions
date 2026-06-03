class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        min_k = high


        while low <= high:
            mid = (high + low) // 2
            curr_time = 0
            for pil in piles:
                curr_time += -(pil // -mid)

            if curr_time <= h:
                min_k = min(mid, min_k)
                high = mid - 1
            
            else:
                low = mid + 1

        return min_k