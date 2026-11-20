class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            temp = temperatures[i]
            while stack and stack[-1][0] <= temp:
                stack.pop()
            if stack:
                top_idx = stack[-1][1]
                result[i] = top_idx - i
            stack.append((temp, i))

        # for res in result:
        #     print(res)

        return result
        
