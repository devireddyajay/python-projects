a=input("enter the input:")
b=" "
for i in a:
    b=i+b
print(b)

user_string = input("Please enter a string.")
reversed = ""

for item in range(len(user_string) - 1, -1, -1):
    reversed += user_string[item]

print(reversed)