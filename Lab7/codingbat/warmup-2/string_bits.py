def string_bits(line):
    result = ""
    for i in range(len(line)):
        if i % 2 == 0:
            result = result + line[i]
    return result
