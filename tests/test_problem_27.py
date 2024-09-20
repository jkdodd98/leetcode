from leetcode.problem_27 import Solution


class TestSolution:
    def setup_method(self):
        self.func = Solution().removeElement

    def test_case_1(self):
        res = self.func(nums=[3, 2, 2, 3], val=3)
        ans = 2
        assert res == ans

    def test_case_2(self):
        res = self.func(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=0)
        ans = 6
        assert res == ans

    def test_case_3(self):
        res = self.func(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=1)
        ans = 7
        assert res == ans

    def test_case_4(self):
        res = self.func(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2)
        ans = 5
        assert res == ans

    def test_case_5(self):
        res = self.func(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=3)
        ans = 7
        assert res == ans

    def test_case_6(self):
        res = self.func(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=4)
        ans = 7
        assert res == ans
