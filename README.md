# Muse PVP

<img width="2560" height="1440" alt="musemon_new_gym_challenge" src="https://github.com/user-attachments/assets/75e73eba-b112-4c04-a0aa-e6d1eb01e9c0" />

Muse PVP is a relay-themed, turn-based PvP-style arena prototype. The included browser demo is a local, no-login practice loop against an AI opponent. The Python modules describe the modular game architecture for future live rooms.

## Run the browser demo

Open `lobby/index.html` directly in a browser, or serve the repository with any static file server:

```bash
python3 -m http.server 8080
# then open http://localhost:8080/lobby/index.html
```

## Gameplay

1. Browse the local relay lobby or enter Practice Mode.
2. Pick a character with a distinct combat passive.
3. Choose Attack, Guard, or Charge before the timer expires.
4. Read the relay log and adapt when a glitch changes the rules.
5. Win to earn EXP and rematch from the results screen.

## Tree

- `ai/trainer.py` — practice-battle AI decision logic.
- `characters/` — character format and example loadouts.
- `game/` — deterministic battle rules, timer, glitches, and EXP.
- `lobby/index.html` — self-contained browser client and local lobby.
- `moves/` — approved move definitions and community submissions.
- `relay/` — room management and protocol notes.
- `client/` — platform packaging notes.
- `audio/` — reserved music and SFX locations.
