x = None
try:
    for elem in x:
        print(elem)
except TypeError as error:
    print(error)

x = "abc"
try:
    x = int(x)
except ValueError as error:
    print(error)

try:
    assert 2 == 3
except AssertionError as error:
    print(error)

array = [1, 2, 3]
try:
    x = array[10]
except IndexError as error:
    print(error)
