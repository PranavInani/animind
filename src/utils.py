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
    return user_input.strip()