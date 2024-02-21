dusa_size = int(input())
next_in_line = int(input())


while next_in_line < dusa_size:
    dusa_size = dusa_size + next_in_line
    next_in_line = int(input())

print(dusa_size)
