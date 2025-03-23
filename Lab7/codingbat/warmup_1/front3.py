def front3(line):
    front_end = 3
    if len(line) < front_end:
        front_end = len(line)
    front = line[:front_end]
    return front + front + front
