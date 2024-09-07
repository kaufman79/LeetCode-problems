
class Solution:
    def romanToInt(self, str: str) -> int:
        map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        ans = 0

        for i in range(len(str)):
            if i < len(str) - 1 and map[str[i]] < map[str[i + 1]]:
                ans -= map[str[i]]
            else:
                ans += map[str[i]]

        return ans

sol = Solution()
print(sol.romanToInt("MMXXIV"))
