# Membership Operator (in)
fruits = ['apple', 'banana', 'orange', 'grape']
search_fruit = 'banana'

if search_fruit in fruits:
    print(f"{search_fruit} is present in the list.")
else:
    print(f"{search_fruit} is not present in the list.")

# Membership Operator (not in)
if 'watermelon' not in fruits:
    print("Watermelon is not present in the list.")
else:
    print("Watermelon is present in the list.")
# Identity Operator (is)
x = [1, 2, 3]
y = [1, 2, 3]

if x is y:
    print("x and y refer to the same object.")
else:
    print("x and y do not refer to the same object.")

# Identity Operator (is not)
if x is not y:
    print("x and y do not refer to the same object.")
else:
    print("x and y refer to the same object.")
bk/u87980o8ih