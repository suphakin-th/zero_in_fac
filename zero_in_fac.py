def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)


def find_zero(result_num, c_zero):
    while result_num[-1] == '0':
        c_zero += 1
        result_num = result_num[:len(result_num)-1]
    return c_zero


num = int(input('ENTER NUMBER YOU WANT TO FIND ZERO : ').strip())
result = factorial(num)
count_zero = find_zero(str(result), 0)
print('%s ! = %s Have \'0\' last extend %s digit' % (num, result, count_zero))
