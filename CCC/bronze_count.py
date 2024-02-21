N = int(input())
list = []
for i in range(N):
    list.append(int(input()))

list.sort(reverse = True)


gold = list[0]

i = 0
next = list[i]

while next == gold:
    i = i + 1
    next = list[i]

silver = list[i]

j = 0
next_b = list[i+j]

while next_b == silver:
    j = j + 1
    next_b = list[i+j]

bronze = list[i+j]

k = 0
next_k = list[i+j+k]

while next_k == bronze:
    k = k + 1
    try:
        next_k = list[i+j+k]
    except IndexError:
        next_k = next_k+10

print(bronze, k)


