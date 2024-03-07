for i in range(1, 101): #Question one
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

def fibonacci(n): #Question two
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

print(fibonacci(100))

def is_power_of_two(num): #Question three
    return num > 0 and (num & (num - 1)) == 0

user_input = int(input("Enter an integer: "))
result = is_power_of_two(user_input)
print(f"{user_input} is a power of two: {result}")

def capitalize_words(sentence): #Question FOUR
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

user_input = input("Enter a string: ")
result = capitalize_words(user_input)
print(f"Capitalized string: {result}")

def reverse_integer(num): #Question five
    sign = -1 if num < 0 else 1
    reversed_num = int(str(abs(num))[::-1]) * sign
    return reversed_num

user_input = int(input("Enter an integer: "))
result = reverse_integer(user_input)
print(f"Reversed integer: {result}")


def count_vowels(sentence): #Question six
    vowels = "aeiouAEIOU"
    return sum(1 for char in sentence if char in vowels)

user_input = input("Enter a sentence: ")
result = count_vowels(user_input)
print(f"Number of vowels in the sentence: {result}")







