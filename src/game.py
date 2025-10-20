"""
game.py - Run this file to play the game!
"""

import sys
from typing import Set
from words import load_words, pick_random
from logic import render_state, is_win, valid_guess, process_guess

MAX_SLICES = 6  # 최대 시도 횟수

def prompt_for_letter() -> str:
    """Ask player for a valid letter."""
    while True:
        raw = input("Guess a letter: ").strip()
        valid, ch = valid_guess(raw)
        if not valid:
            print("⚠️  Please enter one alphabet letter (a-z).")
            continue
        return ch

def play_game(word_source_path: str = None) -> None:
    """Run one game round."""
    word_list = load_words(word_source_path)
    secret = pick_random(word_list)
    guessed: Set[str] = set()
    slices = MAX_SLICES

    print("\n🍉 Welcome! Save the watermelon before it’s sliced!")
    while slices > 0 and not is_win(secret, guessed):
        print("\nWord:", render_state(secret, guessed))
        print(f"Slices left: {slices}")
        print(f"Guessed: {', '.join(sorted(guessed)) or '(none)'}")

        guess = prompt_for_letter()
        guessed, slices, result = process_guess(guess, secret, guessed, slices)

        if result == "already_guessed":
            print(f"⚠️  You already guessed '{guess}'.")
        elif result == "correct":
            print(f"✅ Correct! '{guess}' is in the word.")
        else:
            print(f"❌ Wrong! '{guess}' is not in the word. Slices left: {slices}")

    if is_win(secret, guessed):
        print("\n🎉 You saved the watermelon! The word was:", secret)
    else:
        print("\n💀 The watermelon was sliced! The word was:", secret)

def main():
    """Main loop with replay option."""
    try:
        play_game()
        while True:
            again = input("\nPlay again? (y/n): ").strip().lower()
            if again in ("y", "yes"):
                play_game()
            elif again in ("n", "no"):
                print("👋 Thanks for playing!")
                break
            else:
                print("Please type 'y' or 'n'.")
    except KeyboardInterrupt:
        print("\nGoodbye!")
        sys.exit(0)

if __name__ == "__main__":
    main()
