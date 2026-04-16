def factorial(n):
    """
    Calculate the factorial of a number.
    
    Args:
        n (int): A non-negative integer
        
    Returns:
        int: The factorial of n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result


def factorial_recursive(n):
    """
    Calculate the factorial of a number using recursion.
    
    Args:
        n (int): A non-negative integer
        
    Returns:
        int: The factorial of n
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n == 0 or n == 1:
        return 1
    
    return n * factorial_recursive(n - 1)


if __name__ == "__main__":
    # Demo usage
    print("Factorial Demo")
    print("-" * 40)
    
    # Test iterative version
    for num in range(6):
        result = factorial(num)
        print(f"Factorial of {num} (iterative): {result}")
    
    print()
    
    # Test recursive version
    for num in range(6):
        result = factorial_recursive(num)
        print(f"Factorial of {num} (recursive): {result}")
    
    print()
    
    # Test with larger number
    large_num = 10
    print(f"Factorial of {large_num}: {factorial(large_num)}")
