counter = 0
if counter < 10:
    counter += 1
else:
    pass
print(counter)

animal = "cat"
if animal == "cat":
    print("Meow")
elif animal == "dog":
    print("Wof")
else:
    print("I don't know this animal")

result = 5 if 4 > 3 else 0  # ternary operator; equals to 5
print(result)
result2 = 5 if 3 > 4 else 0  # ternary operator; equals to 0
print(result2)
