# Calculator.
def cal():
    print("This is a Simple Calculator.")
    print(
        "You choose a number, then a sign and then the last number. The signs can be plus, minus, times and division.")

    num1 = int(input("Number 1 --> "))
    sign = input("Sign --> ")
    num2 = int(input("Last number --> "))

    if sign == "+" or sign == "-" or sign == "*" or sign == "/":
        print("You want to calculate %s%s%s." % (num1, sign, num2))

    if sign == "+":
        result = int(num1) + int(num2)
        print("The result is %s." % result)

    elif sign == "-":
        result = int(num1) - int(num2)
        print("The result is %s." % result)

    elif sign == "x" or sign == "*":
        result = num1 * num2
        print("The result is %s." % result)

    elif sign == "/":
        result = num1 / num2
        print("The result is %s." % result)

    elif sign == "xx" or sign == "**":
        result = num1 ** num2
        print("the result is %s." % result)

    else:
        print("Something went wrong.")


# Square root function.
def sqr():
    from math import sqrt
    answer = input("Enter a number you want to find the square root of: ")
    return sqr(answer)

    def cals():
        result = sqrt(int(answer))
        print("The result is %s." % (result))

    print("We will now find the square root of you number.")

    if len(answer) > 0 and answer.isnumeric:
        cals()

    elif answer.isalpha:
        print("You can only use numbers.")

    elif len(answer) == 0:
        print("You must write something.")

    else:
        print("Something went wrong.")

# if function.
def t_if():
    if choice == "scal":
        return cal()

    elif choice == "sr":
        return sqr()
    else:
        print("Something went wrong. Make sure you spelled correctly.")



print("Enter what type of calculations you want.")
print("You can choose 'sr for Square root'and 'scal for a Simple Calculator', .")

choice = input("Enter here: ").lower()

if len(choice) > 0:
    t_if()

else:
    print("Something went wrong. Make sure you spelled it correct.")


