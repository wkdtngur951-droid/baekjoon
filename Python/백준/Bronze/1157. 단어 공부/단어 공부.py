t = input().upper()

t_li = list(set(t))
counts = []
for w in t_li:
    counts.append(t.count(str(w)))

m = max(counts)

if counts.count(m) > 1:
    print('?')

else:
    print(t_li[counts.index(m)])
