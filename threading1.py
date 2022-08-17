import concurrent.futures as futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'sleeping {seconds} seconds..')
    time.sleep(seconds)
    return 'done sleeping..'

with futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(do_something,1)
    print(f1.result)

"""threads=[]

for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()  """

finish = time.perf_counter()

print(f'finished in{round(finish-start,2)} second(s)')