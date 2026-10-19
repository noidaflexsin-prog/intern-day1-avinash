
def find_largest(numbers):
    """Return the largest number from a list."""
    if not numbers:
        raise ValueError("The list cannot be empty")

    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest


# Tests
if __name__ == "__main__":
    print(find_largest([3, 7, 2, 9, 5]))  # Expected: 9
    print(find_largest([-8, -3, -10]))    # Expected: -3
    print(find_largest([4]))              # Expected: 4
