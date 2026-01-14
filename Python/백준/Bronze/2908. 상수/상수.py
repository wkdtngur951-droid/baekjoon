import sys

nums = sys.stdin.read().split()

n1 = nums[0][::-1]
n2 = nums[1][::-1]

print(max(int(n1),int(n2)))