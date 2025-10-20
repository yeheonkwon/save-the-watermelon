# Save the Watermelon - Design

## Problem Statement
Save the watermelon by guessing the correct letters before it is sliced.

## Target Audience
beginners who enjoy word-guessing games.

## Game Rules
- Randomly select a secret word.
- Show a masked version of the word (e.g., _ a _ e).
- Player guesses letters one by one.
- Correct guesses reveal letters.
- Incorrect guesses reduce slices (lives).
- Win if all letters are revealed before slices run out.
- Lose if slices reach 0.

## Core Features (Must-have)
- Random word selection
- Masked word display
- Input validation (single letter, no duplicates)
- Slice counter
- Win/Lose conditions

## Stretch Goals (Optional)
- ASCII art stages
- Difficulty levels
- Word categories
- Scoreboard

## Basic Flow
1. Start game
2. Select secret word
3. Loop:
   - Display word state
   - Ask for a letter
   - Validate input
   - Update guessed letters and slices
4. Check win/lose
5. End game
