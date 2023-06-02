#!/usr/bin/env python3
import random
import matplotlib.pyplot as plt

random.seed(43)
BOARD_SIZE = 40
DECK_SIZE = 16
DIE_SIZE = 4
community_chest_spaces = [2, 17, 33]
chance_spaces = [7, 22, 36]

GO = 0
R1 = 5
JAIL = 10
C1 = 11
E3 = 24
G2J = 30
H2 = 39
NEXT_R = "NEXT_R"
NEXT_U = "NEXT_U"
BACK_3 = "BACK_3"

def chance():
    cards = [GO, R1, JAIL, C1, E3, H2, NEXT_R, NEXT_R, NEXT_U, BACK_3] + [None] * (DECK_SIZE - 10)
    random.shuffle(cards)
    top_card = 0
    while True:
        yield cards[top_card]
        top_card = (top_card + 1) % DECK_SIZE

def community_chest():
    cards = [GO, JAIL] + [None] * (DECK_SIZE - 2)
    random.shuffle(cards)
    top_card = 0
    while True:
        yield cards[top_card]
        top_card = (top_card + 1) % DECK_SIZE

def roll():
    return random.randint(1, DIE_SIZE), random.randint(1, DIE_SIZE)

def handle_chance_strs(card, pos):
    if card == BACK_3:
        return (pos - 3) % BOARD_SIZE
    elif card == NEXT_R:
        while pos not in [5, 15, 25, 35]:
            pos = (pos + 1) % BOARD_SIZE
        return pos
    elif card == NEXT_U:
        while pos not in [12, 28]:
            pos = (pos + 1) % BOARD_SIZE
        return pos

n_turns = 1000000
freq = [0 for _ in range(40)]
pos = 0
doubles_counter = 0
cc_iter = community_chest()
ch_iter = chance()
for _ in range(n_turns):
    freq[pos] += 1
    x, y = roll()
    # Handle rolling doubles logic
    if x == y:
        doubles_counter += 1
        if doubles_counter == 3:
            pos = JAIL
            doubles_counter = 0
            continue
    else:
        doubles_counter = 0
    # Move
    pos = (pos + x + y) % BOARD_SIZE
    #Special squares
    if pos == G2J:
        pos = JAIL
    elif pos in community_chest_spaces:
        card = next(cc_iter)
        if isinstance(card, int):
            pos = card
    elif pos in chance_spaces:
        card = next(ch_iter)
        if isinstance(card, int):
            pos = card
        elif isinstance(card, str):
            pos = handle_chance_strs(card, pos)
            # if you go back 3 you might land on community chest
            if pos in community_chest_spaces:
                card = next(cc_iter)
                if isinstance(card, int):
                    pos = card


print([i for i, _ in sorted(enumerate(freq), key=lambda x: x[1], reverse=True)][:3])

x = range(len(freq))
plt.bar(x, [f/n_turns for f in freq])
plt.xlabel('square')
plt.ylabel('freq')
plt.show()
