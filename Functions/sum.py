def sum_all_nums(*args):
    print(args)
    total = 0
    for num in args:
        total += num
    print(total)

nums = (1,2,3,4,5,6)
print(*nums)
sum_all_nums(*nums)
