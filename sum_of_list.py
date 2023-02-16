def sum_of_list(list):
    return sum(list)

num_list = []
while True:
    num = input('請輸入要加入清單中的數字: ')
    if num == 'q':
        print('stop')
        break
    num = int(num)
    num_list.append(num)

print(sum_of_list(num_list))