def last2(line):
    if len(line) < 2:
        return 0
    last2 = line[len(line) - 2:]
    count = 0
    for i in range(len(line) - 2):
        sub = line[i:i + 2]
        if sub == last2:
            count = count + 1

    return count
