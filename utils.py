from typing import List, Dict
from dataclasses import dataclass


# Using a dataclass basically generates constructor along
# with others (constructor == __init__)
@dataclass
class Question:
    question: str
    choices: List[str]
    answer: str


class GameState:
    current_q_index = 0

    # Hold the players username as the key and the score as the value
    scores: Dict[str, int] = {}
    # Holds the question, choices, answer
    questions: List[Question] = []
    # If game is running
    is_running: bool = False

    def get_current_question(self) -> Question:
        return self.questions[self.current_q_index]

    def is_ended(self) -> bool:
        return len(self.questions) > 0 and self.current_q_index >= len(self.questions)


# Track one game state per channel
game_channels: dict[int, GameState] = {}