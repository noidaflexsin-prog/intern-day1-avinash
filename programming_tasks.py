
from collections import Counter


def second_largest(numbers):
    unique_numbers = sorted(set(numbers), reverse=True)
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]


def is_palindrome(text):
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]


def character_frequency(text):
    return dict(Counter(text))


def filter_adults(users):
    return [user for user in users if user["age"] >= 18]


if __name__ == "__main__":
    print("Second largest:", second_largest([10, 5, 8, 10, 3]))
    print("Palindrome:", is_palindrome("Madam"))
    print("Character frequency:", character_frequency("hello"))

    users = [
        {"name": "Amit", "age": 17},
        {"name": "Priya", "age": 22},
        {"name": "Rahul", "age": 18},
    ]
    print("Adults:", filter_adults(users))
