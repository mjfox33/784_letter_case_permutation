import code_784_letter_case_permutation as c

def test_example_1():
    s = c.Solution()
    assert sorted(s.letterCasePermutation("a1b2")) == sorted(["a1b2","a1B2","A1b2","A1B2"])

def test_example_2():
    s = c.Solution()
    assert sorted(s.letterCasePermutation("3z4")) == sorted(["3z4","3Z4"])