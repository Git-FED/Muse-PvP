"""Practice AI with a deliberately small, readable policy."""

import random


def choose_move(opponent_hp: int, opponent_energy: int, player_hp: int, rng=None) -> str:
    rng = rng or random
    if opponent_hp <= 24 and opponent_energy >= 1:
        return "attack"
    if player_hp <= 28 and opponent_energy < 2:
        return "charge"
    roll = rng.random()
    if roll < 0.46:
        return "attack"
    if roll < 0.72:
        return "guard"
    return "charge"
