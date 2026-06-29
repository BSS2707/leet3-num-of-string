class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        return sum(p in word for p in patterns)


# Example usage
patterns = ["a", "abc", "bc", "d"]
word = "abc"

sol = Solution()
print(sol.numOfStrings(patterns, word))  # Output: 3
