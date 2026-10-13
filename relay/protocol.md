# Relay battle protocol

The future online relay should keep simulation authoritative on the server.

## Client messages

- `join_room { roomCode }`
- `select_character { characterId }`
- `submit_move { turn, move }`
- `rematch {}`

## Server messages

- `room_state { roomCode, seats, phase }`
- `battle_snapshot { revision, turn, fighters, timer, glitch }`
- `round_result { revision, notes, hp }`
- `battle_end { winner, exp, reason }`

Clients must ignore stale revisions, reject unknown move names, and never authoritatively mutate HP, scores, timer, or room membership.
