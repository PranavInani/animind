import os
import re
import uuid
import subprocess
import glob
from src.utils import write_file, log_message, ensure_absolute_path

class ManimExecutor:
    def __init__(self, script_dir=None, output_dir=None):
        from config import MANIM_SCRIPT_DIR, OUTPUT_VIDEO_DIR
        
        self.script_dir = script_dir or MANIM_SCRIPT_DIR
        self.output_dir = output_dir or OUTPUT_VIDEO_DIR
        
        # Create directories if they don't exist
        os.makedirs(self.script_dir, exist_ok=True)
        os.makedirs(self.output_dir, exist_ok=True)
    
    def execute(self, manim_code):
        # Generate unique filenames
        script_id = str(uuid.uuid4())
        script_path = os.path.join(self.script_dir, f"{script_id}.py")
        output_path = os.path.join(self.output_dir, script_id)
        
        # Write code to file
        write_file(script_path, manim_code)
        
        # Execute the script
        self.execute_script(script_path, output_path)
        
        # Return the output video path
        video_path = self._find_output_video(output_path)
        if video_path:
            return ensure_absolute_path(video_path)
        return None
        
    def execute_script(self, script_path, output_path):
        # Create output directory if it doesn't exist
        os.makedirs(output_path, exist_ok=True)
        
        try:
            # First, let's find the Scene class name from the Python file
            with open(script_path, 'r') as f:
                content = f.read()
                # Look for class declarations that inherit from Scene or any Scene subclass
                scene_pattern = r'class\s+(\w+)\s*\(\s*(\w*Scene)\s*\)'
                matches = re.findall(scene_pattern, content)
                scene_classes = [match[0] for match in matches]  # Extract class names
                
            if scene_classes:
                # Use the first scene class found
                scene_class = scene_classes[0]
                log_message(f"Found Scene class: {scene_class}")
                
                # Construct the manim command with explicit scene class
                cmd = [
                    "manim",
                    script_path,
                    f"{scene_class}",  # Specify which scene to render
                    "-qm",  # -q (quality medium), -m (media will be placed in specified directory)
                    "--media_dir", output_path
                ]
            else:
                # No scene class found, try rendering the whole file
                log_message("No Scene class found, trying to render the whole file")
                cmd = [
                    "manim",
                    script_path,
                    "-qm",  # -q (quality medium), -m (media will be placed in specified directory)
                    "--media_dir", output_path
                ]
            
            # Execute the command
            result = subprocess.run(
                cmd,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Log the output for debugging
            log_message("Manim execution completed successfully")
            log_message(f"Manim stdout: {result.stdout}")
            return True
            
        except subprocess.CalledProcessError as e:
            log_message(f"Error executing Manim: {e}")
            log_message(f"Error output: {e.stderr}")
            return False
        except Exception as e:
            log_message(f"Unexpected error during Manim execution: {e}")
            return False

    def _find_output_video(self, output_dir):
        """Find the generated video file in the output directory."""
        # With the -qm flag and specified media_dir, Manim creates this standard path
        expected_path = os.path.join(output_dir, "videos", 
                                    os.path.basename(output_dir),
                                    "720p30", 
                                    f"{os.path.basename(output_dir)}.mp4")
        
        if os.path.exists(expected_path):
            log_message(f"Found video: {expected_path}")
            return expected_path
        else:
            log_message(f"Expected video not found at: {expected_path}")
            # Fall back to searching if needed
            return self._find_video_fallback(output_dir)
    
    def _find_video_fallback(self, output_dir):
        """Fallback method to search for the video if not found at expected location."""
        log_message(f"Searching for video in: {output_dir}")
        
        patterns = [
            os.path.join(output_dir, "videos", os.path.basename(output_dir), "*", "*.mp4"),
            os.path.join(output_dir, "videos", "*", "*.mp4"),
            os.path.join(output_dir, "*.mp4")
        ]
        
        for pattern in patterns:
            videos = glob.glob(pattern)
            if videos:
                return videos[0]
        
        log_message(f"No video found in {output_dir}")
        return None