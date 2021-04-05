import unittest
from batchprocessing import BatchProcessor
import time
import random

class TestBatchProcessor(unittest.TestCase):
    def __do_work(self, item):
        print(f"Dowing work {item['ID']}")
        time.sleep(random.randint(1, 10))
        print(f"Finished work {item['ID']}")

    def test_normal(self):
        items = [{"ID": i, "Name": f"Item {i}" } for i in range(10)]
        batch_size = 5
        worker = self.__do_work

        bp = BatchProcessor()
        bp.Process(items, batch_size, worker)


if __name__ == '__main__':
    unittest.main()