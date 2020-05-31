import unittest
from algo_examples.array import Array


class TestArray(unittest.TestCase):
    """
    Test that the result sum of all numbers
    """
    def test_sum(self):
        """
        정상작동 확인
        :return: 합계 (int)
        """
        instance = Array()
        result = instance.sum(6, '1 2 3 4 10 11')
        self.assertEqual(result, 31)

    def test_sum_raise_exception(self):
        """
        잘못된 입력에 대해 Exception 이 일어나는지 확인
        :return: Exception
        """
        self.assertRaises(Exception, lambda: Array().sum(5, '1 2 3 4 10 11'))