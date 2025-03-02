import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

# Load environment variables
load_dotenv()

def generate_code(user_description):
    """Generate Manim code from user description."""
    print(f"[LOG] Generating code for: {user_description}")

    # Set up Groq LLM
    llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0.7)

    # Create a prompt template
    template = """
    You are an expert in creating animations using the Manim library in Python.

    Generate ONLY valid Python code that uses Manim to create the following animation:

    {description}

    IMPORTANT: Your response must contain ONLY executable Python code without any introduction,
    explanation, markdown formatting, or comments outside the code. Start directly with
    the import statements.
    """

    prompt = ChatPromptTemplate.from_messages([("system", template)])

    # Create a chain and run it
    chain = LLMChain(llm=llm, prompt=prompt)

    # Generate the code
    response = chain.run(description=user_description)

    # Clean up the response to ensure it only contains code
    # Remove any markdown code block formatting
    cleaned_code = response.replace("```python", "").replace("```", "").strip()

    # If the response still starts with explanation text, try to extract just the code
    if not cleaned_code.startswith("from") and not cleaned_code.startswith("import"):
        # Try to find where the code actually starts
        import_index = cleaned_code.find("from manim import")
        if import_index == -1:
            import_index = cleaned_code.find("import manim")

        if import_index != -1:
            cleaned_code = cleaned_code[import_index:].strip()

    return cleaned_code
