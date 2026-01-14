import sys

N, m = sys.stdin.read().split()
m_ = 0

for i in range(int(N)):
	m_ += int(m[i])

print(m_)