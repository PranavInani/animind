# Animind - Manime Text to Animation

This project is a web-based application that allows users to describe animations in natural language, which are then converted into executable Manim Python code. The application leverages LangChain and the Groq API for natural language processing and code generation.

## Demo

Watch our demo to see AniMind in action:

![Demo](https://github.com/PranavInani/animind/blob/main/demo.gif)

## Project Structure

```
manim-text-to-animation
├── app.py                  # Main entry point for the application
├── src                     # Source code directory
│   ├── code_generator.py   # Generates Manim code from user input
│   ├── manim_executor.py   # Executes Manim scripts and handles output
│   ├── prompt_templates.py  # Defines prompt templates for user input
│   └── utils.py            # Utility functions for common tasks
├── assets                  # Directory for assets
│   └── examples.json       # Example prompts and expected outputs
├── .env                    # Environment variables for configuration
├── requirements.txt        # Python dependencies for the project
├── sample_animations       # Directory for sample animations
│   └── default.py          # Sample Manim animation script
├── config.py               # Configuration settings for the application
└── README.md               # Documentation for the project
```

## Installation

To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd manim-text-to-animation
pip install -r requirements.txt
```

## Usage

1. Ensure that you have all the necessary dependencies installed.
2. Set up your environment variables in the `.env` file.
3. Run the application:

```bash
python app.py
```

4. Open your web browser and navigate to the provided local URL to access the application.

## Features

- User-friendly interface for inputting animation descriptions.
- Automatic generation of Manim code based on user input.
- Execution of generated Manim scripts to produce animations.
- Display of resulting animations directly in the web interface.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.
