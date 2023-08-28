#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise ValueError("Value of 'i' exceeds 'a'")
            result += (a ** b) / i
        except ValueError as e:
            result = b + a
            print(f"Caught exception: {e}")
            break

    return result

