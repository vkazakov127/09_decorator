# -*- coding: utf-8 -*-

def is_prime(func):
    def wrapper(*args):
        n = func(*args)
        if n % 2 == 0:
            message = 'Составное'
            return n, message
        d = 3
        while d * d <= n and n % d != 0:
            d += 2
        message = 'Простое' if d * d > n else 'Составное'
        return n, message

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


print(f'5 + 6 + 7 = {sum_three(5, 6, 7)[0]}, {sum_three(5, 6, 7)[1]}')
print(f'5 + 6 + 8 = {sum_three(5, 6, 8)[0]}, {sum_three(5, 6, 8)[1]}')
