second = []
third = []
area = 0
first_row = input()
second_row = input()
third_row = input()

second = second_row.split(" ")
third = third_row.split(" ")

second = [eval(i) for i in second]
third = [eval(i) for i in third]

for i in range(int(first_row)):
    value = second[i]*third[i]
    value1 = second[i+1]-second[i]
    value2 = value1*third[i]
    value3 = value2/2
    area = area + value3 + value

print(area)
