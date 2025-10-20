"""
logic.py - Core game logic
"""

from typing import Set, Tuple, List

def render_state(secret: str, guessed: Set[str]) -> str:
    """Show the secret word with hidden letters (_ a _ e)"""
    result: List[str] = []
    for ch in secret:
        if not ch.isalpha():
            result.append(ch)
        elif ch.lower() in guessed:
            result.append(ch)
        else:
            result.append("_")
    return " ".join(result)

def is_win(secret: str, guessed: Set[str]) -> bool:
    """Return True if player guessed all letters."""
    needed = {c.lower() for c in secret if c.isalpha()}
    return needed.issubset(guessed)

def valid_guess(raw: str) -> Tuple[bool, str]:
    """Check if input is a valid single alphabet letter."""
    if not raw:
        return False, ""
    s = raw.strip().lower()
    if len(s) != 1:
        return False, ""
    if not s.isalpha():
        return False, ""
    return True, s

def process_guess(guess: str, secret: str, guessed: Set[str], slices: int) -> Tuple[Set[str], int, str]:
    """Check the guess and return result."""
    guess = guess.lower()
    if guess in guessed:
        return guessed, slices, "already_guessed"
    guessed.add(guess)
    if guess in {c.lower() for c in secret if c.isalpha()}:
        return guessed, slices, "correct"
    else:
        return guessed, slices - 1, "incorrect"
