# Save the Watermelon - Pseudocode

# 

# MAIN GAME LOOP

# ----------------

# FUNCTION main\_game\_loop

# &nbsp;   secret ← select\_secret\_word()

# &nbsp;   guessed ← empty set

# &nbsp;   slices ← MAX\_SLICES

# 

# &nbsp;   WHILE slices > 0 AND NOT is\_win(secret, guessed)

# &nbsp;       DISPLAY render\_state(secret, guessed)

# &nbsp;       DISPLAY "Slices left: ", slices

# &nbsp;       DISPLAY "Guessed letters: ", guessed

# 

# &nbsp;       guess ← prompt\_for\_letter()

# &nbsp;       IF guess already in guessed THEN

# &nbsp;           DISPLAY "Already guessed"

# &nbsp;           CONTINUE

# &nbsp;       ENDIF

# 

# &nbsp;       ADD guess TO guessed

# 

# &nbsp;       IF guess IN secret THEN

# &nbsp;           DISPLAY "Correct! '" + guess + "' is in the word."

# &nbsp;       ELSE

# &nbsp;           slices ← slices - 1

# &nbsp;           DISPLAY "Wrong! Remaining slices: " + slices

# &nbsp;       ENDIF

# &nbsp;   ENDWHILE

# 

# &nbsp;   IF is\_win(secret, guessed) THEN

# &nbsp;       DISPLAY "You saved the watermelon! The word was: " + secret

# &nbsp;   ELSE

# &nbsp;       DISPLAY "The watermelon was sliced! The word was: " + secret

# &nbsp;   ENDIF

# END FUNCTION

# 

# PROMPT FOR LETTER

# -----------------

# FUNCTION prompt\_for\_letter

# &nbsp;   LOOP

# &nbsp;       DISPLAY "Guess a letter: "

# &nbsp;       INPUT raw

# &nbsp;       IF raw is not a single alphabet letter THEN

# &nbsp;           DISPLAY "Please enter one alphabet letter (a-z)."

# &nbsp;           CONTINUE

# &nbsp;       ENDIF

# &nbsp;       RETURN lowercase(raw)

# &nbsp;   END LOOP

# END FUNCTION

# 

# REPLAY LOOP

# -----------

# FUNCTION main

# &nbsp;   LOOP

# &nbsp;       CALL main\_game\_loop()

# &nbsp;       DISPLAY "Play again? (y/n): "

# &nbsp;       INPUT response

# &nbsp;       IF response IN ("n", "no") THEN

# &nbsp;           BREAK

# &nbsp;       ENDIF

# &nbsp;   END LOOP

# END FUNCTION

# 

# SUPPORTING FUNCTIONS

# --------------------

# select\_secret\_word()     - returns a random word from the word list

# render\_state(secret, guessed) - returns the masked word with guessed letters revealed

# is\_win(secret, guessed)  - returns True if all letters are guessed correctly

# 

