def get_min(data):
    min_value = data[0]

    for value in data:
        if value < min_value:
            min_value = value

    return min_value

def get_max(data):
    max_value = data[0]

    for value in data:
        if value > max_value:
            max_value = value

    return max_value

def get_sum(data):
    summary = 0

    for value in data:
        summary += value

    return summary

def get_avg(data):
    summary = 0

    for value in data:
        summary += value

    avg = summary/len(data)
    return avg

print(get_min([8, 2, 7238]))
print(get_max([8, 2, 7238]))
print(get_sum([8, 2, 7238]))
print(get_avg([8, 2, 7238]))
