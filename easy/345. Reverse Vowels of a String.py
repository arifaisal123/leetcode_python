"""
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"
 
Constraints:
1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_order = []
        reverse_vowels = []
        j = -1
        for letter in s:
            if letter.lower() in ["a", "e", "i", "o", "u"]:
                vowel_order.append(letter)
                reverse_vowels.append(0)
            else:
                reverse_vowels.append(letter)
        for i in range(len(reverse_vowels)):
            if reverse_vowels[i] == 0:
                reverse_vowels[i] = vowel_order[j]
                j -= 1
        return "".join(reverse_vowels)
        