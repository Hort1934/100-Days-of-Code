global_value = [1, 2, 3, 4]


def make_something(function):
    for element in global_value:
        print(function(element))


make_something(lambda x: x * 10)
