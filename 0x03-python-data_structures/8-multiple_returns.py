#!/usr/bin/python3
def multiple_returns(sentence):
    first = ""
    length = len(sentence)
    if not sentence:
        first = "None"
    else:
        first = sentence[0]
    return first, length
