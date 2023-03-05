import emoji
from chat import menu, greeting, regards


greeting()

while input(emoji.emojize(":waving_hand:")) != 'bye':
    if menu() == 'quit':
        break

regards()
