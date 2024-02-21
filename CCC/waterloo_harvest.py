nums_rows = int(input())
nums_cols = int(input())
map = []
for i in range(nums_cols):
    map.append(list(input()))
start_row = int(input())
start_col = int(input())
left = nums_rows-start_row
next = nums_rows-left
harvest = []
value = 0

for j in range(next):
    i = 0
    try:
        while map[start_row+j][start_col+i] != '*':
            harvest.append(map[start_row+j][start_col+i])
            i = i + 1
    except IndexError:
        pass

    try:
        i = 1
        while map[start_row+j][start_col-i] != '*':
            harvest.append(map[start_row+j][start_col-i])
            i = i + 1
    except IndexError:
        pass


for j in range(left):
    i = 0
    try:
        while map[start_row-j-1][start_col+i] != '*':
            harvest.append(map[start_row-j-1][start_col+i])
            i = i + 1
    except IndexError:
        pass
    try:
        i = 1
        while map[start_row-j-1][start_col-i] != '*':
            harvest.append(map[start_row-j-1][start_col-i])
            i = i + 1
    except IndexError:
        pass

for i in range(len(harvest)):
    if harvest[i] == 'S':
        value = value + 1
    if harvest[i] == 'M':
        value = value + 5
    if harvest[i] == 'L':
        value = value + 10
print(value)
