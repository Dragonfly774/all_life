# # text = open('some_file.txt', 'r')
# # print(text)
# # lines = len(open('some_file.txt').readlines())
# # count = 0
# # listt = [str(i) for i in range(0, 10)]
# # for i in listt:
# #
# #     count += text.read().count(i)
# #     print(count)
# # #
# with open("some_file.txt", "rt") as file:
#     text = file.read()
#
# for digit in "0123456789":
#     print(f"{digit} {text.count(digit)}")
isvowel = 0
vowel = "аяоеуюыиэеё"


def vowel_count(word):
    return len(list(filter(lambda x: x in vowel, word)))


with open('some_file.txt', mode='r', encoding='utf-8') as f:
    rawtext = f.read()
    lines = len(rawtext.split('\n'))

isvowel = len(set(filter(lambda x: x in vowel, rawtext)))
istitle = sum(map(lambda x: 1 if x.istitle() else 0, rawtext.split()))
isnumber = sum(map(lambda x: 1 if x.isnumeric() else 0, rawtext))

words = map(lambda x: (x, vowel_count(x)), rawtext.split())
words = sorted(words, key=lambda x: x[1], reverse=True)
words = filter(lambda x: x[1] != 0, words)

words = ' '.join(x[0] for x in words)



