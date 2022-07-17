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
    "/": divide
}


def calculate():
    num1 = int(input("What's the first number?: "))
    for symbol in operation:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = int(input("What's the second number?: "))
        calculation_function = operation[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # operation_symbol = input("Pick another operation: ")
        # num3 = int(input("What's the next number?: "))
        # calculation_function = operation[operation_symbol]
        # answer = calculation_function(calculation_function(num1, num2), num3)
        # second_answer = calculation_function(first_answer, num3)
        # print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

        # if input(f"Type 'y' to continue calculating with {answer}, or type 'no' to exit.: ") == "y":
        # num1 = answer
        # else:
        # should_continue = False
        if input(f"Type 'y' to continue calculating with {answer}, or type 'no' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculate()
