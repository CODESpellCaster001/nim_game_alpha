def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_set_below_n(n):
    prime_set = set()
    for num in range(2, n):
        if is_prime(num):
            prime_set.add(num)
    return prime_set

try:
    n = int(input("请输入一个大于2且大于100的自然数："))
    if n <= 2 or n <= 100:
        print("输入的数字必须大于2且大于100。")
    else:
        primes = prime_set_below_n(n)
        print(f"小于{n}的所有素数组成的集合：{primes}")
except ValueError:
    print("输入无效，请输入一个整数。")
