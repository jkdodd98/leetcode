from leetcode.problem_2491 import Solution


class TestSolution:
    def setup_method(self) -> None:
        self.func = Solution().dividePlayers

    def test_case_1(self) -> None:
        res = self.func([3, 2, 5, 1, 3, 4])
        ans = 22
        assert res == ans

    def test_case_2(self) -> None:
        res = self.func([3, 2, 5, 1, 3, 4])
        ans = 22
        assert res == ans

    def test_case_3(self) -> None:
        res = self.func([1, 1, 2, 3])
        ans = -1
        assert res == ans

    def test_case_4(self) -> None:
        res = self.func([1, 1, 1, 2, 3, 3, 3, 7, 7, 8, 8, 8, 9, 9])
        ans = -1
        assert res == ans

    def test_case_5(self) -> None:
        res = self.func([40, 24, 16, 14])
        ans = -1
        assert res == ans

    def test_case_6(self) -> None:
        res = self.func([3, 5])
        ans = 15
        assert res == ans

    def test_case_7(self) -> None:
        res = self.func([18, 14, 3, 19, 9, 6, 18, 3, 4, 19])
        ans = -1
        assert res == ans

    def test_case_8(self) -> None:
        res = self.func([1, 2, 3, 2, 4, 6])
        ans = -1
        assert res == ans

    def test_case_9(self) -> None:
        res = self.func([2, 2, 5, 12, 12, 10, 9, 4])
        ans = 133
        assert res == ans
