with open('castle.txt', mode='r', encoding='utf-8') as f:
    rawtext = f.read().lower()
    words = rawtext.split()

stroka = ' '.join(words)
s = []
for i in words:
    for j in i:
        s.append(j)
a = sorted(s)
count = 0
for i in range(len(s)):
    if a[i] in s[i]:
        count += 1
with open("verdict.txt", mode="w") as out:
    if count == len(s):
        out.write("OKAY")
    else:
        out.write(''.join(s[count:]))
