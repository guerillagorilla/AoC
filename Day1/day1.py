
#!/usr/bin/python3

'''
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
'''

with open('/home/gorilla/test/day1.txt', 'r') as file:
    data = file.read()
    lines = data.split('\n')

    total = 0
    for line in lines:
        # create a list of numbers in the line
        numbers = [i for i in line if i.isdigit()]
        # if numbers list is not empty, combine the numbers of each row then add the combined number to the total
        if numbers:
            combined_number = int(numbers[0] + numbers[-1])
            total += combined_number

    print(total)
