# 1. Sum of Two Numbers 
def sum_of_two():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"Sum: {a + b}")


# 2. Odd or Even Checker 
def odd_or_even():
    n = int(input("Enter a number: "))
    print(f"{n} is {'Even' if n % 2 == 0 else 'Odd'}")


# 3. Factorial Calculation 
def factorial():
    n = int(input("Enter a non-negative integer: "))
    if n < 0:
        print("Factorial is not defined for negative numbers.")
        return
    result = 1
    for i in range(2, n + 1):
        result *= i
    print(f"{n}! = {result}")


# 4. Fibonacci Sequence 
def fibonacci():
    n = int(input("How many Fibonacci numbers? "))
    if n <= 0:
        print("Please enter a positive integer.")
        return
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    print("Fibonacci sequence:", sequence)


# 5. String Reverse 
def string_reverse():
    s = input("Enter a string to reverse: ")
    print(f"Reversed: {s[::-1]}")


# 6. Palindrome Check 
def palindrome_check():
    s = input("Enter a word or phrase: ").replace(" ", "").lower()
    if s == s[::-1]:
        print(f'"{s}" is a Palindrome')
    else:
        print(f'"{s}" is NOT a Palindrome')


# 7. Leap Year Check 
def leap_year_check():
    year = int(input("Enter a year: "))
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    print(f"{year} is {'a Leap Year' if is_leap else 'NOT a Leap Year'}")


# 8. Armstrong Number 
def armstrong_number():
    num = int(input("Enter a number: "))
    order = len(str(num))
    sum_val = sum(int(digit) ** order for digit in str(num))
    if num == sum_val:
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is NOT an Armstrong number")


# Main Menu
def main():
    menu = {
        "1": ("Sum of Two Numbers",   sum_of_two),
        "2": ("Odd or Even Checker",  odd_or_even),
        "3": ("Factorial Calculation",factorial),
        "4": ("Fibonacci Sequence",   fibonacci),
        "5": ("String Reverse",       string_reverse),
        "6": ("Palindrome Check",     palindrome_check),
        "7": ("Leap Year Check",      leap_year_check),
        "8": ("Armstrong Number",     armstrong_number),
    }

    while True:
        print("Internship Task 1 Challenges: \n")
        for key, (name, _) in menu.items():
            print(f"  {key}. {name}")
        print("  0. Exit")

        choice = input("\nSelect a challenge (0-8): ").strip()
        if choice == "0":
            break
        elif choice in menu:
            print(f"\n── {menu[choice][0]} ──")
            menu[choice][1]()
        else:
            print("Please enter a number from 0 to 8.\n")


if __name__ == "__main__":
    main()