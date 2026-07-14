#Q1. Count Characters
def countCharacters(S):
    a = 0
    d = 0

    for ch in S:
        if ch == 'A':
            a += 1
        elif ch == 'D':
            d += 1

    return [a, d]
#Q2. Count the Heads
def Count_Head(S):
    freq = {}

    for ch in S:
        freq[ch] = freq.get(ch, 0) + 1

    ans = ""

    for ch in sorted(freq):
        if freq[ch] > 1:
            ans += ch + str(freq[ch]) + " "

    return ans.strip()
#Q3. Count the Vowels
def Count_Vowel(S):
    count = 0
    vowels = "aeiouAEIOU"

    for ch in S:
        if ch in vowels:
            count += 1

    return count
#Q4. Concatenate the Strings
def Concatenate_Strings(S1, S2):
    return S1 + S2
#Q5. Find Length (Without len())
def findLength(S):
    count = 0

    for _ in S:
        count += 1

    return count
#Q6. Find the Winner
def Game_Winner(S):
    a = 0
    d = 0

    for ch in S:
        if ch == 'A':
            a += 1
        else:
            d += 1

    if a > d:
        return "Aditya"
    elif d > a:
        return "Danish"
    else:
        return "Draw"
#Q7. Join Strings
def joinStrings(S, P):
    return S + P
#Q8. Palindrome Check
def Plain_Check(S):
    if S == S[::-1]:
        return "True"
    else:
        return "False"
#Q9. Reverse the String
def Reverse_String(S):
    return S[::-1]

#Q10. Match the Strings
def String_Match(S1, S2):
    if S1 == S2:
        return "YES"
    else:
        return "NO"
#Q11. String Replace
def Replace(S, pattern, text):
    return S.replace(pattern, text)
#Q12. Split the String
def Split_the_String(S):
    return S.split()
#Q13. Count the Vowels and Consonants
def Count_Vowels(S):
    count = 0
    vowels = "aeiouAEIOU"

    for ch in S:
        if ch in vowels:
            count += 1

    return count


def Count_Consonants(S):
    count = 0
    vowels = "aeiouAEIOU"

    for ch in S:
        if ch.isalpha() and ch not in vowels:
            count += 1

    return count
