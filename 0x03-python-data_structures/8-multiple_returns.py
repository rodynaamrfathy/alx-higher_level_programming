#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        length =  len(sentence)
        first_char = = sentence[0]
        t = tuple((length, first_char))
        return t
    else:
        return 0, None
