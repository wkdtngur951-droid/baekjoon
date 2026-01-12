import sys


N, M, *nums = map(int, sys.stdin.read().split())


i_ = []
j_ = []

list1 = [*range(1,N+1)]

for num in range(M):
	i_.append(nums[2*num])
	j_.append(nums[2*num+1]) 

for i,j in zip(i_,j_):
	list1[i-1], list1[j-1] = list1[j-1], list1[i-1]



print(*list1)
