from typing import List

def get_prompt_templates() -> List[str]:
    return [
        "Create an animation of a {object} moving from {start} to {end}.",
        "Show a {shape} that changes color from {color1} to {color2}.",
        "Illustrate the concept of {concept} using a {visual} representation.",
        "Animate a {character} performing a {action} in a {setting}.",
        "Demonstrate the {mathematical_operation} of {number1} and {number2} visually."
    ]