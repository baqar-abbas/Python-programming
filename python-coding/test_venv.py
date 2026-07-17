import cowsay

cowsay.cow("Good Mooooorning!")

name = input("What is your name? ").strip()
mood = input("How are you feeling today? ").strip().lower()

if mood in ["happy", "good", "great", "fantastic", "fine"]:
    message = f"Hello {name}! Great to hear you're feeling {mood} today."
elif mood in ["sad", "bad", "not good", "terrible", "tired", "low"]:
    message = f"Hi {name}. Sorry you're feeling {mood}. Hope things get better soon."
else:
    message = f"Hello {name}! Thanks for sharing that you're feeling {mood}."

cowsay.cow(message)

# Output when running the script:
# python test_venv.py
#   _________________
# | Good Mooooorning! |
#   =================
#                  \
#                   \
#                     ^__^
#                     (oo)\_______
#                     (__)\       )\/\
#                         ||----w |
#                         ||     ||
# What is your name? Baqar
# How are you feeling today? good
#   _________________________________________________
#  /                                                 \
# | Hello Baqar! Great to hear you're feeling good to |
# | day.                                              |
#  \                                                 /
#   =================================================
#                                                  \
#                                                   \
#                                                     ^__^
#                                                     (oo)\_______
#                                                     (__)\       )\/\
#                                                         ||----w |
#                                                         ||     ||