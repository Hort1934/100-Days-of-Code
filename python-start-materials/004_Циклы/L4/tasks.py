"""
Два способа для 1 задачи
"""
for number in range(101):
    if number % 2 == 0:
        print(number)

counter = 0
while counter < 101:
    if counter % 2 == 0:
        print(counter)
    counter += 1

"""
2 задача
"""
word = "hello"
for char in word:
    if char == "l":
        print("s")
    else:
        print(char)

"""
# 3
"""

back_counter = 99
end_value = 0
while back_counter > end_value:
    if back_counter % 5 == 0:
        print(back_counter)
    back_counter -= 1
