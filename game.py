from typing import List, Dict, Tuple
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
        """Returns the current question"""
        return self.questions[self.current_q_index]

    def is_ended(self) -> bool:
        """Returns true if the game is ended"""
        return len(self.questions) > 0 and self.current_q_index >= len(self.questions)

    def leaderboard(self) -> List[Tuple[str, int]]:
        """Returns a sorted list of tuples of the players and their scores"""
        return sorted(self.scores.items(), key=lambda x: x[1], reverse=True)


# Track one game state per channel
game_channels: dict[int, GameState] = {}


def must_get_game(
    channel_id: int | None,
    create=False,
) -> GameState | None:
    """
    Returns the game state for the channel ID, if it exists.
    If create=True, it will create a new game state if one does not exist.
    """
    # A safety check to ensure we have a valid channel ID before doing anything
    # with it in our code
    assert channel_id is not None

    game_state = game_channels.get(channel_id)
    # If there is a channel that doesnt have a game running
    if game_state is None:
        # If we want to create a new game, create a new game state with the
        # channel id
        if create:
            game_state = GameState()
            game_channels[channel_id] = game_state
        else:
            return None

    if game_state.is_ended():
        return None

    return game_state


def create_game(channel_id: int) -> GameState:
    """Creates a new game state for the channel and returns it"""
    game_state = must_get_game(channel_id, create=True)
    assert game_state is not None
    return game_state
