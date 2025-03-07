def even_fibonacci_sum(n):
    a, b = 0, 1
    even_sum = 0
    while b <= n:
        if b % 2 == 0:
            even_sum += b
        a, b = b, a + b
    return even_sum

# Get input from the user
N = int(input("Enter a number N: "))
print("Sum of even Fibonacci numbers:", even_fibonacci_sum(N))
