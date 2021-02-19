class Count:
    def add(self, a, b):
        return a + b

import unittest
import mock

class TestCount(unittest.TestCase):
    def test_add(self):
        c = Count()
        c.add = mock.Mock(return_value = 10)
        result = c.add(1,2)
        self.assertEqual(result, 10)
    
    def test2(self):
        client = mock.Mock()
        client.send_request.return_value = 200
        result = client.send_request()
        self.assertEqual(result, 200)


if __name__ == '__main__':
    unittest.main()