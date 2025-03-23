def not_string(line: str):
    if line.startswith("not"):
        return line
    return "not " + line
