def multiply(num1, num2):
    result = 0
    for i in range(num2):
        result += num1
    return result

def raise_to_power(num, exponent):
    result = 1
    for i in range(exponent):
        result = multiply(result, num)
    return result

def square(num):
    return raise_to_power(num, 2)

print(multiply(5,10))
print(raise_to_power(5,10))
print(square(5))