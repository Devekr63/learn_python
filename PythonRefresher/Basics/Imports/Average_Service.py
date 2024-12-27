def average(values):
    average = 0
    if type(values) is dict:
        for value in values.values():
           average += value
    elif type(values) is list:
        for value in values:
            average += value
    average = average / len(values)
    return round(average)
