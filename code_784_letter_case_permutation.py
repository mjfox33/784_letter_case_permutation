class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        ans = [""]
        for char in s:
            ans = [x + current_char for x in ans for current_char in {char, char.swapcase()}]
        return ans