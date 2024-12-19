# -*- coding: utf-8 -*-
"""Untitled39.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RpWSznxGDr_m29mHqZqA1qG1dENF38wQ
"""

import random

characters = ["a brave knight", "a curious cat", "a wise wizard", "a young adventurer", "an old fisherman"]
settings = ["in a mystical forest", "on a distant island", "in a bustling city", "on top of a snowy mountain", "in a secret underground cave"]
conflicts = ["finds a hidden treasure", "fights a dangerous dragon", "uncovers an ancient secret", "has to save a village", "embarks on a dangerous quest"]
helpers = ["an intelligent talking owl", "a loyal dog", "a powerful sorcerer", "a clever thief", "a mystical sword"]
twists = ["but a dark force tries to stop them", "but they discover an unexpected betrayal", "and everything turns out to be a dream", "but they must make a terrible sacrifice", "and they find an unlikely ally in their enemy"]

def generate_story():
    character = random.choice(characters)
    setting = random.choice(settings)
    conflict = random.choice(conflicts)
    helper = random.choice(helpers)
    twist = random.choice(twists)

    story = (f"Once upon a time, {character} was {setting} when they {conflict}. "
             f"Along the way, they were helped by {helper}, "
             f"but {twist}.")
    return story

print(generate_story())