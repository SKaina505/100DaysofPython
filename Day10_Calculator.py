import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {"+":add,
              "-":subtract,
              "*":multiply,
              "/":divide,
              }
def calculator():
    print(art.logo)
    should_accumulate = True
    n1 = float(input("What is the first number"))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        method = input("Pick an operation ")
        n2 = float(input("What is the next number"))

        result = operations[method](n1, n2)
        print(f"{n1} {method} {n2} = {result}")

        progress = input(f"Type 'y' if you want to continue calculating with {result}, or 'n' to start a new calculation: ")

        if progress == "y":
            n1 = result
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()
