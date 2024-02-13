import sys
import unittest as test
sys.path.insert(0 , 'E:\Projects\exercises')
from string_ending import solution

fixed_tests_True = (
    ( "samurai", "ai"    ),
    ( "ninja",   "ja"    ),
    ( "sensei",  "i"     ),
    ( "abc",     "abc"   ),
    ( "abcabc",  "bc"    ),
    ( "fails",   "ails"  ),
)

fixed_tests_False = (
    ( "sumo",    "omo"   ),
    ( "samurai", "ra"    ),
    ( "abc",     "abcd"  ),
    ( "ails",    "fails" ),
    ( "this",    "fails" ),
    ( "spam",    "eggs"  )
)

@test.describe("Fixed Tests")
def test_group():
    @test.it("True Cases")
    def test_case():
        for text, ending in fixed_tests_True:
            test.assert_equals(solution(text, ending), True, f"Incorrect answer for:\n    text = '{text}'\n  ending = '{ending}'\nAssertion failed")
    @test.it("False Cases")
    def test_case():
        for text, ending in fixed_tests_False:
            test.assert_equals(solution(text, ending), False, f"Incorrect answer for:\n    text = '{text}'\n  ending = '{ending}'\nAssertion failed")

@test.describe("Random tests")
def test_group():
    for _ in range(100):
        text_length = randint(5,25)
        text = [chr(randint(97, 122)) for _ in range(text_length)]
        ending_length = int(text_length * (.2, .4, .6, .8)[randint(0, 3)])
        ending = text[-ending_length:]
        if randint(0, 1):
            mismaches = int(ending_length * (.1, .2, .3, .4)[randint(0, 3)])
            while (mismaches := mismaches - 1) > 0:
                ending[randint(0, ending_length - 1)] = chr(randint(97, 122))
        text = ''.join(text)
        ending = ''.join(ending)
        expected = text.endswith(ending)
        @test.it(f'Testing for: text = "{text}", ending = "{ending}" to return {expected}')
        def random_test():
            submitted = solution(text, ending)
            test.assert_equals(submitted, expected)