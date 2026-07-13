
import string

import random
import time
list1=[]
for i in range(200000):
    suff="".join(random.choices(string.ascii_lowercase, k=4))
    list1.append(f"user_{suff}")
target="zzzz"
start=time.perf_counter()
for _ in range(1000):
    if target in list1:
        print("Found")

end=time.perf_counter()
listtime=end - start
print(f"Time taken: {listtime} seconds for list search")
set1=set(list1)
start=time.perf_counter()
for _ in range(1000):
    if target in set1:
        print("Found")

end=time.perf_counter()
settime=end - start
print(f"Time taken: {settime} seconds for set search")
performanceratio=listtime/settime
print(f"set is {performanceratio}x times faster than list")