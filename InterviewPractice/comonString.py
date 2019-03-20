# Given two strings, determine if they share a common substring.
# A substring may be as small as one character.

# For example, the words "a", "and", "art" share the common substring .
# The words "be" and "cat" do not share a substring.


def twoStrings(s1, s2):
    s1 = set(s1)
    s2 = set(s2)

    result = s1.intersection(s2)

    if result:
        return "YES"
    return "NO"

