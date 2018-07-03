import unittest
from myDict import *

class TestDict(unittest.TestCase):

    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')
        

    def test_Init(self):
        d = Dict(a=1, b='abc')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'abc')
        self.assertTrue(isinstance(d, Dict))
    
    def test_keyError(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['key']

if __name__ == '__main__':
    unittest.main()