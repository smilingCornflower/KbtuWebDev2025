def alarm_clock(day, vacation):
    is_weekend = day == 0 or day == 6
    if vacation:
        return "off" if is_weekend else "10:00"
    return "10:00" if is_weekend else "7:00"
