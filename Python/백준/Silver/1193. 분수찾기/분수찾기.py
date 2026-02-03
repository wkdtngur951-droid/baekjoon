X = int(input())

g = 1
l = 2

while X > g:
	g += l
	l += 1



if l%2 == 0:
	print(g-X+1,'/',(l-(g-X+1)), sep ='')
else:
	print((l-(g-X+1)),'/',g-X+1, sep ='')
