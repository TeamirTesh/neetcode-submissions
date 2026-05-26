class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key=lambda x: -x[0])
        times, stack = [], []

        for car in cars:
            time = (target - car[0]) / car[1]
            times.append(time)

        for time in times:
            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)

