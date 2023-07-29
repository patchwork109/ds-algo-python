# https://leetcode.com/problems/ransom-note/
# Given two strings ransomNote and magazine, return true if ransomNote 
# can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.
# ransomNote = "a", magazine = "b" --> False

ransomNote = "a"
magazine = "b"

ransomNote2 = "aa"
magazine2 = "ab"

ransomNote3 = "aa"
magazine3 = "aab"

ransomNote4 = "fihjjjjei"
magazine4 = "hjibagacbhadfaefdjaeaebgi"


def ransom_note(ransomNote, magazine):
    seen_chars_mag = {}
    seen_chars_rn = {}

    for char in magazine:
        if char not in seen_chars_mag:
            seen_chars_mag[char] = 1
        else: 
            seen_chars_mag[char] += 1

    for char in ransomNote:
        if char not in seen_chars_rn:
            seen_chars_rn[char] = 1
        else:
            seen_chars_rn[char] += 1

    for key, value in seen_chars_rn.items():
        if key not in seen_chars_mag or value > seen_chars_mag[key]:
            return False
    return True


print(ransom_note(ransomNote, magazine))
print(ransom_note(ransomNote2, magazine2))
print(ransom_note(ransomNote3, magazine3))
print(ransom_note(ransomNote4, magazine4))


def ransom_note2(ransomNote, magazine):
    mag_chars = {}

    for char in magazine:
        if char not in mag_chars:
            mag_chars[char] = 1
        else:
            mag_chars[char] += 1
    
    for char in ransomNote:
        if char not in mag_chars or mag_chars[char] == 0:
            return False
        mag_chars[char] -= 1

    return True

print(ransom_note2(ransomNote, magazine))
print(ransom_note2(ransomNote2, magazine2))
print(ransom_note2(ransomNote3, magazine3))
print(ransom_note2(ransomNote4, magazine4))

