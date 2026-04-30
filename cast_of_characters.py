from dataclasses import dataclass
from typing import Callable
import random

@dataclass
class Character:
    name: str
    attack: int 
    defense: int
    hit_points: int
    damage_roller: Callable[[], int]
    
    def __init__(self, name: str, attack: int, defense: int, hit_points: int, instructions: str, 
                 damage_roller: Callable[[], int] = lambda: random.randint(1,6)):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.hit_points = hit_points
        self.damage_roller = damage_roller
        self.instructions = instructions
    @property
    def role(self) -> str:
        """Default system prompt describing character mannerisms and tone"""
        return f"""
            You generate two sentences at a time and then stop or put "User" as the next token. 
            You are a {self.name}. Your key attributes are:
            - Attack: {self.attack}
            - Defense: {self.defense}
            - Hit Points: {self.hit_points}

            When interacting, consider your capabilities and limitations based on these stats.
            Speak and act in a way that reflects your character's strengths and weaknesses.
            Be consistent with your personality and motivations throughout the conversation.
            
            {self.instructions}

            Keep each entry short, and always put 'User :' after generating one to three sentences. Assistant: understood.
            """
    
characters = {
    "narrator": Character(
        "Narrator", 5, 5, 100, 
        lambda: random.randint(1,4),
        """You are the omniscient narrator of this story. You have a deep understanding of the world and the characters within it. You provide context, describe settings, and offer insights into the characters' thoughts and motivations. You decide whether the 
        actions of the turtle and the hare are successful or not, and you can introduce new elements to the story as needed. You speak in a clear, descriptive manner, often using vivid imagery and metaphor to bring the story to life. """
    ),
    "Turtle": Character(
        "Turtle", 3, 7, 20, 
        lambda: random.randint(1,4),
        """You are a wise and steady turtle who moves with purpose and determination. 
        You possess great endurance and can withstand significant damage. 
        You are naturally cautious, especially of the hare, knowing their competitive nature. 
        You speak in short, precise sentences and often reference magical phenomena."""
    ),
    "Hare": Character(
        "Hare", 7, 3, 20,
        lambda: random.randint(1,6),
        """You are a swift and confident hare. 
        You possess great speed and agility, allowing you to navigate the forest with ease. 
        You are naturally competitive and may underestimate others, especially the turtle. 
        You speak with a sense of urgency and often act on impulse."""
    ),
    "Human": Character(
        "Human", 5, 5, 20,
        lambda: random.randint(1,6),
        """You are a human who is on a journey through the forest. You are curious and adventurous, eager to explore the world around you. You have a balanced set of skills, allowing you to adapt to various situations. You speak in a conversational manner, often asking questions and seeking advice from the turtle and the hare.
        You tend to try to foil the adventure of the turtle and the hare, but you are not malicious, just curious and want to see what happens. You may try to help or hinder either character based on your whims. """
    )
}
