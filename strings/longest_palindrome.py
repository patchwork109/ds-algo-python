# https://leetcode.com/problems/longest-palindrome/
# Given a string s which consists of lowercase or uppercase letters, 
# return the length of the longest palindrome that can be built with 
# those letters.

# Letters are case sensitive, for example, "Aa" is not considered a 
# palindrome here.

# s = "abccccdd" --> 7
# s = "a" --> 1

s = "abccccdd"
s2 = "a" 
s3 = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"

def longest_palindrome(s):
    seen_char_count = {}

    for char in s:
        if char not in seen_char_count:
            seen_char_count[char] = 1
        else:
            seen_char_count[char] += 1

    longest_count = []
    max_single_char = [0]

    for value in seen_char_count.values():
        if value >= 2 and value % 2 == 0:
            longest_count.append(value)
    
        elif value % 2 != 0:
            max_single_char.append(value)
    
    print(seen_char_count)
    print(sum(longest_count))
    print((max_single_char))
    print(max(max_single_char))        
    
    return sum(longest_count) + max(max_single_char)


print(longest_palindrome(s))
print(longest_palindrome(s2))
print(longest_palindrome(s3))



def longestPalindrome(s):
    odd_count = 0
    d = {}
    for char in s:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
        if d[char] % 2 == 1:
            odd_count += 1
        else:
            odd_count -= 1
    if odd_count > 1:
        return len(s) - odd_count + 1
    return len(s)

print(longestPalindrome(s))
print(longestPalindrome(s2))
print(longestPalindrome(s3))
