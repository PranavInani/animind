import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration settings for the Manim Text to Animation application

# API configuration for LangChain and Groq API
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

# Path to the directory where generated Manim scripts will be stored
MANIM_SCRIPT_DIR = "generated_scripts"

# Path to the directory where output videos will be saved
OUTPUT_VIDEO_DIR = "output_videos"