
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
    assert find_largest([10, 5, 20, 3]) == 20
    assert find_largest([-10, -5, -20, -3]) == -3
    assert find_largest([5]) == 5

    print("All debugging tests passed!")
