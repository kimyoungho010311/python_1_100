import art

def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    if n2 == 0:
        return "Error! Division by zero is not allowed"
    return n1 / n2

operations = {
    '+' : add,
    # add()는 함수를 사용하는것이므로 ()를 제거한다.
    '-' : sub,
    '*' : mul,
    '/' : div
}
print(art.logo)
continue_cal = True
while continue_cal:
    number1 = float(input("What's the first number? : "))
    while True:
        operation = input(" +\n -\n *\n /\nPick an operation : ")
        if operation not in operations:
            print("You picked an invalid operation. Try again.")
            continue

        number2 = float(input("What's the second number? : "))
        result = operations[operation](number1, number2)
        print(f"Result : {result}")

        user_choice = input(f"Type 'y' continue calculation with {result}, or type 'n' to start a new calculation. : \n").lower()

        if user_choice == 'y':
            number1 = result
        else:
            break
    continue_cal = input("Do you want to perform a new calculation? (y/n) : ").lower()== 'y'
    print("\n" * 100)
print("Goodbye")