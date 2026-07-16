import json
from pathlib import Path

from studylog import LogEntry
def read_entries(path):
    try:
        data=json.loads(Path(path).read_text())
        for item in data:
            print("Yielding")
            yield LogEntry.from_dict(item)
    except FileNotFoundError:
        print("File not found")
        return
    except json.JSONDecodeError:
        print("file was corrupted")
        return


class Countdown:
    def __init__(self,start):
        self.start=start
    def __iter__(self):
        return self
    def __next__(self):
        if self.start==0:
            raise StopIteration
        value=self.start
        self.start-=1
        return value
count=Countdown(5)
for num in count:
    print(num)

import time

def memory_demo():
    
    start = time.perf_counter()
    result_list = sum([x**2 for x in range(10_000_000)])
    list_time = time.perf_counter() - start
    print(f"List version:      {list_time:.4f}s")

    
    start = time.perf_counter()
    result_gen = sum(x**2 for x in range(10_000_000))
    gen_time = time.perf_counter() - start
    print(f"Generator version: {gen_time:.4f}s")
if __name__ == "__main__":
    for entry in read_entries("study_log.json"):
        print(entry)
    count=Countdown(5)
    for num in count:
        print(num)
    memory_demo()
    

