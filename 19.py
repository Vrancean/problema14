M=[]
n=int(input("Dati un numar intre 2 si 10:"))
if n>=2 and n<=10:
    m=n
else:
    print("lungimea nu corespunde")
for a in range(0,m):
    x=[]
    for b in range(0,m):
        b=int(input("Dati un numar:"))
        x.append(b)
    M.append(x)
print(M)
dp=[]
ds=[]
dps=[]
dpj=[]
dss=[]
dsj=[]
for a in range(len(M)):
    for b in range(len(M[0])):
        if a==b:
            dp.append(M[a][b])
        if a+b==(len(M)-1):
            ds.append(M[b][a])
for a in range(len(M)):
    for b in range(len(M[0])):
        if a>b:
            dpj.append(M[a][b])
        if a<b:
            dps.append(M[a][b])
        if a+b<(len(M)-1):
            dss.append(M[a][b])
        if a+b>(len(M)-1):
            dsj.append(M[a][b])
print(f"Suma pe diagonala principala este: {sum(dp)}")
print(f"Suma pe diagonala secundara este: {sum(ds)}")
print(f"Suma de sus a diagonalei princiale este: {sum(dps)}")
print(f"Suma de jos a diagonalei princiale este: {sum(dpj)}")
print(f"Suma de sus a diagonalei secundare este: {sum(dss)}")
print(f"Suma de jos a diagonalei secundare este: {sum(dsj)}")