import discord
import json
import time
from difflib import get_close_matches

Brain = 'Brain.json'
intents = discord.Intents.default()
client = discord.Client(intents=intents)

print("Hi, This is my Discord Chatbot")
print("The responses the bot gives might not always be accurate.")
print("-" * 10)
time.sleep(3)


def load_knowledge_base(file_path: str):
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data


def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


def find_best_match(user_question: str, questions: list[str]):
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.80)
    return matches[0] if matches else None


def get_answer_for_question(question: str, knowledge_base: dict):
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]


@client.event
async def on_ready():
    print(f'logged in as {client.user}')


@client.event
async def on_message(message):
    print(f"Received message from {message.author}")

    if message.author == client.user or message.author.name == "Gamer AI":
        return

    if message.content.lower().startswith('/ai'):
        user_input = message.content[len('/ai'):].strip()

        knowledge_base: dict = load_knowledge_base(Brain)

        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            await message.channel.send(f'Bot: {answer}')
        else:
            await message.channel.send('Bot: I don\'t know the answer. Can you teach me?(Type the awnser withought the /ai)')
            response = await client.wait_for('message', check=lambda m: m.author == message.author)

            if response.content.lower() != 'skip':
                knowledge_base["questions"].append({"question": user_input, "answer": response.content})
                save_knowledge_base(Brain, knowledge_base)
                await message.channel.send("Bot: Thank you! I learned a new Response!")


client.run('Discord bot token')
