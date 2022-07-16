def add(n1, n2):
    return n1 + n2


def subtract(m1, m2):
    return m1 - m2


def multiply(a1, a2):
    return a1 * a2


def divide(b1, b2):
    return b1 / b2


operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/":divide
}

num1 = int(input("What's the first number?: "))
for symbol in operation:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number?: "))
calculation_function = operation[operation_symbol]
answer = calculation_function(num1, num2)


print(f"{num1} {operation_symbol} {num2} = {answer}")