def is_armstrong_number(n):
    num_str = str(n)
    power = len(num_str)
    return sum(int(digit)** power for digit in num_str) == n