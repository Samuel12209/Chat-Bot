import json
from difflib import get_close_matches
brain = 'Brain.json'

def load_brain(brain: str):
    with open(brain, 'r') as file:
        data: dict = json.load_brain
    return data