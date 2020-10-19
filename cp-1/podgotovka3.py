class INeedAtLeastSomething(Exception):
    pass


class TooEasyForMe(Exception):
    pass


def words_analyser(*args, real=-1):
    if list(filter(lambda x: '.' in str(x), *args)):
        raise TooEasyForMe('Даже смотреть на них не буду')
    # return list(filter(lambda x: x > real, *args))


nums = [5, 10, 15, 12]
num = 5
answer = words_analyser(nums, real=num)
print(answer)

print('___________________________________--')

nums = []
answer = words_analyser(nums)
print(answer)
