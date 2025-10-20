# Save the Watermelon - Pseudocode

FUNCTION main_game_loop
  secret ← select_secret_word()
  guessed ← ∅
  slices ← MAX_SLICES
  WHILE slices > 0 AND NOT is_win(secret, guessed)
    DISPLAY render_state(secret, guessed)
    guess ← prompt_for_letter()
    IF guess already in guessed THEN
      DISPLAY "Already guessed"
      CONTINUE
    ENDIF
    ADD guess TO guessed
    IF guess IN secret THEN
      DISPLAY "Nice!"
    ELSE
      slices ← slices - 1
      DISPLAY "Sliced! Remaining: " + slices
    ENDIF
  ENDWHILE
  IF is_win(secret, guessed) THEN
    DISPLAY "You saved the watermelon!"
  ELSE
    DISPLAY "Oh no! The melon was sliced."
END FUNCTION
