import random

def verify(password):
    return random.choice([True, False]), "Checking pass:" + password