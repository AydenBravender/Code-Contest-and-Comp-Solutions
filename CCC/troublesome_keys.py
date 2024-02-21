typing = input()
result = input()

typing_list = list(typing)
result_list = list(result)
quiet_key = '-'
j = 0
k = 0

if len(typing_list) == len(result_list):
    k = 'pass_it'

for i in range(len(typing_list)):
    try:
        if typing_list[i] != result_list[i-j]:
            if quiet_key == '-' and k != 'pass_it':
                if typing_list[i+1] == result_list[i-j]:
                        quiet_key = typing_list[i]
                        j = j + 1
                else:
                    silly_key_p = typing_list[i]
                    silly_key_r = result_list[i-j]
            else:
                if typing_list[i] == quiet_key:
                    j = j + 1
                else:
                    silly_key_p = typing_list[i]
                    silly_key_r = result_list[i-j]
    except IndexError:
        quiet_key = typing_list[i]
         

print(silly_key_p, silly_key_r)
print(quiet_key)
