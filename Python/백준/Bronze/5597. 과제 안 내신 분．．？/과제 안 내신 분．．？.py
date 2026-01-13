import sys
data = list(map(int, sys.stdin.read().split()))



li = [*range(1,31)]

new_li = [i for i in li if i not in data]

print(f'{new_li[0]}\n{new_li[1]}')
