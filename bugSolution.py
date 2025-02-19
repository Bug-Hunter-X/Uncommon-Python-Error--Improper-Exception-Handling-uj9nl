def function_with_improved_error_handling(a, b):
    try:
        result = a / b
        return result
    except TypeError:
        return "Error: Unsupported operand types for division"
    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception as e:
        return f"An unexpected error occurred: {type(e).__name__}: {e}"

# Example usage
print(function_with_improved_error_handling(10, 2))  # Output: 5.0
print(function_with_improved_error_handling(10, 0))  # Output: Error: Division by zero
print(function_with_improved_error_handling(10, "2")) # Output: Error: Unsupported operand types for division
print(function_with_improved_error_handling(10, [2,3])) # Output: An unexpected error occurred: TypeError: unsupported operand type(s) for /: 'int' and 'list' 