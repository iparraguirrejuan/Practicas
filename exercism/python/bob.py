"""
Instructions
Your task is to determine what Bob will reply to someone when they say something to him or ask him a question.

Bob only ever answers one of five things:

"Sure." This is his response if you ask him a question, such as "How are you?" The convention used for questions is that it ends with a question mark.
"Whoa, chill out!" This is his answer if you YELL AT HIM. The convention used for yelling is ALL CAPITAL LETTERS.
"Calm down, I know what I'm doing!" This is what he says if you yell a question at him.
"Fine. Be that way!" This is how he responds to silence. The convention used for silence is nothing, or various combinations of whitespace characters.
"Whatever." This is what he answers to anything else.
"""

def response(hey_bob):
    hey_bob1 = hey_bob.strip()
    if not hey_bob1:
        return 'Fine. Be that way!'
    elif hey_bob1.endswith("?") and hey_bob1.isupper():
        return "Calm down, I know what I'm doing!"
    elif hey_bob1.endswith("?"):
        return "Sure."
    elif hey_bob1.isupper():
        return "Whoa, chill out!"
    else:
        return "Whatever."
