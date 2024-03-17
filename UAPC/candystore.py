N, Q = input().split()
N = int(N)
Q = int(Q)

names = []
names1 = []
found = 0
list = []

for i in range(N):
    first, last = input().split()
    names.append(first[0]+last[0])
    names1.append(F"{first} {last}")

for i in range(Q):
    inp = input()
    list.append(inp)



for i in range(Q):
    occ = names.count(list[i])
    if occ > 1:
        print("ambiguous")
    elif occ < 1:
        print("nobody")
    else:
        index = names.index(list[i])
        print(names1[index])


        
