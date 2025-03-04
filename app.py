import gradio as gr
import time
from src.code_generator import generate_code, modify_animation_code
from src.manim_executor import ManimExecutor
from src.utils import log_message, validate_input, ensure_absolute_path
from src.conversation_state import ConversationState

def create_app():
    # Create a new conversation state per session
    conversation_state = ConversationState(max_history=20)
    
    def create_animation(user_input):
        try:
            # Validate input
            user_input = validate_input(user_input)
            
            # Add this message to conversation history
            conversation_state.add_user_message(user_input)
            
            # Generate Manim code from user input
            log_message(f"Generating code for: {user_input}")
            manim_code = generate_code(user_input)
            
            # Execute the generated Manim code and get the output video path
            log_message("Executing Manim code")
            executor = ManimExecutor()
            output_video_path = executor.execute(manim_code)
            
            if not output_video_path:
                error_msg = "Failed to generate animation. Please check logs for details."
                # Add error message to conversation history
                conversation_state.add_assistant_message(error_msg)
                return None, error_msg, update_history()
            
            # Ensure path is normalized
            output_video_path = ensure_absolute_path(output_video_path)
                
            log_message(f"Returning video path: {output_video_path}")
            
            # Add successful response and store current animation code and video path
            success_msg = "Here's your animation! You can ask for modifications if needed."
            conversation_state.add_assistant_message(success_msg, manim_code, output_video_path)
                
            # Return both the video path and the generated code
            return output_video_path, manim_code, update_history()
        
        except ValueError as ve:
            error_msg = f"Error: {str(ve)}"
            conversation_state.add_assistant_message(error_msg)
            log_message(f"Validation error: {error_msg}")
            return None, error_msg, update_history()
        except Exception as e:
            error_msg = f"Unexpected error: {str(e)}"
            conversation_state.add_assistant_message(error_msg)
            log_message(f"Unexpected error: {error_msg}")
            return None, error_msg, update_history()
    
    def modify_animation(user_input):
        try:
            # Validate input
            user_input = validate_input(user_input)
            
            # Add user request to conversation history
            conversation_state.add_user_message(user_input)
            
            # Check if we have existing animation code
            existing_code = conversation_state.current_animation_code
            if not existing_code:
                error_msg = "No existing animation to modify. Please create an animation first."
                conversation_state.add_assistant_message(error_msg)
                return None, error_msg, update_history()
            
            # Modify the existing code based on feedback
            log_message(f"Modifying animation based on: {user_input}")
            modified_code = modify_animation_code(existing_code, user_input)
            
            # Execute the modified code
            executor = ManimExecutor()
            output_video_path = executor.execute(modified_code)
            
            if not output_video_path:
                error_msg = "Failed to generate modified animation. Please check logs for details."
                conversation_state.add_assistant_message(error_msg)
                return None, error_msg, update_history()
            
            # Ensure path is normalized
            output_video_path = ensure_absolute_path(output_video_path)
            
            # Update conversation state with new animation
            success_msg = "I've updated your animation! You can request more changes if needed."
            conversation_state.add_assistant_message(success_msg, modified_code, output_video_path)
            
            return output_video_path, modified_code, update_history()
            
        except Exception as e:
            error_msg = f"Error modifying animation: {str(e)}"
            conversation_state.add_assistant_message(error_msg)
            return None, error_msg, update_history()
    
    def process_input(user_input, is_modification=False):
        """Process user input and determine whether to create or modify animation"""
        if is_modification:
            return modify_animation(user_input)
        else:
            return create_animation(user_input)
    
    def update_history():
        history = conversation_state.get_history()
        formatted_history = "**Conversation History:**\n\n"
        
        for message in history:
            role = message["role"]
            content = message["content"]
            
            if role == "user":
                formatted_history += f"👤 **You**: {content}\n\n"
            else:
                formatted_history += f"🤖 **AniMind**: {content}\n\n"
        
        return formatted_history
    
    def clear_conversation():
        conversation_state.clear_history()
        return update_history()
    
    # Set up the Gradio interface
    with gr.Blocks(title="AniMind - AI-Powered Math Animations") as iface:
        gr.Markdown("# ✨ AniMind")
        gr.Markdown("### Transform your ideas into beautiful mathematical animations")
        
        with gr.Row():
            with gr.Column(scale=1):
                user_input = gr.Textbox(
                    placeholder="Describe an animation or request changes...",
                    label="Your request",
                    lines=3
                )
                
                with gr.Row():
                    create_btn = gr.Button("Create New Animation", variant="primary")
                    modify_btn = gr.Button("Modify Current Animation")
                
                clear_btn = gr.Button("Clear Conversation History")
                
                # Display conversation history
                history_display = gr.Markdown("**Conversation History:**")
                
            with gr.Column(scale=2):
                with gr.Row():
                    status_indicator = gr.Markdown("Ready")
                
                output_video = gr.Video(label="Generated Animation")
                output_code = gr.Code(language="python", label="Generated Manim Code", max_lines=20, elem_id="code-output")
        
        # Connect the buttons to their respective functions
        create_btn.click(
            fn=lambda x: process_input(x, False),
            inputs=user_input,
            outputs=[output_video, output_code, history_display],
            show_progress="minimal"
        )
        
        modify_btn.click(
            fn=lambda x: process_input(x, True),
            inputs=user_input,
            outputs=[output_video, output_code, history_display],
            show_progress="minimal"
        )
        
        # Clear conversation history
        clear_btn.click(
            fn=clear_conversation,
            inputs=None,
            outputs=history_display
        )
        
        # Add examples
        gr.Examples(
            examples=[
                ["Create a bouncing ball animation"],
                ["Show a rotating cube"],
                ["Animate a sine wave"],
                ["Make the cube rotate faster"],
                ["Change the ball color to blue"],
                ["Add a title 'Physics in Motion'"]
            ],
            inputs=user_input
        )
    
    return iface

if __name__ == "__main__":
    app = create_app()
    app.launch()