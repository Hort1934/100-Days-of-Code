def check(sequence):
    if len(set(sequence)) == len(sequence):
        return True
    return False


def check_sequence_unique(array):
    try:
        return check(array)
    except TypeError as type_error:
        print(type_error, 'use only strings, lists or sets')


s = False
u = check_sequence_unique(s)
print(u)
