"""Deterministic turn resolver used by the local demo and future relay server."""

from dataclasses import dataclass, field
from typing import Literal

MoveName = Literal["attack", "guard", "charge"]


@dataclass
class Fighter:
    name: str
    hp: int = 100
    max_hp: int = 100
    energy: int = 1
    guarded: bool = False
    charged: bool = False


@dataclass
class RoundResult:
    attacker_move: MoveName
    defender_move: MoveName
    damage_to_attacker: int = 0
    damage_to_defender: int = 0
    notes: list[str] = field(default_factory=list)


class Battle:
    def __init__(self, player: Fighter, opponent: Fighter):
        self.player = player
        self.opponent = opponent
        self.turn = 1
        self.glitch_multiplier = 1.0

    @staticmethod
    def _base_damage(move: MoveName, charged: bool) -> int:
        if move != "attack":
            return 0
        return 18 if charged else 12

    def resolve(self, player_move: MoveName, opponent_move: MoveName) -> RoundResult:
        result = RoundResult(player_move, opponent_move)
        p, o = self.player, self.opponent
        p.guarded = player_move == "guard"
        o.guarded = opponent_move == "guard"
        p.charged = player_move == "charge"
        o.charged = opponent_move == "charge"

        if player_move == "guard":
            p.energy = min(3, p.energy + 1)
        if opponent_move == "guard":
            o.energy = min(3, o.energy + 1)
        if player_move == "charge":
            p.energy = min(3, p.energy + 1)
        if opponent_move == "charge":
            o.energy = min(3, o.energy + 1)

        p_damage = int(self._base_damage(opponent_move, o.charged) * self.glitch_multiplier)
        o_damage = int(self._base_damage(player_move, p.charged) * self.glitch_multiplier)
        if p.guarded:
            p_damage = max(0, p_damage // 3)
        if o.guarded:
            o_damage = max(0, o_damage // 3)
        if player_move == "attack" and opponent_move == "charge":
            result.notes.append("Your attack interrupts the charge.")
        if player_move == "charge" and opponent_move == "attack":
            result.notes.append("The opponent catches you charging.")

        p.hp = max(0, p.hp - p_damage)
        o.hp = max(0, o.hp - o_damage)
        result.damage_to_attacker = p_damage
        result.damage_to_defender = o_damage
        self.turn += 1
        return result
