'''
Longest Word
Given a text as input, find and output the longest word.
'''
text = input().split()
length = [len(x) for x in text]
maximum = max(length)
text_index = length.index(maximum)
print(text[text_index])