"""Relay glitches are bounded rule modifiers, not arbitrary client effects."""

from dataclasses import dataclass
import random


@dataclass(frozen=True)
class Glitch:
    id: str
    title: str
    description: str
    damage_multiplier: float = 1.0
    timer_seconds: int | None = None


GLITCHES = (
    Glitch("static", "STATIC BLOOM", "All attacks hit 15% harder.", 1.15),
    Glitch("short-circuit", "SHORT CIRCUIT", "The next turn is only 7 seconds.", 1.0, 7),
    Glitch("soft-reset", "SOFT RESET", "Both fighters recover 6 HP, but charge is cleared.", 1.0),
)


def roll_glitch(rng: random.Random | None = None) -> Glitch:
    return (rng or random).choice(GLITCHES)
