from ast import Assert
from typing import List
from message import Message, get_completion
import random

def run_conversation(model: str, project_description: str, prompts: List[str]) -> None:
    root_message = Message('system', project_description)
    
    current_message = root_message
    while True:
        print(f"{current_message.role}: {current_message.content}")

        user_input = input('(PROMPT) $ ').strip() 
        user_content = user_input or random.choice(prompts)
        
        user_message = Message('user', user_content, current_message)
        print(f"{user_message.role}: {user_message.content}")
        
        current_message = user_message.prompt(model)

            
            
        #current message is content feedback. Therefore, user can send in system mode with instructions,
        #or, user can send in user mode with prompts
        
        