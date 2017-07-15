import unittest

from factorial import fact

class TestFactorial(unittest.TestCase):

	def test_fact(self):
	
		res = fact(5)
		self.assertEqual(res, 120)

	def test_error(self):
		
		self.assertTaises(ZeroDivisonError, div, 0)

if __name__=='__main__':
	unittest.main()


