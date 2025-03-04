class ConversationState:
    def __init__(self, max_history=20):
        self.conversation_history = []
        self.current_animation_code = None
        self.current_video_path = None
        self.max_history = max_history
        
    def add_user_message(self, message):
        self._add_message({"role": "user", "content": message})
        
    def add_assistant_message(self, message, animation_code=None, video_path=None):
        self._add_message({"role": "assistant", "content": message})
        if animation_code:
            self.current_animation_code = animation_code
        if video_path:
            self.current_video_path = video_path
    
    def _add_message(self, message):
        """Add a message to history, maintaining the maximum history size."""
        self.conversation_history.append(message)
        # If we exceed the maximum history size, remove oldest messages
        if len(self.conversation_history) > self.max_history:
            # Remove oldest messages (keep the most recent max_history messages)
            self.conversation_history = self.conversation_history[-self.max_history:]
            
    def get_history(self):
        return self.conversation_history
    
    def clear_history(self):
        """Clear conversation history but maintain current animation state."""
        self.conversation_history = []