def front_times(line, n):
    front_len = 3
    if front_len > len(line):
        front_len = len(line)
    front = line[:front_len]

    result = ""
    for i in range(n):
        result = result + front
    return result
