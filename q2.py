def process_list(original):
    # Create a copy
    result = original.copy()

    # Remove negative numbers
    result = [num for num in result if num >= 0]

    # Append 0
    result.append(0)

    # Sort in ascending order
    result.sort()

    # Return the modified list
    return result

original = [5, -2, 8, -1, 3]

result = process_list(original)

print("Original:", original)
print("Result:", result)
