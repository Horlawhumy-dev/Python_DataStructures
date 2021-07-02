# Letter Frequency

import math
# You are making a program to analyze text.
# Take the text as the first input and a letter as the second input, and output the frequency of that letter in the text as a whole percentage.

# Sample Input:
# hello
# l

# Sample Output:
# 40

# The letter l appears 2 times in the text hello, which has 5 letters. So, the frequency would be (2/5)*100 = 40

#your code goes here

text = input("Enter your sample text: ")
letter = input("Enter the letter to be counted: ")

if letter in text:
    result = text.count(letter) / len(text) * 100
    print(str(math.floor(result)) + '%')