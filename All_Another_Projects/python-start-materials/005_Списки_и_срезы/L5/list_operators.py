a = [1, 2, 3, 4]  # list a was created
a.append(5)  # append 5 to list a
print(a)
b = []  # list b
b.append(3)  # append 3 to empty list b
print(b)
b.extend(a)  # [3] + [1, 2, 3, 4]
print(b)
b += a
print(b)
b.pop(1)
print(b)
b.sort()
print(b)
b.reverse()
print(b)
c = []
for elem in b:
    if elem < 3:
        c.append(elem)
print(c)
