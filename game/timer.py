"""Move timer rules. A player that reaches zero loses the round."""

from dataclasses import dataclass


@dataclass
class MoveTimer:
    seconds: int = 12
    remaining: float = 12.0

    def reset(self, seconds: int | None = None) -> None:
        if seconds is not None:
            self.seconds = seconds
        self.remaining = float(self.seconds)

    def tick(self, elapsed: float) -> bool:
        self.remaining = max(0.0, self.remaining - elapsed)
        return self.remaining <= 0

    @property
    def timed_out(self) -> bool:
        return self.remaining <= 0
