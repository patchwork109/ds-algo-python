# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
# Given two strings needle and haystack, return the index of the first occurrence of 
# needle in haystack, or -1 if needle is not part of haystack.
# haystack = "sadbutsad", needle = "sad" --> 0 (the first occurrence is at index 0)
# haystack = "leetcode", needle = "leeto" --> -1 (leeto is not part of leetcode)

haystack = "hellosadbutsad"
needle = "sad"

def index_of_first_occurrence(needle, haystack):
    for index in range(len(haystack)):
        if haystack[index:index + len(needle)] == needle:
            print(f"{needle} is in {haystack}")
            print(f"The index is {index}")
            return index
    return -1

print(index_of_first_occurrence(needle, haystack))