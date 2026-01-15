w = input()
c_li = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for c in c_li:
    if c in w:
        w = w.replace(c,'a')


print(len(w))
