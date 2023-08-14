#!/usr/bin/python3
def multiple_returns(sentence):

    if sentence == '':
        b = None
    else:
        b = sentence[0]
    return (len(sentence), b)
