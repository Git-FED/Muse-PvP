"""Small EXP progression module for Muse PVP."""

from dataclasses import dataclass


@dataclass
class Profile:
    level: int = 1
    exp: int = 0
    wins: int = 0

    @property
    def next_level_exp(self) -> int:
        return 100 + (self.level - 1) * 60

    def award_win(self, amount: int = 40) -> list[str]:
        messages = [f"+{amount} EXP // relay victory"]
        self.exp += amount
        self.wins += 1
        while self.exp >= self.next_level_exp:
            self.exp -= self.next_level_exp
            self.level += 1
            messages.append(f"LEVEL UP // now level {self.level}")
        return messages
