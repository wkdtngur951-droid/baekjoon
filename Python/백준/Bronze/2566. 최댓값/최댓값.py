import sys

nums = [*map(int,sys.stdin.read().split())]

idx = nums.index(max(nums))

print(max(nums))
print(idx//9 + 1, idx%9 + 1)