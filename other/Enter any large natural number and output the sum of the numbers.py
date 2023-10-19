def sum_of_digits(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n //= 10
    return total

num = int(input("请输入一个自然数："))
result = sum_of_digits(num)
print(f"各位数字之和为：{result}")
