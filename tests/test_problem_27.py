from leetcode.problem_27 import Solution


class TestSolution:
    def setup_method(self) -> None:
        self.func = Solution().removeElement

    def test_case_1(self) -> None:
        res = self.func(nums=[3, 2, 2, 3], val=3)
        ans = 2
        assert res == ans

    def test_case_2(self) -> None:
        res = self.func(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=0)
        ans = 6
        assert res == ans

    def test_case_3(self) -> None:
        res = self.func(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=1)
        ans = 7
        assert res == ans

    def test_case_4(self) -> None:
        res = self.func(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2)
        ans = 5
        assert res == ans

    def test_case_5(self) -> None:
        res = self.func(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=3)
        ans = 7
        assert res == ans

    def test_case_6(self) -> None:
        res = self.func(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=4)
        ans = 7
        assert res == ans
