import json
import time
from difflib import get_close_matches
Brain = 'Brain.json'
print("Hi This is my Chatbot")
print("The responses the bot gives might not allways be accurate.")
print("-"*10)
time.sleep(3)


def load_knowledge_base(file_path: str):
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent = 2)


def find_best_match(user_question:str, questions: list[str]):
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.8)
    return matches[0] if matches else None

def get_awnser_for_question(question: str, knowledge_base: dict):
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["awnser"]

def chat_bot():
    knowledge_base: dict = load_knowledge_base(Brain)

    while True:
        user_input: str = input('You: ')
        if user_input.lower() == 'quit':  # corrected comparison
            break
        
        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            awnser: str = get_awnser_for_question(best_match, knowledge_base)
            print(f'bot: {awnser}')
        else:
            print('Bot: I don\'t know the answer. Can you teach me?')
            new_answer: str = input('Type the answer or "skip" to skip: ')

            if new_answer.lower() != 'skip':
                knowledge_base["questions"].append({"question": user_input, "awnser": new_answer})
                save_knowledge_base(Brain, knowledge_base)
                print("Bot: Thank you! I learned a new Response!")

if __name__ == '__main__':
    chat_bot()