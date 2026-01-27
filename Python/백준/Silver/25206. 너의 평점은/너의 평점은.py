import sys

ex = sys.stdin.read().splitlines()
result = []
nums = []
for i in range(len(ex)):
    nms = float(ex[i].split()[1])
    grd = ex[i].split()[2]
    if grd != 'P':
        if grd == 'A+':
            grdnum = 4.5
        elif grd == 'A0':
            grdnum = 4.0
        elif grd == 'B+':
            grdnum = 3.5
        elif grd == 'B0':
            grdnum = 3.0
        elif grd == 'C+':
            grdnum = 2.5
        elif grd == 'C0':
            grdnum = 2.0
        elif grd == 'D+':
            grdnum = 1.5
        elif grd == 'D0':
            grdnum = 1.0
        elif grd == 'F':
            grdnum = 0
        result.append(grdnum*nms)
        nums.append(nms)
            
print(sum(result)/sum(nums))