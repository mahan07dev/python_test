import pandas as pd

# تابع برای محاسبه فاکتوریل
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# تابع برای یافتن عوامل اول
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# تابع برای محاسبه جمع تا عدد
def sum_to_n(n):
    return n * (n + 1) // 2

# اعداد اولیه
numbers = [10, 11, 12]

# ایجاد دیکشنری برای DataFrame
data = {
    'Number': numbers,
    'Prime Factors': [prime_factors(num) for num in numbers],
    'Factorial': [factorial(num) for num in numbers],
    'Sum to Number': [sum_to_n(num) for num in numbers],
}

# ایجاد DataFrame
df = pd.DataFrame(data)

print(df)