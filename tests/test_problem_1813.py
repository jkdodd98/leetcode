from leetcode.problem_1813 import Solution


class TestSolution:
    def setup_method(self) -> None:
        self.func = Solution().areSentencesSimilar

    def test_case_1(self) -> None:
        res = self.func(sentence1="My name is Haley", sentence2="My Haley")
        ans = True
        assert res == ans

    def test_case_2(self) -> None:
        res = self.func(sentence1="of", sentence2="A lot of words")
        ans = False
        assert res == ans

    def test_case_3(self) -> None:
        res = self.func(sentence1="Eating right now", sentence2="Eating")
        ans = True
        assert res == ans

    def test_case_4(self) -> None:
        res = self.func(sentence1="Luky", sentence2="Lucccky")
        ans = False
        assert res == ans

    def test_case_5(self) -> None:
        res = self.func(sentence1="Ogn WtWj HneS", sentence2="Ogn WtWj HneS")
        ans = True
        assert res == ans

    def test_case_6(self) -> None:
        res = self.func(sentence1="B", sentence2="ByI BMyQIqce b bARkkMaABi")
        ans = False
        assert res == ans

    def test_case_7(self) -> None:
        res = self.func(sentence1="aAB", sentence2="ARkk MaAB")
        ans = False
        assert res == ans

    def test_case_8(self) -> None:
        res = self.func(sentence1="hello", sentence2="hello world python")
        ans = True
        assert res == ans

    def test_case_9(self) -> None:
        res = self.func(sentence1="python", sentence2="hello world python")
        ans = True
        assert res == ans

    def test_case_10(self) -> None:
        res = self.func(sentence1="world", sentence2="hello world python")
        ans = False
        assert res == ans

    def test_case_11(self) -> None:
        res = self.func(sentence1="A", sentence2="a A b A")
        ans = True
        assert res == ans

    def test_case_12(self) -> None:
        res = self.func(sentence1="c h p Ny", sentence2="c BDQ r h p Ny")
        ans = True
        assert res == ans
