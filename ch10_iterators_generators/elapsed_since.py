import time

def elapsed_since(data):
    last_time = None
    for item in data:
        current_time = time.perf_counter()
        delta = current_time - (last_time or current_time)
        last_time = current_time
        yield delta, item


for t in elapsed_since('abcd'):
    print(t)
    time.sleep(2)

print(list(elapsed_since('efgh')))