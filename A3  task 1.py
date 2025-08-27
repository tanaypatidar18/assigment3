def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

sample_number =(int(input("Enter a number: ")))
print(f"Factorial of {sample_number} is: {factorial(sample_number)}")





