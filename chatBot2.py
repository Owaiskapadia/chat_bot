import json
import time
from difflib import get_close_matches
from textblob import TextBlob

# Predefined questions and answers
predefined_responses = {
    "hello": "Hi there!",
    "how are you": "I'm a chatbot, so I don't have feelings, but thanks for asking!",
    "what is your name": "I'm a simple CLI chatbot.",
    "help": "Available commands:\n - 'help': List available commands and instructions.\n - 'exit': Quit the chatbot.\nYou can ask me anything!"
}

# Load the knowledge base from a JSON file
def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

# Save the knowledge base to a JSON file
def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

# Find the best match for the user question from a list of questions
def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

# Get the answer for a given question from the knowledge base or predefined responses
def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    question_lower = question.lower()  # Normalize the question to lowercase
    # Check predefined responses first
    for key in predefined_responses.keys():
        if key in question_lower:
            return predefined_responses[key]
    # Check the knowledge base if no predefined response is found
    for q in knowledge_base["questions"]:
        if q["question"].lower() == question_lower:
            return q["answer"]
    return None

# Analyze sentiment of the user input
def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

# Simulate typing effect for the response
def type_response(response):
    for char in response:
        print(char, end='', flush=True)
        time.sleep(0.05)  # Adjust the delay as needed
    print()

# Main function for the chatbot
def chat_bot():
    knowledge_base: dict = load_knowledge_base('knowledgeBase.json')  # Load the knowledge base from file
    
    while True:
        user_input: str = input('You: ')
        
        if user_input.lower() == "exit":
            type_response("Goodbye!")  # Respond and exit if the user types 'exit'
            break
        
        if user_input.lower() == 'quit':
            break  # Exit if the user types 'quit'

        # Check for predefined commands like 'help'
        if user_input.lower() in predefined_responses:
            type_response(f'Bot: {predefined_responses[user_input.lower()]}')
            continue

        # Analyze sentiment of the user input and respond accordingly
        sentiment = analyze_sentiment(user_input)
        if sentiment > 0:
            type_response("You seem positive!")
        elif sentiment < 0:
            type_response("You seem negative!")
        else:
            type_response("You seem neutral!")

        # Find the best match for the user's question
        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print(f'Bot: {answer}')
        else:
            print('Bot: I don\'t know the answer. Can you teach me?')
            new_answer: str = input('Type the answer or "skip" to skip: ')
            
            if new_answer.lower() != 'skip':
                # Add the new question and answer to the knowledge base
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                save_knowledge_base('knowledgeBase.json', knowledge_base)  # Save the updated knowledge base
                print('Bot: Thank you! I learned something today!')

# Entry point for the script
if __name__ == '__main__':
    chat_bot()
