"""Simple examples for Labs 11–12: arithmetic and logical problem-solving."""

def sum_two_numbers(a, b):
    return a + b

def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

def largest_of_two(a, b):
    if a > b:
        return a
    if b > a:
        return b
    return "Both are equal"

if __name__ == "__main__":
    print("Sum of 8 and 5:", sum_two_numbers(8, 5))
    print("7 is:", even_or_odd(7))
    print("Largest of 12 and 9:", largest_of_two(12, 9))
    print("Compare 4 and 4:", largest_of_two(4, 4))
