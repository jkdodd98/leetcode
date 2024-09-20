"""
214. Shortest Palindrome

- Difficulty: Hard
- Acceptance Rate: 36.4%

Topis: string, rolling hash, string matching, hash function

You are given a string s. You can convert s to a palindrome by adding characters in
front of it.

Return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: s = "abcd"
Output: "dcbabcd"


Constraints:

0 <= s.length <= 5 * 104
s consists of lowercase English letters only.
"""


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        length = len(s)
        reverse = s[::-1]

        for i in range(length):
            left = s[: length - i]
            right = reverse[i:]
            if left == right:
                return reverse[:i] + s


if __name__ == "__main__":
    res = Solution().shortestPalindrome("abcd")
    print(res)
