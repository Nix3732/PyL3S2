n = int(input())
m = [str(input()) for i in range(n)]
c = 0
f = []
for i in range(len(m)-1):
    for j in range(i+1, len(m)):
        if i == j:
            c += 1
    f.append(c)
print(f)