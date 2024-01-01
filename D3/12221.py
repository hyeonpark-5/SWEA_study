t = int(input())
for tt in range(1, t + 1):
    a, b = map(int, input().split())
    if a >= 10 or b >= 10:
        print(f'#{tt} {-1}')
    else:
        print(f'#{tt} {a * b}')
