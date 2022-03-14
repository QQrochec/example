"""Много четных чисел из последовательности Фибоначчи"""
def even(n):
    fib_nums = [0, 1]
    yield 0
    for _ in range(n*3 - 2):
        next = fib_nums[-1] + fib_nums[-2]
        fib_nums.pop(0)
        fib_nums.append(next)
        if next % 2 == 0:
            yield next


for i in even(int(input())):
    print(i, end='\t')

