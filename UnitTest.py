
class Dict(dict):
    def __init__(self, **kw):
        super().__init__(self, **kw)
    
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(f"Dict has no attribute {key}")
    
    def __setattr__(self, key, val):
        self[key] = val

import unittest

class TestDict(unittest.TestCase):
    def setUp(self):
        print("Setting up")
    
    def tearDown(self):
        print("Tearing down")

    def test_init(self):
        print("Testing init...")
        d = Dict(a=1, b="test", c=100.23)
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, "test")
        self.assertTrue(isinstance(d, Dict))
    
    def test_key(self):
        print("Testing key...")
        d = Dict()
        d['key'] = 'val'
        self.assertEqual(d.key, 'val')
    
    def test_attr(self):
        d = Dict()
        d.key = 'val'
        self.assertIn('key', d)
        self.assertEqual(d['key'], 'val')
    
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            val = d["key1"]
    
if __name__ == '__main__':
    unittest.main()