# -*- coding: UTF-8 -*-
from multiprocessing import Pool
import time

class BatchProcessor():
    def __init__(self):
        super().__init__()
    
    def Process(self, items, batch_size, worker):
        assert items and hasattr(items, "__len__")
        assert batch_size > 0
        assert worker

        items_num = len(items)
        quotient = items_num // batch_size
        remainder = items_num % batch_size
        
        batch_number = quotient if remainder == 0 else quotient + 1
        pool = Pool(batch_size)

        for batch_idx in range(batch_number):
            start_idx = batch_idx * batch_size
            end_idx = (start_idx + batch_size) if (start_idx + batch_size) <= items_num else items_num
            pool.map(worker, items[start_idx: end_idx])

        pool.close()
def __Do_Work(item):
    print(f"Dowing work {item['ID']}")
    time.sleep(1)

if __name__ == '__main__':
    items = [{"ID": i, "Name": f"Item {i}" } for i in range(10)]
    batch_size = 5
    worker = __Do_Work

    bp = BatchProcessor()
    bp.Process(items, batch_size, worker)