import random, time

data = [random.randint(1, 1000) for x in range(10_000_000)]

def get_min(data):
    min_value = data[0]

    for value in data:
        if value < min_value:
            min_value = value

    return min_value

start = time.time()

result1 = get_min(data)
end = time.time()
print(end-start)

result2 = min(data)
end2 = time.time()
print(end2-end)