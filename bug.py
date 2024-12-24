def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Invalid input type")
        return None

# The uncommon error is the lack of handling for other potential exceptions.
# The function only handles ZeroDivisionError and TypeError. Other errors might occur
# due to other input type, like string, or invalid operations, leading to unexpected behavior.