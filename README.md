#  Unique Approach to Longest Palindromic Substring
Using repeated-character pairs and averages to predict palindrome centers reduces the number of expansions.
[LeetCode Problem #5](https://leetcode.com/problems/longest-palindromic-substring/)

#  Problem Summary:
Given a string s, return the longest palindromic substring in s.

#  Approach:
1. **Identify repeated characters**  
   - For each character in the string, store all indices where it occurs.  
   - Palindromes are symmetric, so repeated characters often define potential palindrome boundaries.
2. **Compute candidate centers using averages**  
   - For each pair of repeated indices `(i, j)`, compute `(i + j)/2` as the potential center of symmetry.  
   - Multiple pairs with the same average indicate a symmetric structure.
3. **Expand around candidate centers**  
   - Check characters outward from the center to confirm the palindrome.  
   - Keep track of the longest palindrome found.
4. **Fallback for single characters or non-repeating sections**  
   - If no repeated-character centers produce a longer palindrome, expand around every character/gap to ensure correctness.
  
#  Edge Cases
- Empty string → returns `""`  
- All identical characters → returns the full string  
- Single-character string → returns the character itself

#  Advantages:
- Reduces unnecessary expansions by focusing on likely centres.
- Leverages mathematical symmetry of palindromes
- Handles odd as well as even length palindromes
