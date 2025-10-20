# Save the Watermelon - Test Plan

## Test Matrix
| Test Case                  | Input            | Expected Output                     |
|----------------------------|----------------|-----------------------------------|
| Correct guess               | letter in word  | Letter revealed                    |
| Incorrect guess             | letter not in word | Slices decrease by 1             |
| Repeat guess                | same letter     | Display "Already guessed"          |
| Win condition               | all letters guessed | Display "You saved the watermelon!" |
| Lose condition              | slices reach 0  | Display "Oh no! The melon was sliced." |

## Manual Test Results
- Correct guesses: ✅ works
- Incorrect guesses: ✅ slices decrease
- Repeat guesses: ✅ message displayed
- Win: ✅ displays success message
- Lose: ✅ displays fail message
