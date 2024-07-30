Project Purpose
This CLI chatbot provides interactive communication with users by responding to predefined commands and dynamically learning new questions and answers. It also analyzes sentiment to provide feedback on user input.

Features
Predefined Responses: Handles specific queries like greetings and help commands.
Dynamic Learning: Updates its knowledge base with new questions and answers.
Sentiment Analysis: Offers feedback based on the sentiment of user input.
Typing Simulation: Simulates a typing effect for responses.
Requirements
Python 3.x
Dependencies: Install with:
bash
Copy code
pip install textblob
Running the Chatbot
Install Dependencies:
Ensure you have the required libraries:

bash
Copy code
pip install textblob
Execute the Script:
Run the chatbot using Python:

bash
Copy code
python chatbot.py
Interact with the Chatbot:

Type your questions or commands.
Type "exit" to end the session or "quit" to stop the program.
Example Interaction
vbnet
Copy code
You: hello
Bot: Hi there!

You: how are you
Bot: I'm a chatbot, so I don't have feelings, but thanks for asking!

You: help
Bot: Available commands:
 - 'help': List available commands and instructions.
 - 'exit': Quit the chatbot.
You can ask me anything!

You: what is the capital of France?
Bot: I don't know the answer. Can you teach me?
Type the answer or "skip" to skip: Paris
Bot: Thank you! I learned something today!

Notes:
Make sure knowledgeBase.json is correctly formatted with a "questions" key containing question-answer pairs.
Adjust sentiment analysis and typing delay in the script if needed.
