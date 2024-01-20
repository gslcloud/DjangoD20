from typing import Union

def refactor_code(original_code: str) -> str:
    """
    Refactors the code by removing empty lines and trailing whitespace.
    
    Args:
        original_code (str): The original code to be refactored.
    
    Returns:
        str: The refactored code.
    
    Raises:
        ValueError: If the original_code is not a string or is empty or contains only whitespace.
    """
    if not isinstance(original_code, str) or not original_code.strip():
        raise ValueError("Invalid input code.")

    lines = original_code.splitlines()
    refactored_lines = [line.strip() for line in lines if line.strip()]
    refactored_code = "\n".join(refactored_lines)

    return refactored_code