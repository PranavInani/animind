import os
import platform
import re

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def log_message(message):
    print(f"[LOG] {message}")

def validate_input(user_input):
    if not user_input.strip():
        raise ValueError("Input cannot be empty.")
    
    # Check for potentially problematic inputs
    max_length = 1000
    if len(user_input) > max_length:
        raise ValueError(f"Input is too long. Maximum {max_length} characters allowed.")
    
    # Additional validation could be added here
    return user_input.strip()

def clean_code_response(response):
    """Clean up code response from LLM to extract only executable code."""
    # Remove any markdown code block formatting
    cleaned_code = response.replace("```python", "").replace("```", "").strip()
    
    # If the response still starts with explanation text, try to extract just the code
    if not cleaned_code.startswith("from") and not cleaned_code.startswith("import"):
        # Try to find where the code actually starts
        import_index = cleaned_code.find("from manim import")
        if import_index == -1:
            import_index = cleaned_code.find("import manim")
        
        if import_index != -1:
            cleaned_code = cleaned_code[import_index:].trip()
    
    return cleaned_code

def ensure_absolute_path(path):
    """Ensure a path is absolute, normalizing for the current platform."""
    if not os.path.isabs(path):
        path = os.path.abspath(path)
    
    # Normalize path separators for the current platform
    return os.path.normpath(path)