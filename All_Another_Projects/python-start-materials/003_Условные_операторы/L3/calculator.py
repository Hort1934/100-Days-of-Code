first_value = 5
second_value = 10
operator = "+"
if operator == "+":
    print(first_value + second_value)
elif operator == "-":
    print(first_value - second_value)
elif operator == "/":
    if second_value == 0:
        print("Division on zero, impossible")
    else:
        print(first_value / second_value)
elif operator == "*":
    print(first_value * second_value)
else:
    print("Choose right operator from given 4: + - * /")
