import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration settings for the Manim Text to Animation application

# API configuration for LangChain and Groq API
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY", "")
GROQ_API_URL = "https://api.groq.com/v1"

# Path to the directory where generated Manim scripts will be stored
MANIM_SCRIPT_DIR = "generated_scripts"

# Path to the directory where output videos will be saved
OUTPUT_VIDEO_DIR = "output_videos"

# Default prompt template for LangChain
DEFAULT_PROMPT_TEMPLATE = "Create a Manim animation for the following description: {description}"

# Video rendering settings
VIDEO_RENDER_WIDTH = 1920
VIDEO_RENDER_HEIGHT = 1080
VIDEO_RENDER_FPS = 30

# Logging configuration
LOGGING_LEVEL = "INFO"  # Options: DEBUG, INFO, WARNING, ERROR, CRITICAL

# Other constants
SUPPORTED_ANIMATION_TYPES = ["Circle", "Square", "Text", "Line"]  # Extendable list of supported animation types