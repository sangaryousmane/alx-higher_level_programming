#!/usr/bin/python3
def multiple_returns(sentence):
    
    if sentence == '':
        a, b = len(sentence), None
    else:
        b = sentence[0]
    return (a, b)
