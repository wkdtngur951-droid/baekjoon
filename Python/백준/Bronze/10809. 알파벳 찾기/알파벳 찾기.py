S = input()

a = 'abcdefghijklmnopqrstuvwxyz'
result = []

for i in range(len(a)):
	if a[i] in S:
		result.append(S.index(a[i]))
	else:result.append(-1)

print(*result, sep = ' ')