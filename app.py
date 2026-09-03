# temperature = int(input('Enter the temperature: '))
# print("Temperature is:", temperature)
# if temperature > 30:
#     print("It's hot")
#     print("Stay hydrated")
# elif temperature < 20:
#     print("It's cold")
#     print("Wear a jacket")
# elif temperature == 30:
#     print("It's a warm day")
#     print("Perfect for a walk")
# print("Have a great day!")

# age=int(input("Enter your age:"))
# if age < 18:
#     messages = "You are a minor."
# elif 18 <= age < 65:
#     messages = "You are an adult."
# else:
#     messages = "You are a senior citizen."
# print("Thank you."+messages)

print("\nThis is a simple for loop for numbers\n")
for number in range(11):
    print("The number is:", number)

print("\nThis is a simple for loop for letters\n")

for letter in "Python":
    print("The letter is:", letter)

print("\nThis is a simple for loop for numbers with step\n")

for number in range(3):
    print("attempt :", number+1, (number+1)*".")

print("\nThis is a simple for loop for numbers with step\n")

for number in range(1,4):
    print("attempt2 :", number, number*".")

print("\nThis is a simple for loop for numbers with step\n")

for number in range(1,10,2):
    print("attempt3 :", number, number*".")


print("\nThis is a simple while loop for numbers\n")

number = 1
while number <= 10:
    print("The number is:", number)
    number += 1


