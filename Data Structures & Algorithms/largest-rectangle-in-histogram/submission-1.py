class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and h <= stack[-1][1]:
                popped_index, popped_height = stack.pop()
                max_area = max(max_area, popped_height * (i - popped_index))
                start = popped_index
            stack.append((start,h))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area

            