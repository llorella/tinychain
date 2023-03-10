from typing import Optional, List
from api import get_completion

class Message:
    def __init__(self, role: str, content: str, prev=None) -> None:
        self.role = role
        self.content = content
        self.prev = prev
        
    def prompt(self, model: str) -> 'Message':
        completion = get_completion(model, self.expand())
        completion_message = Message('assistant', completion, self)
        return completion_message
        
    def expand(self) -> list[dict]:
        base =  [ self.format() ]
        if self.prev == None: 
            return base
        else: 
            return (self.prev.expand() + base)
   
    def format(self) -> dict: 
        message_dict = { 'role' : self.role, 'content' : self.content }
        return message_dict
    
    def __str__(self) -> str:
        return "role: " + self.role + ", content: " + self.content