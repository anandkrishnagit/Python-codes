def print_num(n):
    if n > 0:
        print_num(n - 1)
        print(n, end = ' ')

print('Numbers from 1 to 100:')
print_num(100)