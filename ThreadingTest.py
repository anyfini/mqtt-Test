import threading
import time

start = time.perf_counter()
print(start)

def do_something():
    print("sleeping  sec")
    time.sleep(1)
    print("Done sleeping")

threads = []

for x in range(10):
    t = threading.Thread(target=do_something)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')