def count_valleys(steps, path):
    level = 0 
    valleys = 0

    for step in path:
        if step == "U":
            level += 1
        else:
            level -= 1

        if step == "U" and level == 0:
            valleys += 1

    return valleys




steps = 12
path = "DDUUDDUDUUUD"
valley_count = count_valleys(steps, path)
print(valley_count)
