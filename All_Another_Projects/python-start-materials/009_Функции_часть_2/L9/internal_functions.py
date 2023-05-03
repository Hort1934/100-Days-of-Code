def external():
    x = 10  # local variable in 'external' function

    def internal(value):  # local function in 'external' function
        return value

    y = 20  # local variable in 'external' function
    return y + internal(x)


print(external())  # correct
print(x)  # error of calling local variable
print(y)  # error of calling local variable
print(internal())  # error of calling local function
