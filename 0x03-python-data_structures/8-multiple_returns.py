#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == '':
        char_1 = None
    else:
        char_1 = sentence[0]
        a, b = len(sentence), char_1
        return (a, b)
