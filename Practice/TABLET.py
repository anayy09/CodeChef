# Buying New Tablet

for test in range(int(input())):
    n,b = map(int,input().split())
    l = []
    for i in range(n):
        w,h,p = map(int,input().split())
        if p <= b:
            l.append(w*h)
    if len(l) == 0:
        print("no tablet")
    else:
        print(max(l))
  
