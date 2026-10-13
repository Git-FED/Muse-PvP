"""In-memory local room manager used as a reference for a future socket service."""

from dataclasses import dataclass, field
import secrets


@dataclass
class Room:
    code: str
    seats: list[str | None] = field(default_factory=lambda: [None, None])
    phase: str = "lobby"

    def join(self, player_id: str) -> int:
        if player_id in self.seats:
            return self.seats.index(player_id)
        for index, seat in enumerate(self.seats):
            if seat is None:
                self.seats[index] = player_id
                return index
        raise ValueError("room is full")


def new_room() -> Room:
    return Room(code=secrets.token_hex(2).upper())
