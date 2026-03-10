# lcm.py
# Program to find the Least Common Multiple (LCM) of two numbers

def find_lcm(a, b):
    # Find the greater number
    greater = max(a, b)

    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1


# Take input from user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

lcm = find_lcm(num1, num2)

print(f"The LCM of {num1} and {num2} is {lcm}")