# -*- coding: UTF-8 -*-
from threading import Thread

class BatchProcessor():
    def __init__(self):
        super().__init__()
    
    def Process(self, rows, batch_size, worker):
        assert rows and isinstance(rows, list)
        assert batch_size > 0
        assert worker

        rows_num = len(rows)
        quotient = rows_num // batch_size
        remainder = rows_num % batch_size
        
        batch_number = quotient if remainder == 0 else quotient + 1

        for batch_idx in range(batch_number):
            threads = []
            start_idx = batch_idx * batch_size
            end_idx = (start_idx + batch_size) if (start_idx + batch_size) <= rows_num else rows_num
            for row in rows[start_idx: end_idx]:
                t = Thread(target=worker, args=(row,))
                threads.append(t)
                t.start()
            
            for t in threads:
                t.join()

def __Do_Work(row):
    print(f"Dowing work {row['ID']}")

if __name__ == '__main__':
    rows = [{"ID": i, "Name": f"Item {i}" } for i in range(10)]
    batch_size = 5
    worker = __Do_Work

    bp = BatchProcessor()
    bp.Process(rows, batch_size, worker)