class ManimExecutor:
    def __init__(self, script_dir=None, output_dir=None):
        from config import MANIM_SCRIPT_DIR, OUTPUT_VIDEO_DIR
        import os
        
        self.script_dir = script_dir or MANIM_SCRIPT_DIR
        self.output_dir = output_dir or OUTPUT_VIDEO_DIR
        
        # Create directories if they don't exist
        os.makedirs(self.script_dir, exist_ok=True)
        os.makedirs(self.output_dir, exist_ok=True)
    
    def execute(self, manim_code):
        import os
        from src.utils import write_file
        import uuid
        
        # Generate unique filenames
        script_id = str(uuid.uuid4())
        script_path = os.path.join(self.script_dir, f"{script_id}.py")
        output_path = os.path.join(self.output_dir, script_id)
        
        # Write code to file
        write_file(script_path, manim_code)
        
        # Execute the script
        self.execute_script(script_path, output_path)
        
        # Return the output video path
        return self._find_output_video(output_path)
        
    def execute_script(self, script_path, output_path):
        import subprocess
        import os
        import re
        
        # Create output directory if it doesn't exist
        os.makedirs(output_path, exist_ok=True)
        
        try:
            # First, let's find the Scene class name from the Python file
            with open(script_path, 'r') as f:
                content = f.read()
                # Look for class declarations that inherit from Scene
                scene_classes = re.findall(r'class\s+(\w+)\s*\(\s*Scene\s*\)', content)
                
            if scene_classes:
                # Use the first scene class found
                scene_class = scene_classes[0]
                print(f"Found Scene class: {scene_class}")
                
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
                print("No Scene class found, trying to render the whole file")
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
            print(f"Manim execution completed successfully")
            print(f"Manim stdout: {result.stdout}")
            return True
            
        except subprocess.CalledProcessError as e:
            print(f"Error executing Manim: {e}")
            print(f"Error output: {e.stderr}")
            return False
        except Exception as e:
            print(f"Unexpected error during Manim execution: {e}")
            return False

    def _find_output_video(self, output_dir):
        """Find the generated video file in the output directory."""
        import os
        import glob
        
        print(f"Looking for video in: {output_dir}")
        
        # Check common Manim output directory patterns
        possible_paths = [
            # Direct in output directory
            os.path.join(output_dir, "*.mp4"),
            # In videos subdirectory
            os.path.join(output_dir, "videos", "*.mp4"),
            # In videos/[quality] subdirectory
            os.path.join(output_dir, "videos", "*", "*.mp4"),
            # Match the exact nested pattern we're seeing
            os.path.join(output_dir, "videos", os.path.basename(output_dir), "720p30", "*.mp4"),
            # Broader search with any resolution
            os.path.join(output_dir, "videos", os.path.basename(output_dir), "*", "*.mp4")
        ]
        
        # Try each pattern
        for pattern in possible_paths:
            videos = glob.glob(pattern)
            if videos:
                video_path = videos[0]  # Take the first match
                print(f"Found video: {video_path}")
                return video_path
        
        # If we get here, no video was found
        print(f"No video found in {output_dir}")
        
        # List some directories to help debug
        print("Checking directory contents:")
        if os.path.exists(os.path.join(output_dir, "videos")):
            print(f"Contents of {os.path.join(output_dir, 'videos')}:")
            print(os.listdir(os.path.join(output_dir, "videos")))
            
            nested_dir = os.path.join(output_dir, "videos", os.path.basename(output_dir))
            if os.path.exists(nested_dir):
                print(f"Contents of {nested_dir}:")
                print(os.listdir(nested_dir))
        
        return None