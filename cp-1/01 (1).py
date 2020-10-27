with open('stomach.txt', encoding='utf8', mode='r') as file:
    first, second = file.read().lower().splitlines()
    first = list(first)
    result = []

    for let in second:
        if let in first:
            result.append(first.index(let))
        else:
            result = None
            break

    result = str(tuple(result)) if result else 'None'
    f = open('food.txt', 'w')
    f.write(result)
    f.close()
