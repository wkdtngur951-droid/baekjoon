import sys

N , *m = sys.stdin.read().split()
N = int(N)

fe = []

for i in range(N):
	fe.append(m[i][0] + m[i][-1])


print(*fe, sep = '\n')