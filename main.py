# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])
lastopened = ["char", "position"]  # store last opening bracket


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
        lastopened[0] = next
        lastopened[1] = i+1
        if next in ")]}":
            if len(opening_brackets_stack) == 0:
                return i+1
            if not are_matching(opening_brackets_stack[len(opening_brackets_stack)-1], next):
                return i+1
            opening_brackets_stack.pop(len(opening_brackets_stack)-1)
    if len(opening_brackets_stack) == 0:
        return "Success"
    else:
        return lastopened[1]


def main():
    if input() == "I":
        text = input()
        mismatch = find_mismatch(text)
        print(mismatch)


if __name__ == "__main__":
    main()
