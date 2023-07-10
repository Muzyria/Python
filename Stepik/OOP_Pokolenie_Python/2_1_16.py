def annual_return(start, percent, years):
    value = start
    for _ in range(years):
        value = value * (1 + percent / 100)
        yield value
