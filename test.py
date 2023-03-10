from main import run_conversation

model = "gpt-3.5-turbo"
description = "You are an assistant. Help the user with programming questions."
prompts = [
    "I'm learning about typescript",
    "What is typescript good for",
    "What is it not good for",
    ""
]

run_conversation(model, description, prompts)

#the description is system defined and the prompts are user defined
#well related data 
