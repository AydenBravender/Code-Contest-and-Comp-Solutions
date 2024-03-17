num = int(input())
p = 0
w = 0
k = 0
for i in range(num):
    inp = input()
    if inp == 'phone':
        p = 1
    if inp == 'wallet':
        w = 1
    if inp == 'keys':
        k = 1

if p+k+w < 3:
    if k == 0:
        print("keys")
    if p == 0:
        print("phone")
    if w == 0:
        print("wallet")
else:
    print("ready")

