import sys

N, *m = map(int, sys.stdin.read().split())

M = max(m)

new_m = [x/M*100 for x in m]

print(sum(new_m)/len(new_m))