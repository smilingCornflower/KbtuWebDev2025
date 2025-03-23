def front_back(line):
    if len(line) <= 1:
        return line
    mid = line[1:len(line) - 1]
    return line[len(line) - 1] + mid + line[0]
