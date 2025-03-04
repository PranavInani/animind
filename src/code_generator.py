import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from src.utils import clean_code_response, log_message

# Load environment variables
load_dotenv()

def generate_code(user_description):
    """Generate Manim code from user description."""
    log_message(f"Generating code for: {user_description}")

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

    try:
        # Generate the code
        response = chain.run(description=user_description)
        
        # Clean up the response
        return clean_code_response(response)
    except Exception as e:
        log_message(f"Error generating code: {str(e)}")
        raise

def modify_animation_code(existing_code, user_feedback):
    """Modify existing Manim code based on user feedback."""
    log_message(f"Modifying animation based on feedback: {user_feedback}")
    
    # Set up Groq LLM
    llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0.7)
    
    # Create a prompt template for modification
    template = """
    You are an expert in creating animations using the Manim library in Python.
    
    You are given EXISTING Manim code and a request for modifications. 
    Update the code to implement the requested changes while preserving the core animation.
    
    EXISTING CODE:
    ```python
    {existing_code}
    ```
    
    REQUESTED CHANGES:
    {user_feedback}
    
    IMPORTANT: Your response must contain ONLY executable Python code without any introduction,
    explanation, markdown formatting, or comments outside the code. Start directly with
    the import statements. Keep ALL necessary import statements even if unchanged.
    """
    
    prompt = ChatPromptTemplate.from_messages([("system", template)])
    
    try:
        # Create a chain and run it
        chain = LLMChain(llm=llm, prompt=prompt)
        
        # Generate the modified code
        response = chain.run(existing_code=existing_code, user_feedback=user_feedback)
        
        # Clean up the response
        return clean_code_response(response)
    except Exception as e:
        log_message(f"Error modifying code: {str(e)}")
        raise
