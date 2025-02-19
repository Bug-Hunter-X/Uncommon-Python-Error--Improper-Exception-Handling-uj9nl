def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except TypeError:
        return "Error: Cannot divide a string by a number"
except ZeroDivisionError:
    return "Error: Cannot divide by zero"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Example usage
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(10, 0))  # Output: Error: Cannot divide by zero
print(function_with_uncommon_error(10, "2")) # Output: Error: Cannot divide a string by a number
print(function_with_uncommon_error(10, [2,3])) # Output: An unexpected error occurred: unsupported operand type(s) for /: 'int' and 'list'