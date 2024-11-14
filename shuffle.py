from random import shuffle
deck = [{'value':i, 'suit':c}
    for c in ['spades', 'clubs', 'hearts', 'diamonds']
    for i in range(1,14)]
print(len(deck))
print()
shuffle(deck)
print(deck)



