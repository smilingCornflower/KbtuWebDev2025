def caught_speeding(speed, is_birthday):
    allowance = 5 if is_birthday else 0
    if speed <= 60 + allowance:
        return 0
    elif speed <= 80 + allowance:
        return 1
    else:
        return 2
