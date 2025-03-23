def string_splosion(line):
    result = ""
    for i in range(len(line)):
        result = result + line[:i + 1]
    return result
