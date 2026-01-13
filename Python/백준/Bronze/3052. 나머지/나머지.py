import sys

data = list(map(int, sys.stdin.read().split()))


my_li = []

for i in data:
	my_li.append(i%42)


print(len(set(my_li)))