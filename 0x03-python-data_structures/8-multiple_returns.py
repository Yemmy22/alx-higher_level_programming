#!/usr/bin/python3
def multiple_returns(sentence):
    for i in range(len(sentence)):
        i += 1

    if i == 0:
        return None
    else:
        return i, sentence[0]
