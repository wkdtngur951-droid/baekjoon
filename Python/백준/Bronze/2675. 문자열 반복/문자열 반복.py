import sys

T, *RS = sys.stdin.read().split()

T = int(T)
R = [RS[2*i] for i in range(T)]
S = [RS[2*i+1] for i in range(T)]

R = [*map(int,R)]

result = []

for i in range(T):
	for j in range(len(S[i])):
		result.append(S[i][j]*R[i])

split_sizes = []
for i in range(len(S)):
    split_sizes.append(len(S[i]))

start = 0
for size in split_sizes:
    end = start + size
    print(*result[start:end],sep='')
    start = end