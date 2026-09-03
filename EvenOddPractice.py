numbers = [10, 20, 30, 40, 50,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print("\nNumbers:", numbers)


max_number=numbers[0]
min_number=numbers[0]
total_number=0

for number in numbers:
    if number>max_number:
        max_number=number
print(f'Max Number: {max_number}')

for number in numbers:
    if number<min_number:
        min_number=number
print(f'Min number: {min_number}')

for number in numbers:
    total_number+=number

print(f'Sum of total number: {total_number}')

even_number=[]
for number in numbers:
    if number%2==0:
        # even_number.append(number)
        even_number+=[number]

print(f'Even number: {even_number}')


odd_number=[]

for number in numbers:
    if number%2!=0:
        # odd_number=[number]
        odd_number+=[number]
print(f'Odd number: {odd_number}')



#  "statusLine": {
#      "type": "command",
#     "command": "node \"C:\\Users\\SEBPO\\.claude\\settings.json\""
#    },
#  "model": "opus[1m]"
