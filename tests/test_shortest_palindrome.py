from leetcode.shortest_palindrome import Solution


class TestSolution:
    def setup_method(self):
        self.func = Solution().shortestPalindrome

    def test_case_1(self):
        res = self.func("aacecaaa")
        ans = "aaacecaaa"
        assert res == ans

    def test_case_2(self):
        res = self.func("abcd")
        ans = "dcbabcd"
        assert res == ans

    def test_case_3(self):
        res = self.func("a")
        ans = "a"
        assert res == ans

    def test_case_4(self):
        res = self.func("racecar")
        ans = "racecar"
        assert res == ans

    def test_case_5(self):
        res = self.func("baa")
        ans = "aabaa"
        assert res == ans

    def test_case_6(self):
        res = self.func("abc")
        ans = "cbabc"
        assert res == ans

    def test_case_7(self):
        res = self.func("fgfhf")
        ans = "fhfgfhf"
        assert res == ans

    def test_case_8(self):
        res = self.func("zoog")
        ans = "goozoog"
        assert res == ans

    def test_case_9(self):
        res = self.func("rqiqreur")
        ans = "ruerqiqreur"
        assert res == ans

    def test_case_10(self):
        res = self.func("qwerty")
        ans = "ytrewqwerty"
        assert res == ans
