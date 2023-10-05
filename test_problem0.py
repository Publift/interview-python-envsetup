import unittest

from problem0 import Problem0


class Problem0Test(unittest.TestCase):
    def test_Problem0(self):
        p = Problem0()
        assert p.add(2, 3) == 5
