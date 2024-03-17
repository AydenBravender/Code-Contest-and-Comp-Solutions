N , K = input().split()
unique = 0
total_unique = 0

list = []

for i in range(int(N)):
    list.append(input().split())

for j in range(int(N)):
    unique_set = set(list[j])
    # Count unique values
    unique = len(unique_set)
    
    total_unique = total_unique + (int(K) - unique)
print(total_unique)

