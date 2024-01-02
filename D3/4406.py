t = int(input())
w = ['a', 'e', 'i', 'o', 'u']
for tt in range(1, t + 1):
    word = input()
    print(f'#{tt}', end = ' ')
    for s in word:
        if s in w:
            continue
        print(s, end = '')
    print()

 