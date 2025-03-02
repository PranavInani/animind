import gradio as gr
from src.code_generator import generate_code
from src.manim_executor import ManimExecutor
from src.utils import log_message, validate_input

def create_animation(user_input):
    try:
        # Validate input
        user_input = validate_input(user_input)
        
        # Generate Manim code from user input
        log_message(f"Generating code for: {user_input}")
        manim_code = generate_code(user_input)
        
        # Execute the generated Manim code and get the output video path
        log_message("Executing Manim code")
        executor = ManimExecutor()
        output_video_path = executor.execute(manim_code)
        
        if not output_video_path:
            return None, "Failed to generate animation. Please check logs for details."
        
        # Make sure the path is absolute for Gradio
        import os
        if not os.path.isabs(output_video_path):
            output_video_path = os.path.abspath(output_video_path)
            
        log_message(f"Returning video path: {output_video_path}")
            
        # Return both the video path and the generated code
        return output_video_path, manim_code
    
    except ValueError as ve:
        log_message(f"Validation error: {str(ve)}")
        return None, f"Error: {str(ve)}"
    except Exception as e:
        log_message(f"Error creating animation: {str(e)}")
        return None, f"An unexpected error occurred: {str(e)}"

# Set up the Gradio interface
with gr.Blocks(title="Text to Manim Animation") as iface:
    gr.Markdown("# Text to Manim Animation")
    gr.Markdown("Enter a description of the animation you want to create, and see it generated in real-time!")
    
    with gr.Row():
        with gr.Column(scale=1):
            input_text = gr.Textbox(
                label="Describe your animation", 
                placeholder="Example: Create an animation of a circle transforming into a square",
                lines=5
            )
            generate_btn = gr.Button("Generate Animation")
        
        with gr.Column(scale=2):
            output_video = gr.Video(label="Generated Animation")
            output_code = gr.Code(language="python", label="Generated Manim Code")
    
    generate_btn.click(
        fn=create_animation,
        inputs=input_text,
        outputs=[output_video, output_code]
    )
    
    # Add examples
    gr.Examples(
        examples=[
            ["Create a bouncing ball animation"],
            ["Show a rotating cube"],
            ["Animate a sine wave"],
            ["Display a growing tree"],
            ["Create a star twinkling"]
        ],
        inputs=input_text
    )

# Launch the application
if __name__ == "__main__":
    iface.launch()